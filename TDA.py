class BasicNode:
    def __init__(self, data):
        self.data = data
        self.Next = None


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
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = new_node
            self.length += 1

    def len(self):
        return self.length

    def show_all(self):
        tmp = self.first
        cont = 1
        while tmp.next is not None:
            print(f"en la lista de valores en la posicion {cont} es {tmp.data}")
            tmp = tmp.next
            cont = cont + 1

    def get(self, pos):
        tmp = self.first
        cont = 0
        while tmp.Next is not None and cont != pos:
            tmp = tmp.Next
        return tmp.data


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
        self.Head = None
        self.Tail = None
        self.len = 0

    def enqueue(self, px, py, data):
        new_node = BasicNode(px, py, data)
        if self.Head is None:
            self.Head = new_node
            self.Tail = self.Head
            self.len += 1
        else:
            self.Tail.Next = new_node
            self.Tail = new_node
            self.len += 1

    def dequeue(self):
        if self.Head is None:
            print("No items in the queue")
        else:
            data = self.Head
            self.Head = self.Head.next
            if self.Head is None:
                self.Tail = None
            self.len -= 1
            return data

    def length(self):
        return self.len

    def show_queue(self):
        tmp = self.Head
        while tmp.next is not None:
            print(f"{tmp.data}")
            tmp = tmp.next
        print(f"{tmp.data}")

    def peek(self):
        return self.Head

    def last(self):
        return self.Tail
