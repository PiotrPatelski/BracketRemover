from tkinter import Label
class LabelManager:
    def __init__(self, holder):
        self.__instantiate_labels(holder)
        self.__set_labels_position()
    def __instantiate_labels(self, holder):
        self.__title_label = Label(holder, text="App by Piotr Patelski")
        self.__instruction_label = Label(holder, text="Paste string to have its brackets removed:\n")
        self.__progress_label = Label(holder, text="")
    def __set_labels_position(self):
        self.__title_label.grid(row=0, column=2)
        self.__instruction_label.grid(row=1, column=2)
        self.__progress_label.grid(row=6, column=2)
    def display_success_status(self):
        self.__progress_label.config(text="Removal finished succesfully!\n")