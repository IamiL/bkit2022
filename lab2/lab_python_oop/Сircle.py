from lab_python_oop.Figure import Figure
from lab_python_oop.Color import Color
import math

class Сircle(Figure):

    figure_name = "круг"

    def __init__(self,_color , _radius ):

        self.radius = _radius
        self.color = Color()
        self.color.color_figure = _color

    def square(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} и площадью {}'.format(
            self.figure_name,
            self.color.color_figure,
            self.radius,
            self.square()
        )