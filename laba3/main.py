# --- ФУНКЦІЇ ТА ПРОЦЕДУРИ ДЛЯ ЗАВДАННЯ 1 ---

def is_symmetric(row):
    """Функція для розпізнавання симетричної послідовності."""
    return row == row[::-1]


def build_vector_b(matrix, vector_b):
    """Процедура побудови вектора B із номерів симетричних рядків (нумерація з 1)."""
    vector_b.clear()
    for i in range(len(matrix)):
        if is_symmetric(matrix[i]):
            vector_b.append(i + 1)


def print_vector_7_per_line(vector_b):
    """Процедура виведення вектора по сім елементів у рядку."""
    if not vector_b:
        print("Симетричних рядків у матриці не знайдено.")
        return
    for i in range(len(vector_b)):
        print(f"{vector_b[i]:4d}", end=" ")
        if (i + 1) % 7 == 0:
            print()
    if len(vector_b) % 7 != 0:
        print()


def task_1():
    print("\n--- Завдання 1: Пошук симетричних рядків матриці ---")
    while True:
        try:
            n = int(input("Введіть розмірність квадратної матриці n (1 <= n <= 15): "))
            if 1 <= n <= 15:
                break
            print("Помилка: n має бути від 1 до 15.")
        except ValueError:
            print("Помилка: введіть ціле число.")

    print(f"Введіть елементи матриці {n}x{n} по рядках (цілі числа через пробіл):")
    matrix_a = []
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Рядок {i + 1}: ").split()))
                if len(row) == n:
                    matrix_a.append(row)
                    break
                print(f"Помилка: потрібно ввести рівно {n} чисел.")
            except ValueError:
                print("Помилка: вводьте лише цілі числа через пробіл.")

    vector_b = []
    build_vector_b(matrix_a, vector_b)

    print("\nРезультат — вектор B (номери симетричних рядків):")
    print_vector_7_per_line(vector_b)


# --- ФУНКЦІЯ ДЛЯ ЗАВДАННЯ 2 ---

def task_2():
    print("\n--- Завдання 2: Держава з мінімальною щільністю населення ---")
    
    # Готовий список із 15 держав: (Назва, Населення [млн], Площа [тис. кв. км])
    countries = [
        ("Україна", 41.0, 603.5),
        ("Польща", 38.0, 312.7),
        ("Німеччина", 83.2, 357.6),
        ("Франція", 67.8, 551.7),
        ("Іспанія", 47.4, 505.9),
        ("Італія", 59.1, 301.3),
        ("Канада", 38.2, 9984.7),
        ("Австралія", 25.7, 7692.0),
        ("Монголія", 3.3, 1564.1),
        ("Норвегія", 5.4, 385.2),
        ("Фінляндія", 5.5, 338.4),
        ("Швеція", 10.4, 450.3),
        ("Бразилія", 214.0, 8515.8),
        ("Аргентина", 45.8, 2780.4),
        ("Казахстан", 19.0, 2724.9),
    ]

    print("Заданий список 15 держав:")
    for i, (name, pop, area) in enumerate(countries, start=1):
        print(f"{i:2d}. {name:<12} | Населення: {pop:>5.1f} млн | Площа: {area:>7.1f} тис. км²")

    min_density = float("inf")
    min_country = ""

    for name, population, area in countries:
        density = population / area
        if density < min_density:
            min_density = density
            min_country = name

    print(f"\nРезультат:")
    print(f"Держава з мінімальною щільністю населення: {min_country}")
    print(f"Щільність: {min_density * 1000:.2f} осіб/км² ({min_density:.4f} тис. осіб/км²)")


# --- ФУНКЦІЯ ДЛЯ ЗАВДАННЯ 3 ---

def task_3():
    print("\n--- Завдання 3: Підрахунок попередніх входжень слів ---")
    print("Вводьте текст по рядках. Щоб завершити введення, залиште рядок порожнім і натисніть Enter:")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    words = text.split()

    if not words:
        print("Текст порожній.")
        return

    word_counts = {}
    result = []

    for word in words:
        count = word_counts.get(word, 0)
        result.append(str(count))
        word_counts[word] = count + 1

    print("\nРезультат (кількість попередніх появ кожного слова):")
    print(" ".join(result))


# --- ГОЛОВНЕ МЕНЮ ---

def main():
    while True:
        print("\n" + "=" * 50)
        print("ЛАБОРАТОРНА РОБОТА №3 (ВАРІАНТ 3)")
        print("1. Завдання 1 — Симетричні рядки матриці")
        print("2. Завдання 2 — Мінімальна щільність населення (15 держав)")
        print("3. Завдання 3 — Підрахунок входжень слів у тексті")
        print("0. Вихід")
        print("=" * 50)

        choice = input("Оберіть пункт меню (0-3): ").strip()

        if choice == "1":
            task_1()
        elif choice == "2":
            task_2()
        elif choice == "3":
            task_3()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір! Введіть 1, 2, 3 або 0.")


if __name__ == "__main__":
    main()