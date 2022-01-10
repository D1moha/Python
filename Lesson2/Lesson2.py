#0 - создаём список
list0 = [1, 3, 3, 4] #ключ 3
list1 = [2, 1, 3, 5] #ключ 1
list2 = [4, 0, 1, 7] #ключ 0
list3 = [5, 2, 1, 0] #ключ 2
list4 = [0, 4, 8, 3] #ключ 4
listOriginal = [list0, list1, list2, list3, list4]
print ("Исходный список:", listOriginal)
print ("- - -")

#1 - сортируем список по возрастанию
listSortByAscending = sorted(listOriginal, key = lambda x: x[1])
print ("1. Список по возрастанию:", listSortByAscending)
print ("- - -")

#2 - создаём словарь
dicNew = dict(zip([x.pop(1) for x in listSortByAscending], [x for x in listSortByAscending]))
print ("2. Словарь:", dicNew)
print ("- - -")
    
#3 - сортируем значения в словаре по убыванию
dicValues = list(dicNew.values())
for x in dicValues:
    x.sort(reverse = True)
dicSortValuesByDescending = dict(zip(dicNew.keys(),dicValues))
print ("3. Словарь со значениями по убыванию:", dicSortValuesByDescending)
print ("- - -")

#4 - получаем множество из всех значений словаря
setDicValues = dicSortValuesByDescending.values()
setNew = set([item for sublist in setDicValues for item in sublist])
print("4. Множество из значений словаря:", setNew)
print ("- - -")

#5 - преобразуем множество в строку
strNew = ''.join(map(str,setNew))
print ("5. Строка:", strNew)
