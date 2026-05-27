# Мини-программа
# ИТОГОВАЯ МИНИ-ПРОГРАММА
# Вариант 3: Конвертер валют
# 
# Программа позволяет конвертировать рубли в доллары и евро,
# а также обратно. Работает в цикле до команды "выход".
# Содержит: переменные разных типов, условие if, цикл for, функцию def.

# ============================================
# Функция конвертации
# ============================================
def convert_currency(amount, rate, direction):
    """
    Конвертирует валюту.
    direction: 'to_usd', 'to_eur', 'to_rub'
    """
    if direction == 'to_usd':
        return amount / rate['usd']
    elif direction == 'to_eur':
        return amount / rate['eur']
    elif direction == 'to_rub':
        return amount * rate['currency_rate']
    else:
        return None

# ============================================
# Приветствие и ввод курсов
# ============================================
print("\n" + "="*50)
print("        ДОБРО ПОЖАЛОВАТЬ В КОНВЕРТЕР ВАЛЮТ")
print("="*50)

# Переменные разных типов
usd_rate = float(input("Введите курс доллара к рублю (1 USD = ? руб.): "))
eur_rate = float(input("Введите курс евро к рублю (1 EUR = ? руб.): "))

rates = {
    'usd': usd_rate,
    'eur': eur_rate
}

print(f"\nКурсы установлены: USD = {usd_rate} руб., EUR = {eur_rate} руб.")

# ============================================
# Основной цикл программы
# ============================================
while True:
    print("\n" + "-"*40)
    print("Что вы хотите сделать?")
    print("1. Рубли → Доллары")
    print("2. Рубли → Евро")
    print("3. Доллары → Рубли")
    print("4. Евро → Рубли")
    print("5. Показать текущие курсы")
    print("0. Выход")
    
    choice = input("Ваш выбор: ")
    
    # Условие выхода
    if choice == '0':
        print("\nСпасибо за использование конвертера! До свидания!")
        break
    
    # Обработка выбора пользователя
    if choice == '1':
        rub = float(input("Введите сумму в рублях: "))
        usd = convert_currency(rub, rates, 'to_usd')
        print(f"{rub:.2f} руб. = {usd:.2f} USD")
        
    elif choice == '2':
        rub = float(input("Введите сумму в рублях: "))
        eur = convert_currency(rub, rates, 'to_eur')
        print(f"{rub:.2f} руб. = {eur:.2f} EUR")
        
    elif choice == '3':
        usd = float(input("Введите сумму в долларах: "))
        rub = convert_currency(usd, rates, 'to_rub')
        print(f"{usd:.2f} USD = {rub:.2f} руб.")
        
    elif choice == '4':
        eur = float(input("Введите сумму в евро: "))
        rub = convert_currency(eur, rates, 'to_rub')
        print(f"{eur:.2f} EUR = {rub:.2f} руб.")
        
    elif choice == '5':
        print("\n--- ТЕКУЩИЕ КУРСЫ ---")
        # Цикл for для вывода курсов
        for currency, rate in rates.items():
            if currency == 'usd':
                print(f"Доллар (USD): {rate} руб.")
            elif currency == 'eur':
                print(f"Евро (EUR): {rate} руб.")
                
    else:
        print("Неверный выбор. Пожалуйста, выберите 0-5.")
    
    # Дополнительный цикл for — показывает доступные валюты
    if choice in ['1', '2', '3', '4']:
        print("\nДоступные валюты для конвертации:")
        available = ["USD", "EUR", "RUB"]
        for i, curr in enumerate(available, 1):
            print(f"  {i}. {curr}")

print("\n" + "="*50)