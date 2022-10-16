money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05   # сразу зададим 105%

month = 0  # количество месяцев, которое можно прожить

while money_capital >= spend:
    month += 1
    spend *= increase
    money_capital -= spend
    money_capital += salary

print(month)
