class Color:

    def __init__(self):
        self.color = None

    @property
    def color_figure(self):
        return self.color

    @color_figure.setter
    def color_figure(self, _color):
        self.color = _color