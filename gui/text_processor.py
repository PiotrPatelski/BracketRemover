from tkinter import Text
from tkinter import END

class TextProcessor:
    def __init__(self, holder):
        self.__instantiate_text_boxes(holder)
        self.__assign_boxes_position()
    def __instantiate_text_boxes(self, holder):
        self.__input_box = Text(holder, width=50, height=20)
        self.__output_box = Text(holder, width=50, height=20)
    def __assign_boxes_position(self):
        self.__input_box.grid(row=2, column=1, rowspan=4, sticky="news")
        self.__output_box.grid(row=2, column=3, rowspan=4, sticky="news")
    def __get_input_text(self):
        return self.__input_box.get("1.0", END)
    def __print_with_overwrite(self, result):
        self.__output_box.delete("1.0", END)
        self.__output_box.insert(END, result)
    def handle_strategy(self, filtering_strategy, status_indication):
        self.__print_with_overwrite(filtering_strategy(self.__get_input_text()))
        status_indication()