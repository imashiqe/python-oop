balance =3000

def buy_things(item,price):
    print(f'previous balance: {balance}')
    global balance
    balance = balance - price
    print(f'new balance: {item}',balance)

    buy_things('sunglass', 1000)