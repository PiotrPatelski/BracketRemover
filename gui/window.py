from tkinter import Tk
class Window:
    def __init__(self, title, rows, columns):
        self.impl = Tk()
        self.impl.title(title)
        self.__make_grid_responsive(rows=rows, columns=columns)
    def __make_grid_responsive(self, rows, columns):
        for row in range(rows):
            self.impl.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            self.impl.grid_columnconfigure(column, weight=1)
    def run(self):
        self.impl.mainloop()