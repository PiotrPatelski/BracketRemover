from gui.window import Window
from gui.text_processor import TextProcessor
from gui.label_manager import LabelManager
from gui.buttons import TextProcessorButtons

class App:
    def __init__(self):
        self.window = Window(title = "Bracket Remover 1.0", rows = 6, columns = 5)
        self.text_processor = TextProcessor(holder = self.window.impl)
        self.label_manager = LabelManager(holder = self.window.impl)
        self.buttons = TextProcessorButtons(holder = self.window.impl,
                                            commanded_obj = self.text_processor,
                                            status_indication = self.label_manager.display_success_status)
    def run(self):
        self.window.run()