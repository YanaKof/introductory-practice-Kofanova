# Модуль 3
# МОДУЛЬ 3: Функции
# Выполнено 5 упражнений из методички

# ============================================
# Упражнение 1. calculate_profit()
# ============================================
print("\n--- Упражнение 1. calculate_profit() ---")

def calculate_profit(revenue, costs):
    """Принимает выручку и затраты, возвращает прибыль"""
    return revenue - costs

# Тестирование на трёх парах значений
print(f"Прибыль (10000, 7000): {calculate_profit(10000, 7000)} руб.")
print(f"Прибыль (5000, 6000): {calculate_profit(5000, 6000)} руб.")
print(f"Прибыль (15000, 15000): {calculate_profit(15000, 15000)} руб.")

# ============================================
# Упражнение 2. calculate_vat()
# ============================================
print("\n--- Упражнение 2. calculate_vat() ---")

def calculate_vat(price, vat_rate=20):
    """Принимает цену и ставку НДС (по умолчанию 20%), возвращает сумму налога"""
    return price * vat_rate / 100

print(f"НДС 20% от 1000 руб.: {calculate_vat(1000)} руб.")
print(f"НДС 10% от 1000 руб.: {calculate_vat(1000, 10)} руб.")
print(f"НДС 20% от 5000 руб.: {calculate_vat(5000)} руб.")

# ============================================
# Упражнение 3. get_category()
# ============================================
print("\n--- Упражнение 3. get_category() ---")

def get_category(revenue):
    """Возвращает категорию бизнеса по выручке"""
    if revenue < 1_000_000:
        return "Микробизнес"
    elif revenue < 10_000_000:
        return "Малый бизнес"
    elif revenue < 100_000_000:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"

# Тестирование на 4 значениях
test_revenues = [500000, 5000000, 50000000, 200000000]
for rev in test_revenues:
    print(f"Выручка {rev:,} руб. → {get_category(rev)}")

# ============================================
# Упражнение 4. compound_interest()
# ============================================
print("\n--- Упражнение 4. compound_interest() ---")

def compound_interest(capital, rate, years):
    """Принимает капитал, ставку и срок, возвращает итоговую сумму"""
    return capital * (1 + rate / 100) ** years

print(f"Стартовый капитал: 100000 руб., ставка 10%")
print(f"  Через 3 года: {compound_interest(100000, 10, 3):.2f} руб.")
print(f"  Через 5 лет: {compound_interest(100000, 10, 5):.2f} руб.")
print(f"  Через 10 лет: {compound_interest(100000, 10, 10):.2f} руб.")

# ============================================
# Упражнение 5. apply_discount()
# ============================================
print("\n--- Упражнение 5. apply_discount() ---")

def apply_discount(price, discount_percent):
    """Принимает цену и процент скидки, возвращает новую цену"""
    return price * (100 - discount_percent) / 100

# Применить к списку из 5 товаров в цикле
products = [
    {"name": "Ноутбук", "price": 50000},
    {"name": "Мышь", "price": 1500},
    {"name": "Клавиатура", "price": 3000},
    {"name": "Монитор", "price": 25000},
    {"name": "Наушники", "price": 4500}
]

discount = 15
print(f"Цены со скидкой {discount}%:")
for product in products:
    new_price = apply_discount(product["price"], discount)
    print(f"  {product['name']}: {product['price']} руб. → {new_price:.2f} руб.")