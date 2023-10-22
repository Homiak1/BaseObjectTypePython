salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
increased_spend = 6000
for i in range(months):
    if i == 0:
        money = salary - spend
    else:
        money = salary - increased_spend
    increased_spend = increased_spend * increase + increased_spend
    money_capital -= money
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(round(money_capital, 0)))
