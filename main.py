import math

def task_1():
    print("\n--- Завдання 1: Обчислення функції z(a) ---")
    try:
        a = float(input("Введіть значення аргумента a: "))
        # z(a) = 1/4 - 1/4 * sin(5/2 * pi - 8a)
        z = 0.25 - 0.25 * math.sin((5 / 2) * math.pi - 8 * a)
        print(f"Результат: z({a}) = {z}")
    except ValueError:
        print("Помилка: введіть числове значення!")

def task_2():
    print("\n--- Завдання 2: Сума чисел від 1 до n, кратних k ---")
    try:
        n = int(input("Введіть число n (більше за 2): "))
        k = int(input("Введіть число k (1 < k < n): "))
        
        if k <= 1 or k >= n:
            print("Помилка: умова 1 < k < n не виконується!")
            return
            
        total_sum = 0
        multiples = []
        for i in range(1, n + 1):
            if i % k == 0:
                total_sum += i
                multiples.append(i)
                
        print(f"Числа від 1 до {n}, кратні {k}: {multiples}")
        print(f"Сума таких чисел: {total_sum}")
    except ValueError:
        print("Помилка: введіть цілі числа!")

def task_3():
    print("\n--- Завдання 3: Робота з одновимірним масивом дійсних чисел ---")
    try:
        input_str = input("Введіть елементи масиву через пробіл (наприклад: 3.5 -2.1 4 -5.0 1.2): ")
        arr = [float(x) for x in input_str.split()]
        
        if not arr:
            print("Масив порожній!")
            return
            
        # 1. Максимальний елемент
        max_elem = max(arr)
        
        # 2. Середнє арифметичне від'ємних елементів
        negative_elems = [x for x in arr if x < 0]
        if negative_elems:
            avg_neg = sum(negative_elems) / len(negative_elems)
        else:
            avg_neg = "Від'ємних елементів немає"
            
        # 3. Вивести додатні елементи у зворотному порядку
        positive_elems_reversed = [x for x in arr if x > 0][::-1]
        
        print(f"\nПочатковий масив: {arr}")
        print(f"Максимальний елемент: {max_elem}")
        print(f"Середнє арифметичне від'ємних елементів: {avg_neg}")
        print(f"Додатні елементи у зворотному порядку: {positive_elems_reversed}")
        
    except ValueError:
        print("Помилка: будь ласка, вводьте лише дійсні числа через пробіл!")

def main():
    while True:
        print("\n==============================")
        print(" МЕНЮ ЛАБОРАТОРНОЇ РОБОТИ №1 (ВАРІАНТ 2)")
        print("==============================")
        print("1. Виконати Завдання 1 (Обчислення z(a))")
        print("2. Виконати Завдання 2 (Сума кратних чисел)")
        print("3. Виконати Завдання 3 (Операції з масивом)")
        print("0. Вихід")
        print("==============================")
        
        choice = input("Оберіть номер завдання (0-3): ")
        
        if choice == '1':
            task_1()
        elif choice == '2':
            task_2()
        elif choice == '3':
            task_3()
        elif choice == '0':
            print("Вихід із програми. До побачення!")
            break
        else:
            print("Невірний вибір! Будь ласка, введіть число від 0 до 3.")

if __name__ == "__main__":
    main()