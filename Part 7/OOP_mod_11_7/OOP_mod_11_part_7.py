class DiscountCalculator:
    def __init__(self, discount):
        self.discount = discount /100

    def __call__(self, price):
        new_price = price - (price * self._discount)
        # new_price = price * (1 - self._discount)
        return new_discount

#calculator = DiscountCalculator(20)
#print(calculator(50))
#print(calculator(100))
#print(calculator(360))

#calculator2 = DiscountCalculator(20)
#print(calculator(70))
#print(calculator(200))
#print(calculator(450))

obj.set_radius(20)
obj.radius = 20
class ImageResizer:
    def __init__(self, width, height, max_width, max_height):
        self._width = width
        self.max_width = width
        self._height = height
        self._max_hight = max_height
    @propetry
    def width(self):
        return self._width
    @width.getter
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if  value <=self._max_width:
            self._width = value
        else:
            raise ValueError("bab value")

    @propetry
    def height(self):
        print("propetry from width")
        return self._height

    @height.getter
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        print("height.setter")

        if value <= self._max_height:
            self._height = value
        else:
            raise ValueError("bab value")
    @height.deleter
    def height(self):
        print("hello from deleter")


resizer =  ImageResizer(0, 0, 1200, 1600)

resizer.width = 10
print(resizer.width)
resizer.height = 10
def resizer.height
def resizer.width


