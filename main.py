from picture_generator import draw_pnl_picture

if __name__ == '__main__':

    print('What coin did you trade?')
    coin = input()
    print('Wich direction did you trade? Long/Short?')
    while True:
        try:
            d = input()
            if 'ong' in d or 'l' in d or 'L' in d:
                direction = 'long'
                break
            if 'ort' in d or 's' in d or 'S' in d:
                direction = 'short'
                break
        except:
            print("Can't identify direction... Please tra again:")

    print('What was your entry price?')
    while True:
        try:
            entry_price = float(input().replace(',', '.'))
            break
        except:
            print('Please enter a number :)')

    print('What was your exit price?')
    while True:
        try:
            exit_price = float(input().replace(',', '.'))
            break
        except:
            print('Please enter a number :)')


    print('What was your leverage?')
    while True:
        try:
            leverage = int(input())
            break
        except:
            print('Please enter a number :)')


    profit = draw_pnl_picture(coin=coin,
                     direction=direction,
                     entry_price=entry_price,
                     exit_price=exit_price,
                     leverage=leverage)

    if profit > 0:
        print('Nice Trade! Share it in the Discord: https://discord.com/channels/938278313200328724/938278313686876247')


