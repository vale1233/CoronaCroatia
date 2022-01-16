import frontend, backend
from tkinter import *


def main():
    texttwo = backend.updated_date(self='info')
    root = Tk()
    root.wm_title(f"Covid-19: Croatia (last update: {texttwo[0:10]})")
    root.geometry("400x270")

    app = frontend.Window(root)
    frontend.center_tkinter(root)

    root.mainloop()


if __name__ == '__main__':
    main()