from lab_python_oop.Figure import Figure
from lab_python_oop.Color import Color

class Rectangle(Figure):


    def __init__(self, _color, _widht, _height):

        self.widht = _widht
        self.height = _height
        self.color = Color()
        self.color.color_figure = _color


    figur_name = "прямоугольник"

    def square(self):
        return self.height * self.widht

    def __repr__(self):
        return '{} {} цвета шириной {} длиной {} и площадью {}'.format(
            self.figur_name,
            self.color.color_figure,
            self.widht,
            self.height,
            self.square()
        )