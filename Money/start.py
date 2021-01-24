from HW_python.Money import money

m = money.MyMoney()
print(f'I have {m.select_money()}$')
m.send_money(1000)
print(f'I have {m.select_money()}$')