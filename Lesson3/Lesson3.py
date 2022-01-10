import csv
import json

def f_gen(): #создаём генератор от 5 до 90 
    for n in range(5, 91):
        yield n

def funс_1(): #создаём функцию_1 для вычисления значений при изменении x в диапазоне генератора
    res = []
    for x in f_gen():
        fx1 = x / (x + 100)
        res.append(fx1)
    return res

def funс_2(): #создаём функцию_2 для вычисления значений при изменении x в диапазоне генератора
    res = []
    for x in f_gen():
        fx2 = 1 / x
        res.append(fx2)
    return res

def funс_3(): #создаём функцию_3, которая вычисляется на основании функции_1 и функции_2
    fx1 = funс_1()
    fx2 = funс_2()
    i = 0
    my_dict = dict() #создаём словарь 
    for x in f_gen(): #записываем в словарь аргументы и значения функций
        fx3 = 20 * (fx1[i] + fx2[i]) / x
        my_dict[x] = [fx1[i], fx2[i], fx3]
        i += 1
    return my_dict

def func_write_csv(): #сохраняем результаты вычислений в csv-файл
    with open('Lesson3.csv', 'w', newline='') as my_file:
        my_csv_writer = csv.writer(my_file, delimiter=',')
        my_csv_writer.writerow(["x", "Fx1", "Fx2", "Fx3"]) #заголовок в виде x, f1(x), f2(x), f3(x)
        res = funс_3()
        for key in res:
            x = key
            Fx1 = res[key][0]
            Fx2 = res[key][1]
            Fx3 = res[key][2]
            my_csv_writer.writerow([x, Fx1, Fx2, Fx3])
func_write_csv()

def func_read_csv(): #читаем csv-файл и возвращаем результаты в виде списка
    with open('Lesson3.csv', newline='') as f:
        reader = csv.reader(f)
        my_list = list(reader)
    del my_list[0]
    return my_list

def func_json(): #сохраняем список в json-файл
    my_list = func_read_csv()
    with open('data.json', 'w') as f:
        json.dump(my_list, f)
func_json()