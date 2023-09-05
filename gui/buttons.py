from tkinter import Button
from logic.helper_functions import make_no_round_brackets
from logic.helper_functions import make_no_square_brackets
from logic.helper_functions import make_no_curly_brackets
from logic.helper_functions import make_no_brackets

def create_button(holder, description, on_click_function, row_pos, column_pos):
    button = Button(holder, text=description, command=on_click_function)
    button.grid(row=row_pos, column=column_pos)
    return button
class TextProcessorButtons:
    def __init__(self, holder, commanded_obj, status_indication):
        self.__buttons = []
        self.__buttons.append(create_button(
            holder=holder,
            description="Remove '()'",
            on_click_function=lambda: commanded_obj.handle_strategy(make_no_round_brackets, status_indication),
            row_pos=2,
            column_pos=2))
        self.__buttons.append(create_button(
            holder=holder,
            description="Remove '[]'",
            on_click_function=lambda: commanded_obj.handle_strategy(make_no_square_brackets, status_indication),
            row_pos=3,
            column_pos=2))
        self.__buttons.append(create_button(
            holder=holder,
            description="Remove '{}'",
            on_click_function=lambda: commanded_obj.handle_strategy(make_no_curly_brackets, status_indication),
            row_pos=4,
            column_pos=2))
        self.__buttons.append(create_button(
            holder=holder,
            description="Remove all brackets",
            on_click_function=lambda: commanded_obj.handle_strategy(make_no_brackets, status_indication),
            row_pos=5,
            column_pos=2))