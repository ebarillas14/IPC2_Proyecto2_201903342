class BasicNode:
    def __init__(self, px, py, data):
        self.px = px
        self.py = py
        self.data = data
        self.Next = None


class BasicLinkedList:
    def __init__(self):
        self.First = None
        self.length = 0

    def insert(self, px, py, data):
        new_node = BasicNode(px, py, data)
        if self.First is None:
            self.First = new_node
            self.length += 1
        else:
            tmp = self.First
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = new_node
            self.length += 1

    def get_value(self, px, py):
        tmp = self.First
        while (tmp.px != px or tmp.py != py) and tmp.Next is not None:
            tmp = tmp.Next
        return tmp.data

    def len(self):
        return self.length

    def show_all(self):
        tmp = self.First
        while tmp.Next is not None:
            print(f"en la lista de valores en la posicion x({tmp.px}) y({tmp.py}) el peso de la casilla es {tmp.data}")
            tmp = tmp.Next

    def update(self, px, py, value):
        tmp = self.First
        while (tmp.px != px or tmp.py != py) and tmp.Next is not None:
            tmp = tmp.Next
        tmp.data = value


class Matrix:
    def __init__(self, row_count, col_count, value_list):
        self.matrix = BasicLinkedList()
        self.columns = col_count
        self.rows = row_count
        rows = BasicLinkedList()
        for y in range(row_count):
            cols = BasicLinkedList()
            for x in range(col_count):
                value = value_list.get_value(x, y)
                cols.insert(x, y, value)
                # value = randint(1, 100)
                # cols.insert(x, y, value)
                # print(f" Row:{y+1} Column:{x+1} Value:{value}")
            rows.insert(0, y, cols)
        self.matrix = rows

    def get_value(self, x, y):
        row = self.matrix.get_value(0, y)
        col = row.First
        while col.px != x or col.py != y and col is not None:
            col = col.Next

        return col.data

    def display_in_menu(self):
        mt = self.matrix
        tmp = self.matrix.First
        while tmp.Next is not None:
            line = "|"
            col_tmp = tmp.data.First
            while col_tmp is not None:
                line += f"{col_tmp.data}|"
                col_tmp = col_tmp.Next
            print(line)
            tmp = tmp.Next
            """ This last part of the code is to show the last 
            iteration / last row"""
        line = "|"
        col_tmp = tmp.data.First
        while col_tmp is not None:
            line += f"{col_tmp.data}|"
            col_tmp = col_tmp.Next
        print(line)

    def update_value(self, x, y, value):
        row = self.matrix.get_value(0, y)
        col = row.First
        while col.px != x or col.py != y and col is not None:
            col = col.Next
        col.data = value


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
            self.Head = self.Head.Next
            if self.Head is None:
                self.Tail = None
            self.len -= 1
            return data

    def length(self):
        return self.len

    def show_queue(self):
        tmp = self.Head
        while tmp.Next is not None:
            print(f"{tmp.data}")
            tmp = tmp.Next
        print(f"{tmp.data}")

    def peek(self):
        return self.Head

    def last(self):
        return self.Tail
