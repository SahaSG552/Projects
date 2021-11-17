figure = ["ножницы", "бумага", "камень", "ящерица", "Спок"]
name = ("Тимур", "Руслан")
# t_figure, r_figure = input(), input()
t_figure, r_figure = "камень", "бумага"
# сдвигаем список так, чтобы то, что показывает Тимур было первым в списке
# из этого списка выбираем 2 элемента от 1 индекса с шагом 2 - Тимур побеждает, если Руслан показывает что то из этих 2х элементов
win = [(figure[figure.index(t_figure):]+figure[:figure.index(t_figure)])[i] for i in range(1, len(figure), 2)]

if t_figure == r_figure:
    print("ничья")
else:
    print(name[r_figure not in win])