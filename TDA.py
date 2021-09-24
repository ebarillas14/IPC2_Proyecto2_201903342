class BasicNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class BasicLinkedList:
    def __init__(self):
        self.first = None
        self.length = 0

    def insert(self, data):
        new_node = BasicNode(data)
        if self.first is None:
            self.first = new_node
            self.length += 1
        else:
            tmp = self.first
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = new_node
            self.length += 1

    def len(self):
        return self.length

    def show_all(self):
        tmp = self.first
        cont = 0
        while tmp.next is not None:
            print(f"en la lista de valores en la posicion {cont} es {tmp.data}")
            tmp = tmp.next
            cont = cont + 1
        print(f"en la lista de valores en la posicion {cont} es {tmp.data}")

    def get(self, pos):
        tmp = self.first
        cont = 0
        while tmp.next is not None and cont != pos:
            tmp = tmp.next
            cont += 1
        return tmp.data

    def append(self, basic_list):
        if self.first is None:
            self.first = basic_list.first
            self.length += basic_list.len()
        else:
            tmp = self.first
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = basic_list.first
            self.length += basic_list.len()


class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.actual = None
        self.length = 0

    def insert(self, data):
        new_node = DoubleNode(data)
        if self.first is None:
            self.first = new_node
            self.length += 1
        else:
            tmp = self.first
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = new_node
            new_node.prev = tmp
            self.length += 1

    def get_value(self, px, py):
        tmp = self.first
        while (tmp.px != px or tmp.py != py) and tmp.next is not None:
            tmp = tmp.next
        return tmp.data

    def len(self):
        return self.length

    def show_all(self):
        tmp = self.first
        while tmp.next is not None:
            print(f"en la lista de valores en la posicion x({tmp.px}) y({tmp.py}) el peso de la casilla es {tmp.data}")
            tmp = tmp.next

    def update(self, px, py, value):
        tmp = self.first
        while (tmp.px != px or tmp.py != py) and tmp.next is not None:
            tmp = tmp.next
        tmp.data = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue(self, data):
        new_node = BasicNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.len += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.len += 1

    def dequeue(self):
        if self.head is None:
            print("No items in the queue")
        else:
            data = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.len -= 1
            return data

    def length(self):
        return self.len

    def show_queue(self):
        tmp = self.head
        while tmp.next is not None:
            print(f"{tmp.data}")
            tmp = tmp.next
        print(f"{tmp.data}")

    def peek(self):
        return self.head

    def last(self):
        return self.tail
