import constants as preset
from frontend.sceneManager import SceneManager
from backend.modelManager import ModelManager
from tkinter import Tk

"""
sources:
https://tkdocs.com/tutorial/index.html
https://tkdocs.com/widgets/
https://www.pythontutorial.net/tkinter/tkinter-grid/
"""


class SpyOT(Tk):
    def __init__(self, title=preset.title):
        super().__init__()
        self.title(title)
        self.backend = ModelManager()
        self.frontend = SceneManager(self)


def main():
    demo = SpyOT("SpyOT Demo")
    demo.mainloop()


if __name__ == '__main__':
    main()
