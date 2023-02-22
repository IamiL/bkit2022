from lab_python_oop.Rectangle import Rectangle

class Quadrate(Rectangle):

    figure_name = "квадрат"

    def __init__(self, _color, _side):
        self.side = _side
        super().__init__(_color, self.side, self.side)


    def __repr__(self):
        return '{} {} цвета со стороной {} и площадью {}'.format(
            Quadrate.figure_name,
            self.color.color_figure,
            self.side,
            self.Square()