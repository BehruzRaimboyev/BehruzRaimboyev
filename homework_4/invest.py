def invest(amount,rate,years):
    amountss=[]
    for years in range(1,years+1):
     amount+=amount*(rate/100)
     amountss.append(amount)
    print(f'year{years}:${amount:.2f}')


