from tkinter import Tk
from models.window import Janela1


def main() -> None:
    root = Tk()
    app = Janela1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
