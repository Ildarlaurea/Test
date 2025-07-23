# Определяем класс Node — это один узел связанного списка
class Node:
    def __init__(self, data):
        self.data = data         # Хранимое значение (например, число или строка)
        self.next = None         # Ссылка на следующий узел (по умолчанию None, потому что пока следующего узла нет)

# Определяем класс LinkedList — это сам односвязный список
class LinkedList:
    def __init__(self):
        self.head = None         # Голова списка — начальный элемент. Пока список пустой, поэтому head = None
    # Метод для проверки, пустой ли список
    def isEmpty(self):
        return self.head is None  # Если голова не указывает ни на один узел, значит список пуст
    # Метод для добавления нового элемента (узла) в конец списка
    def append(self, data):
        new_node = Node(data)    # Создаём новый узел, в который помещаем переданные данные

        # Если список пустой (нет ни одного элемента)
        if self.head is None:
            self.head = new_node # Новый узел становится первым элементом списка
            return               # Выходим из метода, потому что вставка завершена

        # Если список уже содержит элементы, идём по списку до самого конца
        current = self.head      # Начинаем с головы списка
        while current.next is not None:  # Пока существует следующий элемент
            current = current.next       # Переходим к следующему узлу

        current.next = new_node  # Последний узел теперь указывает на новый узел (добавили в конец)
    # Метод для удаления последнего элемента из списка
    def pop(self):
        # Если список пуст, удалять нечего
        if self.head is None:
            print("Список пустой. Удалять нечего.")
            return

        # Если в списке только один элемент
        if self.head.next is None:
            print(f"Удалён: {self.head.data}")  # Показываем, что удаляется
            self.head = None                   # Просто обнуляем голову — список снова пуст
            return

        # В остальных случаях: идём по списку до предпоследнего элемента
        current = self.head
        while current.next.next is not None:
            current = current.next  # Двигаемся по списку

        # После цикла current — это предпоследний узел
        print(f"Удалён: {current.next.data}")  # Показываем данные удаляемого последнего узла
        current.next = None                    # Отрываем ссылку на последний узел, удаляя его
    # Метод для вставки элемента в список по определённому индексу (позиции)
    def insertAtIndex(self, data, index):
        new_node = Node(data)  # Создаём новый узел

        # Если индекс 0 — вставка в начало списка
        if index == 0:
            new_node.next = self.head  # Новый узел указывает на текущую голову
            self.head = new_node       # Новый узел становится новой головой списка
            return

        current = self.head            # Начинаем идти с головы списка
        position = 0                   # Текущая позиция (начинаем с 0)

        # Идём по списку до узла, перед которым нужно вставить новый элемент
        while current is not None and position < index - 1:
            current = current.next    # Переход к следующему узлу
            position += 1             # Увеличиваем позицию

        # Если current стал None — значит индекс был слишком большим
        if current is None:
            print("Индекс вне диапазона — элемент не вставлен.")
            return

        # Вставляем узел: новый узел указывает на следующий за current, а current теперь указывает на новый
        new_node.next = current.next
        current.next = new_node
    # Метод для вывода всех элементов списка на экран
    def display(self):
        current = self.head  # Начинаем с головы списка
        while current is not None:  # Пока не достигнем конца списка
            print(current.data, end=" -> ")  # Выводим значение узла и стрелочку
            current = current.next           # Переходим к следующему узлу
        print("None")  # Конец списка (следующего узла больше нет)
