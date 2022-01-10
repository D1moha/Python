import math

class Shape(): #задаём базовый класс
    def __init__(self, center = [0, 0]): 
        self.center = center #устанавливаем центр геометрических фигур

    def get_distance(self, figure_1, figure_2): #задаём метод для определения расстояния между центрами двух фигур
        dist = math.sqrt((figure_2[0]-figure_1[0])**2 + (figure_2[1]-figure_1[1])**2) #вычисляем расстояние между центрами двух фигур
        return (dist) 

class Circle(Shape): #задаём класс для круга
    def __init__(self, center, radius = 1):
        super().__init__(center) #получаем геометрический центр фигуры из базового класса
        self.radius = radius

    def get_center(self): #задаём метод для получения геометрического центра фигуры
        return self.center

    def get_area(self, radius): #задаём метод для вычисления площади фигуры
        area = math.pi*(radius**2) #вычисляем площадь круга
        return area
    
    def move(self, coord_circle): #задаём метод для перемещения геометрического центра фигуры
        self.center = coord_circle
        return self.center

res_circle = Circle((0,0)) #демонстрация работы класса
print('Circle')
print('get_center:', res_circle.get_center())
print('get_area:', res_circle.get_area(1))
coord_circle = (int(input('x:')),int(input('y:'))) #задаём новые координаты геометрического центра круга
print('move center:', res_circle.move(coord_circle))

class Square(Shape): #задаём класс для квадрата
    def __init__(self, center, radius = 1):
        super().__init__(center) #получаем геометрический центр фигуры из базового класса
        self.radius = radius

    def get_center(self): #задаём метод для получения геометрического центра фигуры
        return self.center

    def get_vertex(self, radius): #задаём метод для получения координат фигуры
        vertex = [(self.center[0]-radius/2, self.center[1]-radius/2), (self.center[0]+radius/2, self.center[1]-radius/2), (self.center[0]+radius/2,self.center[1]+radius/2), (self.center[0]-radius/2,self.center[1]+radius/2)] #вычисляем координаты квадрата
        return vertex

    def get_area(self,radius): #задаём метод для вычисления площади фигуры
        area = radius**2 #вычисляем площадь квадрата
        return area

    def move(self, coord_square): #задаём метод для перемещения геометрического центра фигуры
        self.center = coord_square
        return self.center

res_square = Square((0,0)) #демонстрация работы класса
print('Square')
print('get_center:', res_square.get_center())
print('get_vertex:', res_square.get_vertex(1))
print('get_area:', res_square.get_area(1))
coord_square = (int(input('x:')),int(input('y:'))) #задаём новые координаты геометрического центра квадрата
print('move center:', res_square.move(coord_square))

class Triangle(Shape): #задаём класс для треугольника 
    def __init__(self, center, radius = 1):
        super().__init__(center) #получаем геометрический центр фигуры из базового класса
        self.radius = radius

    def get_center(self): #задаём метод для получения геометрического центра фигуры
        return self.center

    def get_vertex(self, radius): #задаём метод для получения координат фигуры
        r_max = (radius*math.sqrt(3))/3 #вычисляем расстояние от геометрического центра до вершины
        r_min = r_max/2 #вычисляем расстояние от геометрического центра до стороны трецгольника
        vertex = [(self.center[0],self.center[1]+r_max), (self.center[0]+radius/2,self.center[1]-r_min), (self.center[0]-radius/2,self.center[1]-r_min)] #вычисляем координаты квадрата
        return vertex

    def get_area(self, radius): #задаём метод для вычисления площади фигуры
        p = (radius+radius+radius)/2 
        area = math.sqrt(p*(p-radius)*(p-radius)*(p-radius)) #вычисляем площадь треугольника
        return area

    def move(self, coord_triangle): #задаём метод для перемещения геометрического центра фигуры
        self.center = coord_triangle
        return self.center

res_triangle = Triangle((0,0)) #демонстрация работы класса
print('Triangle')
print('get_center:', res_triangle.get_center())
print('get_vertex:', res_triangle.get_vertex(1))
print('get_area:', res_triangle.get_area(1))
coord_triangle = (int(input('x:')),int(input('y:'))) #задаём новые координаты геометрического центра треугольника
print('move center:', res_triangle.move(coord_triangle))

res_distance = Shape() #демонстрация работы класса
print('Distance:', res_distance.get_distance((1,1),(2,2))) #получаем расстояние между указанными геометрическими центрами двух фигур 