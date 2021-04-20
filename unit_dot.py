from tkinter import *
from math import *


class UnitDot:
    def __init__(self, cnv, rad_val, own_radius, circle_radius, center_x, center_y, color='green', active_color='red'):
        self.cnv = cnv
        self.rad_val = rad_val
        self.own_radius = own_radius
        self.circle_radius = circle_radius
        self.center_x = center_x
        self.center_y = center_y
        self.is_active = False
        self.color = color
        self.active_color = active_color
        self.x = self.circle_radius * cos(self.rad_val) + self.center_x
        self.y = self.circle_radius * sin(self.rad_val) + self.center_y
        self.own_id = self.draw_circle()

    def draw_circle(self):
        x1 = self.x - self.own_radius
        x2 = self.x + self.own_radius
        y1 = self.y - self.own_radius
        y2 = self.y + self.own_radius
        own_id = self.cnv.create_oval(
            x1, y1, x2, y2, fill=self.color, tags='dot')
        return own_id

    def update_coord(self, new_circle_radius, new_center_x, new_center_y):
        # update some vals here
        self.circle_radius = new_circle_radius
        self.center_x = new_center_x
        self.center_y = new_center_y
        new_x = self.circle_radius * cos(self.rad_val) + self.center_x
        new_y = self.circle_radius * sin(self.rad_val) + self.center_y
        x1 = new_x - self.own_radius
        x2 = new_x + self.own_radius
        y1 = new_y - self.own_radius
        y2 = new_y + self.own_radius
        self.cnv.coords(self.own_id, x1, y1, x2, y2)

    def set_selected(self):
        self.is_active = True
        self.cnv.itemconfig(self.own_id, fill=self.active_color)

    def set_unselected(self):
        self.is_active = False
        self.cnv.itemconfig(self.own_id, fill=self.color)
