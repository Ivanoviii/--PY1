salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for cap in range(1, months + 1):
    cap = spend - salary
    spend *= increase + 1
    need_money += cap

print(round(need_money))
