from random import choices


def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Введите целочисленное значение")


# birthdays_range = 20
people = [_ for _ in range(1, 366)]
birthdays_range = get_int("Введите количество людей: ")
iterations = get_int("Количество итераций: ")
counter = 0  # считаем совпадения
for i in range(iterations):
    birthdays = choices(people, k=birthdays_range)
    counter += len(set(birthdays)) == birthdays_range

print(
    f"Вероятность, что из {birthdays_range} людей "
    f"у кого-то совпадёт день рождения: "
    f"{round(((iterations-counter)*100)/iterations, 5)}%"
)
