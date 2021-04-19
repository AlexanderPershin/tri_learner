from tkinter import *


class Tri_learner:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x500+100+100')
        self.create_gui()
        self.root.bind('<Configure>', self.update_canvas)
        self.cnt = 0
        self.root.mainloop()

    def create_gui(self):
        self.cnv = Canvas(self.root)
        self.cnv.configure(background='white')
        self.line_width = 3
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.cnv.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=NSEW)
        self.create_units()
        self.create_btns()

    def create_btns(self):
        self.sidebar = Frame(self.root)
        Label(self.sidebar, text='sin(x)').grid()
        Label(self.sidebar, text='cos(x)').grid()
        Label(self.sidebar, text='tg(x)').grid()
        Label(self.sidebar, text='ctg(x)').grid()
        self.sidebar.grid(column=3, row=0, columnspan=1,
                          rowspan=3, sticky=NSEW)

    def create_units(self):
        radius = 150
        x1 = self.center_coord['x'] - radius
        x2 = self.center_coord['x'] + radius
        y1 = self.center_coord['y'] - radius
        y2 = self.center_coord['y'] + radius
        print(self.center_coord)
        self.units = self.cnv.create_oval(
            x1, y1, x2, y2, fill=None, width=self.line_width)
        self.x_axis = self.cnv.create_line(
            0, self.center_coord['y'], self.max_coord['x'], self.center_coord['y'], width=self.line_width)
        self.y_axis = self.cnv.create_line(
            self.center_coord['x'], 0, self.center_coord['x'], self.max_coord['y'], width=self.line_width)

    @property
    def center_coord(self):
        self.root.update_idletasks()
        x = self.cnv.winfo_width() / 2
        y = self.cnv.winfo_height() / 2
        return {'x': x, 'y': y}

    @property
    def max_coord(self):
        self.root.update_idletasks()
        x = self.cnv.winfo_width()
        y = self.cnv.winfo_height()
        return {'x': x, 'y': y}

    def update_canvas(self, event):
        self.cnt += 1
        print(f'update {self.cnt}')

        radius = 150
        x1 = self.center_coord['x'] - radius
        x2 = self.center_coord['x'] + radius
        y1 = self.center_coord['y'] - radius
        y2 = self.center_coord['y'] + radius
        self.cnv.coords(self.units, x1, y1, x2, y2)

        self.cnv.coords(self.x_axis,
                        0, self.center_coord['y'], self.max_coord['x'], self.center_coord['y'])
        self.cnv.coords(self.y_axis,
                        self.center_coord['x'], 0, self.center_coord['x'], self.max_coord['y'])


if __name__ == "__main__":
    Tri_learner()
