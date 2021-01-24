"""
    比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    创建子类【猫】，继承【动物类】，
    重写父类的__init__方法，继承父类的属性，
    添加一个新的属性，毛发 = 短毛，
    添加一个新的方法， 会捉老鼠，
    重写父类的【会叫】的方法，改成【喵喵叫】
"""
__author__ = 'cheche'


class _Animal(object):

    def __init__(self, name, color, age, sex):
        self._name = name
        self._color = color
        self._age = age
        self._sex = sex

    @staticmethod
    def howl():
        raise Exception('需要重写叫声！')

    @staticmethod
    def animal_run():
        print('高速向您奔来...')


class Cat(_Animal):

    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self._fur = 'short'

    @property
    def fur(self):
        return self._fur

    @fur.setter
    def fur(self, newfur):
        self._fur = newfur

    @staticmethod
    def howl():
        print('喵喵喵 -<>- ')

    @staticmethod
    def catch_mouse():
        print('杰瑞！别跑！')


if __name__ == "__main__":
    cat = Cat('Tom', 'gray', '6', 'male')
    print(cat.fur)
    cat.fur = 'long'
    print(cat.fur)






