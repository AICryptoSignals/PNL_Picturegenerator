import sys

from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("pnl_pictures")

    return os.path.join(base_path, relative_path)

def draw_pnl_picture(coin='BNBUSDT',
                     direction='Long',
                     entry_price=333.3,
                     exit_price=355.5,
                     leverage=10):

    path = os.path.dirname(os.path.abspath(__file__))

    im = Image.open(resource_path("./pnl_background.png"))

    color_orange = (242, 97, 34)
    color_cyan = (69, 197, 224)

    # Calculate Profit
    if 'ong' in direction:
        if exit_price > entry_price:
            profit = f'+{round((exit_price-entry_price)*leverage, 2)}%'
        else:
            profit = f'{round((exit_price-entry_price)*leverage, 2)}%'
    else:
        if exit_price < entry_price:
            profit = f'+{round((entry_price-exit_price)*leverage, 2)}%'
        else:
            profit = f'{round((entry_price-exit_price)*leverage, 2)}%'

    image_editable = ImageDraw.Draw(im)

    font = ImageFont.truetype(resource_path('./Lato-Black.ttf'), size=180)
    image_editable.text((380, 500), coin, color_cyan, font=font)
    font = ImageFont.truetype(resource_path('./Lato-Regular.ttf'), size=140)
    if 'ong' in direction:
        image_editable.text((450, 750), "Long", color_cyan, font=font)
    else:
        image_editable.text((450, 750), "Short", color_cyan, font=font)

    font = ImageFont.truetype(resource_path('./Lato-Bold.ttf'), size=500)
    image_editable.text((380, 1100), profit, color_cyan, font=font)

    font = ImageFont.truetype(resource_path('./Lato-Regular.ttf'), size=150)
    image_editable.text((380, 1930), "Entry Price", color_orange, font=font)
    image_editable.text((380, 2190), "Exit Price", color_orange, font=font)
    image_editable.text((380, 2450), "Leverage", color_orange, font=font)

    image_editable.text((1450, 1930), str(entry_price), color_orange, font=font)
    image_editable.text((1450, 2190), str(exit_price), color_orange, font=font)
    image_editable.text((1450, 2450), str(leverage), color_orange, font=font)

    # Insert the QR-Code
    qr_code = Image.open(resource_path("./qr_code_crypticorn_blue.png"))
    qr_code = qr_code.resize((500, 500), Image.ANTIALIAS)
    im.paste(qr_code, (3100, 4000))

    date = datetime.now()
    im.save(f'./pnl_{coin}_{date.year}-{date.month}-{date.day}_{date.hour}-{date.minute}.png')

    return float(profit.replace('+', '').replace('%', ''))
