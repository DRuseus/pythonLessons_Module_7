class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def __find_name(self, name, *lines):
        _flag = False
        for line in lines:
            point = line.find(',')
            if name == line[:point].lower():
                _flag = True
        return _flag

    def add(self, *add_products):
        file = open(self.__file_name, 'a+')
        for prod in add_products:
            file.seek(0)
            lines_list = file.readlines()
            if self.__find_name(prod.name.lower(), *lines_list):
                print(f'Продукт {prod.name} уже есть в магазине')
            else:
                file.write(prod.__str__() + '\n')
        file.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    p4 = Product('nePotato', 55.9, 'Vegetables')
    p5 = Product('GREEN Potato', 15.4, 'Vegetables')
    p6 = Product('Red Potato', 25.2, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3, p4, p5, p6)

    print(s1.get_products())
