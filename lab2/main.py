from faker import Faker
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Сircle import Сircle
from lab_python_oop.Square import Quadrate

def main():

    rect = Rectangle("синего", 1, 1)
    curc = Сircle("зеленого", 1)
    square = Square("красного", 1)
    print(rect)
    print(curc)
    print(square)

    fake = Faker()
    print(fake.sentence())


if __name__ == "__main__":
    main()
