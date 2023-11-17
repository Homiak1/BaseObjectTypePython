money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
average_capital = money_capital + salary - spend
total_month = 0
while average_capital + salary > spend:
    average_capital = (average_capital + salary) - spend
    spend = spend * (increase + 1)
    total_month += 1
print("Количество месяцев, которое можно протянуть без долгов:", total_month)
