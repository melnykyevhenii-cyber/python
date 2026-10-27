import math

# Завдання 1: Сума ряду з точністю епсилон (варіант 5)
def task_1():
    print("\n--- Завдання 1 ---")
    try:
        x = float(input("Введіть дійсне число x (не рівне 0): "))
        a = float(input("Введіть дійсне число a (не рівне 0): "))
        eps = float(input("Введіть точність eps (> 0): "))
        
        if x == 0 or a == 0 or eps <= 0:
            print("Помилка: x та a не повинні дорівнювати 0, а eps має бути більше 0.")
            return

        def get_term(k, x, a):
            try:
                # Обчислюємо чисельник
                numerator = math.cos(math.pow(a, k) + math.pow(x, k))
                # Обчислюємо знаменник
                denom_int = math.factorial(k**2)
                # Якщо знаменник занадто великий для float або чисельник дуже малий
                return numerator / float(denom_int)
            except (OverflowError, ValueError):
                # Якщо k^2 дуже велике (наприклад, factorial(16) і більше), 
                # значення чисельника / (k^2)! прямує до 0.
                return 0.0

        N = 1  # Починаємо з N = 1
        while True:
            # Сума N членів (від k=0 до N)
            sum_N = sum(get_term(k, x, a) for k in range(N + 1))
            # Сума 2N членів (від k=0 до 2N)
            sum_2N = sum(get_term(k, x, a) for k in range(2 * N + 1))
            
            # Перевіряємо умову зупинки: |S_{2N} - S_N| < eps
            if abs(sum_2N - sum_N) < eps:
                print(f"Результат суми: {sum_2N:.8f}")
                print(f"Врахована кількість доданців (2N + 1): {2 * N + 1}")
                break
            
            N *= 2
            if N > 1024:  # Безпечне обмеження
                print(f"Результат суми (досягнуто межі): {sum_2N:.8f}")
                print(f"Врахована кількість доданців: {2 * N + 1}")
                break

    except ValueError:
        print("Будь ласка, вводьте коректні числові значення.")

# Завдання 2: Послідовність an (варіант 5)
def task_2():
    print("\n--- Завдання 2 ---")
    try:
        x = float(input("Введіть дійсне число x: "))
        eps = float(input("Введіть точність eps (> 0): "))
        
        if eps <= 0:
            print("Точність має бути більше 0.")
            return

        def get_an(n, x):
            try:
                num = (x**(2*n)) * math.sin(x**n)
                den = float(math.factorial(n**2))
                return num / den
            except OverflowError:
                return 0.0

        prev_a = get_an(1, x)
        found = False
        
        for n in range(2, 101):  # обмежено першими 10^2 членами
            curr_a = get_an(n, x)
            if abs(curr_a - prev_a) < eps:
                print(f"Знайдено елемент: a_{n} = {curr_a}")
                print(f"Його номер n = {n}")
                print(f"Попередній елемент: a_{n-1} = {prev_a}")
                print(f"Різниця: {abs(curr_a - prev_a)}")
                found = True
                break
            prev_a = curr_a
            
        if not found:
            print("В заданому діапазоні (перші 100 членів) умова не виконалась.")
    except ValueError:
        print("Будь ласка, вводьте числові значення.")

# Завдання 3: Робота з текстом (варіант 5)
def task_3():
    print("\n--- Завдання 3 ---")
    text = input("Введіть текст: ")
    
    import re
    tokens = re.findall(r'\b\w+\b|[^\w\s]|\s+', text)
    
    result = []
    for token in tokens:
        if token.isalpha():
            length = len(token)
            if length % 2 != 0:  # непарна довжина
                mid = length // 2
                new_word = token[:mid] + token[mid+1:]
                result.append(new_word)
            else:
                result.append(token)
        else:
            result.append(token)
            
    processed_text = "".join(result)
    print("Оброблений текст:")
    print(processed_text)

# Завдання 4: Рекурсивна функція перевірки степеня (варіант 5)
def is_power(n, p):
    if n == 1:
        return True
    if n < p or p <= 1:
        return False
    if n % p != 0:
        return False
    return is_power(n // p, p)

def task_4():
    print("\n--- Завдання 4 ---")
    try:
        n = int(input("Введіть ціле число n: "))
        p = int(input("Введіть основу степеня p (p > 1): "))
        
        if p <= 1:
            print("Число p має бути більше 1.")
            return
            
        if n <= 0:
            print("Число n має бути додатним.")
            return

        result = is_power(n, p)
        if result:
            print(f"Так, число {n} є степенем числа {p}.")
        else:
            print(f"Ні, число {n} НЕ є степенем числа {p}.")
    except ValueError:
        print("Будь ласка, вводьте цілі числа.")

# Головне меню програми
def main():
    while True:
        print("\n==============================")
        print("   МЕНЮ ЛАБОРАТОРНОЇ РОБОТИ №2")
        print("==============================")
        print("1. Завдання 1 (Сума ряду)")
        print("2. Завдання 2 (Послідовність an)")
        print("3. Завдання 3 (Обробка тексту)")
        print("4. Завдання 4 (Рекурсія - степінь числа)")
        print("0. Вихід з програми")
        print("==============================")
        
        choice = input("Оберіть номер завдання (0-4): ")
        
        if choice == '1':
            task_1()
        elif choice == '2':
            task_2()
        elif choice == '3':
            task_3()
        elif choice == '4':
            task_4()
        elif choice == '0':
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Невірний вибір! Будь ласка, введіть число від 0 до 4.")

if __name__ == "__main__":
    main()