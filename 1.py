def print_dictionary(data):
    """Виводить всі значення словника."""
    if not data:
        print("Словник порожній.")
        return

    for key, value in data.items():
        print(f"{key}: {value}")


def add_entry(data):
    """Додає новий запис до словника."""
    key = input("Введіть ключ (модель авто): ")
    try:
        value = (int(input("Введіть вартість: ")), int(input("Введіть вік: ")))
        data[key] = value
        print(f"Запис '{key}: {value}' додано.")
    except ValueError:
        print("Помилка: Вартість та вік повинні бути цілими числами.")


def remove_entry(data):
    """Видаляє запис зі словника."""
    key = input("Введіть ключ для видалення: ")
    if key in data:
        del data[key]
        print(f"Запис з ключем '{key}' видалено.")
    else:
        print(f"Запис з ключем '{key}' не знайдено.")



def view_sorted(data):
    """Виводить вміст словника за відсортованими ключами."""
    if not data:
        print("Словник порожній.")
        return
    
    sorted_keys = sorted(data.keys())
    for key in sorted_keys:
        print(f"{key}: {data[key]}")



def calculate_average_cost(data):
    """Обчислює середню вартість автомобілів, вік яких перевищує 6 років."""
    total_cost = 0
    count = 0
    for model, (cost, age) in data.items():
        if age > 6:
            total_cost += cost
            count += 1
    if count == 0:
        print("Немає автомобілів, вік яких перевищує 6 років.")
        return None  # Або повернути 0, залежно від бажаної логіки

    return total_cost / count



def main():
    car_data = {
        "audi": (250000, 3),
        "ferrari": (3500000, 7),
        "bmw": (500000, 6),
        "toyota": (600000, 12)
    }

    while True:
        print("\nМеню:")
        print("1. Вивести словник")
        print("2. Додати запис")
        print("3. Видалити запис")
        print("4. Перегляд за відсортованими ключами")
        print("5. Обчислити середню вартість (вік > 6)")
        print("0. Вихід")


        choice = input("Виберіть дію: ")


        if choice == '1':
            print_dictionary(car_data)
        elif choice == '2':
            add_entry(car_data)
        elif choice == '3':
            remove_entry(car_data)
        elif choice == '4':
            view_sorted(car_data)
        elif choice == '5':
            average_cost = calculate_average_cost(car_data)
            if average_cost is not None:
                print(f"Середня вартість автомобілів старше 6 років: {average_cost}")
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()