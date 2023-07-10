class Graph:
    def __init__(self, data, is_show=True):
        self.data = data.copy()

    def set_data(self, data):
        self._data = data

    def list_to_str(self, d):
        return " ".join(list(map(str, d)))

    def show_table(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            return self.list_to_str(self.data)

    def show_graph(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print(
                f"Графическое отображение данных: {self.list_to_str(self.data)}"
            )

    def show_bar(self):
        print(f"Столбчатая диаграмма: {self.list_to_str(self.data)}")

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
