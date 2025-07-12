"""
YouTube tutorial: https://youtu.be/JlMyYuY1aXU?si=bUOoZt5K9LMQNh8d 11:13 min

1. Минимум, который должен реализовать

class Node:
    def __init__(self, data):
        self.data = data -
        self.next = None - так как нет связанного узла ставим None

class LinkedList:
    def __init__(self):
        self.head = None - означает что список пустой нет первого элемента


Почему 2 класса?

    1. Node — это один элемент связного списка
    Он хранит данные и ссылку на следующий узел. Без него — просто негде хранить информацию.

    2. LinkedList — это весь поезд (вся цепочка узлов)
    Он управляет узлами:
        1. знает, где начало списка (свойство head)
        2. добавляет узлы (append)
        3. удаляет, ищет, выводит список


2. Обязательные методы для начала:
    1. append()	Добавляет элемент в конец списка
    2. length()
    3. display()

    prepend()	Добавляет элемент в начало
    print_list()	Выводит все значения
    delete()	Удаляет элемент по значению
    find()	Проверяет, есть ли значение

"""


# from YouTube
class Node:
    def __init__(self, data=None):
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = Node()  # idk is it possible to put just none

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


"""
explanation: 

1. Часть 1: Node — один элемент списка
class Node:
    def __init__(self, data = None):
        self.data = data

просто запомнить, вопрос: почему у нас два класса        


2. Часть 2: LinkedList — весь список
class LinkedList:
    def __init__(self):
        self.head = Node()


self.head = Node() - создаём пустой первый элемент, который называется "голова списка"
Это как старт — с него начинается цепочка.


3. Метод append — добавление элемента в конец

def append(self, data):
    new_node = Node(data)
    cur = self.head
    while cur.next != None:
        cur = cur.next
    cur.next = new_node

new_node = Node(data) - создаём новый элемент, в который кладём значение data     
cur = self.head - начинаем с самого начала списка
while cur.next != None: - пока у текущего узла есть следующий, идём вперёд
cur = cur.next - переходим к следующему элементу
cur.next = new_node - когда дошли до конца, добавляем новый элемент в список


4. Метод length — сколько всего элементов

def length(self):
    cur = self.head
    total = 0
    while cur.next != None:
        total += 1
        cur = cur.next
    return total

cur = self.head - начинаем с самого начала списка
total = 0 - счётчик количества элементов
while cur.next != None: -  пока есть следующий узел — продолжаем считать
total += 1 - добавляем 1 к счётчику
cur = cur.next - переходим к следующему элементу
return total - возвращаем общее количество

5. Метод display — показать все элементы

def display(self):
    elems = []
    cur = self.head
    while cur.next != None:
        cur = cur.next
        elems.append(cur.data)
    print(elems)

elems = [] = создаём пустой список, в который положим значения
cur = self.head - начинаем с самого начала списка
while cur.next != None: -  пока есть следующий узел — продолжаем считать
cur = cur.next - переходим к следующему элементу
elems.append(cur.data) - добавляем значение текущего узла в список
print(elems) -  выводим все значения на экран

"""