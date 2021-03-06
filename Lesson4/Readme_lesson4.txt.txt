Задание:
Разработать класс Shape для математического описания плоских фигур:
круга, квадрата и равностороннего треугольника. 
Каждая из геометрических фигур должна представляться своим классом (Circle, Square, Triangle), который наследуется от Shape.

Конструктор класса (Circle, Square, Triangle) должен принимать два значения: геометрический центр плоской фигуры и радиус (сторона фигуры).

Геометрический центр должен быть атрибутом класса Shape (по умолчанию – начало координат 0; 0), а радиус (сторона) – атрибуты дочерних классов (по умолчанию 1).
В дочерних классах предусмотреть наличие следующих методов:
– get_center() – возвращает геометрический центр фигуры;
– get_vertex() – возвращает вершины фигуры (для квадрата и треугольника);
– get_area() – возвращает площадь фигуры;
– move(x, y) – перемещает геометрический центр фигуры в точку (x, y).
В базовом классе предусмотреть метод get_distance(figure_1, figure_2), вычисляющий расстояние между фигурами figure_1 и figure_2 (геометрическими центрами).

Положение фигуры рассматривать в декартовой системе координат (см. рисунок), поворот фигур относительно геометрического центра не принимать во внимание (см. рисунок).

Произвести демонстрацию всех возможностей классов на примерах.


Для запуска программы нужно запустить на выполнение файл Lesson4.py
Программа состоит из классов:
1. Shape() - базовый класс, определяется геометрический центр и метод get_distance для определения расстояния между центрами двух фигур
2. Circle() - класс для круга, состоит из методов:
- get_center - получается геометрический центр из базового класса
- get_area - высчитывает площадь круга
- move - перемещает геометрический центр круга
3. Square() - класс для квадрата
- get_center - получается геометрический центр из базового класса
- get_vertex - определяет вершины квадрата
- get_area - высчитывает площадь квадрата
- move - перемещает геометрический центр квадрата
4. Triangle() - класс для равностороннего треугольника
- get_center - получается геометрический центр из базового класса
- get_vertex - определяет вершины треугольника
- get_area - высчитывает площадь треугольника
- move - перемещает геометрический центр треугольника