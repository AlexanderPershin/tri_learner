from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
from math import *

from unit_dot import UnitDot


class Tri_learner:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x500+100+100')
        self.radius = 150
        self.dots_rads = [0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6,
                          pi, 7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2, 5*pi/3, 7*pi/4, 11*pi/6]
        self.active_dot = None
        self.create_gui()
        self.root.bind('<Configure>', self.update_canvas)
        self.root.mainloop()

    def create_gui(self):
        self.cnv = Canvas(self.root)
        self.cnv.configure(background='light cyan')
        self.line_width = 3
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.cnv.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=NSEW)
        self.create_units()
        self.draw_dots()
        self.create_info()

    def create_info(self):
        self.sidebar = Frame(self.root)
        self.sidebar.grid_columnconfigure(0, weight=1)
        self.sidebar.grid_columnconfigure(1, weight=1)
        fn = font.Font(size=22, weight='normal')
        Label(self.sidebar, font=fn, text='x = ', anchor='e').grid(
            sticky=NSEW, column=0, row=0)

        self.x_value = StringVar()
        self.x_value.set('0')
        Label(self.sidebar, font=fn, textvariable=self.x_value, anchor='w').grid(
            sticky=NSEW, column=1, row=0)

        Label(self.sidebar, font=fn, text='sin(x) = ', anchor='e').grid(
            sticky=NSEW, column=0, row=1)
        self.sin_value = Label(self.sidebar, font=fn, text='0', anchor='w').grid(
            sticky=NSEW, column=1, row=1)
        Label(self.sidebar, font=fn, text='cos(x) = ', anchor='e').grid(
            sticky=NSEW, column=0, row=2)
        self.cos_value = Label(self.sidebar, font=fn, text='1', anchor='w').grid(
            sticky=NSEW, column=1, row=2)
        Label(self.sidebar, font=fn, text='tg(x) = ', anchor='e').grid(
            sticky=NSEW, column=0, row=3)
        self.tg_value = Label(self.sidebar, font=fn, text='0', anchor='w').grid(
            sticky=NSEW, column=1, row=3)
        Label(self.sidebar, font=fn, text='ctg(x) = ', anchor='e').grid(
            sticky=NSEW, column=0, row=4)
        self.ctg_value = Label(self.sidebar, font=fn, text='-', anchor='w').grid(
            sticky=NSEW, column=1, row=4)
        self.sidebar.grid(column=3, row=0, columnspan=1,
                          rowspan=3, sticky=NSEW)

    def create_units(self):
        x1 = self.center_coord['x'] - self.radius
        x2 = self.center_coord['x'] + self.radius
        y1 = self.center_coord['y'] - self.radius
        y2 = self.center_coord['y'] + self.radius
        self.units = self.cnv.create_oval(
            x1, y1, x2, y2, fill=None, outline='DarkOrchid4', width=self.line_width)
        self.x_axis = self.cnv.create_line(
            0, self.center_coord['y'], self.max_coord['x'], self.center_coord['y'], width=self.line_width, fill='OrangeRed2')
        self.y_axis = self.cnv.create_line(
            self.center_coord['x'], 0, self.center_coord['x'], self.max_coord['y'], width=self.line_width, fill='OrangeRed2')

        self.y_axis_label = self.cnv.create_text(
            self.center_coord['x'] + 20, 20, text='Y', font="Times 20 italic bold")
        self.x_axis_label = self.cnv.create_text(
            self.max_coord['x'] - 50, self.center_coord['y'] - 20, text='X', font="Times 20 italic bold")

    def draw_dots(self):
        self.dots = []
        dots_li = [0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6,
                   pi, 7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2, 5*pi/3, 7*pi/4, 11*pi/6]
        dots_repr = ['0', 'π/6', 'π/4', 'π/3',
                     'π/2', '2π/3', '3π/4', '5π/6', 'π', '7π/6', '5π/4', '4π/3', '3π/2', '5π/3', '7π/4', '11π/6', '0']
        actual_rads = dots_li[:]
        actual_rads.reverse()
        actual_rads.insert(0, 0)
        dots_repr.reverse()
        for num, rad_val in enumerate(dots_li):
            new_dot = UnitDot(self.cnv, rad_val, 7, self.radius,
                              self.center_coord['x'], self.center_coord['y'], actual_rads[num], color='tomato', label=dots_repr[num])
            self.dots.append(new_dot)
            self.cnv.tag_bind(new_dot.own_id, '<Button-1>',
                              lambda event, new_dot=new_dot: self.on_dot_clicked(new_dot))

    def on_dot_clicked(self, dot):
        for i in self.dots:
            i.set_unselected()
        dot.set_selected()
        self.active_dot = dot
        self.x_value.set(self.active_dot.label)

    def draw_circle(self, x, y, r=3):
        x1 = x - r
        x2 = x + r
        y1 = y - r
        y2 = y + r
        self.cnv.create_oval(x1, y1, x2, y2, fill='red')

    @ property
    def center_coord(self):
        self.root.update_idletasks()
        x = self.cnv.winfo_width() / 2
        y = self.cnv.winfo_height() / 2
        return {'x': x, 'y': y}

    @ property
    def max_coord(self):
        self.root.update_idletasks()
        x = self.cnv.winfo_width()
        y = self.cnv.winfo_height()
        return {'x': x, 'y': y}
        return dots_li

    def update_canvas(self, event):
        self.radius = min(self.max_coord['x'], self.max_coord['y']) / 4

        # update units circle
        x1 = self.center_coord['x'] - self.radius
        x2 = self.center_coord['x'] + self.radius
        y1 = self.center_coord['y'] - self.radius
        y2 = self.center_coord['y'] + self.radius
        self.cnv.coords(self.units, x1, y1, x2, y2)

        # update x and y axises
        self.cnv.coords(self.x_axis,
                        0, self.center_coord['y'], self.max_coord['x'], self.center_coord['y'])
        self.cnv.coords(self.y_axis,
                        self.center_coord['x'], 0, self.center_coord['x'], self.max_coord['y'])

        # update x and y labels
        self.cnv.coords(self.y_axis_label,
                        self.center_coord['x'] + 20, 20)
        self.cnv.coords(self.x_axis_label,
                        self.max_coord['x'] - 50, self.center_coord['y'] - 20)

        # update dots
        for dot in self.dots:
            dot.update_coord(
                self.radius, self.center_coord['x'], self.center_coord['y'])


if __name__ == "__main__":
    Tri_learner()
