class MyList:
    def __init__(self, *values):
        self.size = 0
        self.head = None
        if len(values) > 0:
            self.head = MyNode(values[0])
            self.size = 1
            for value in values[1:]:
                self.add(value)

    def get_size(self):
        return self.size

    def clear(self):
        self.head = None
        self.size = 0

    def add(self, *values):
        if len(values) == 0:
            return

        if self.head is None:
            self.head = MyNode(values[0])
            self.size = 1
            values = values[1:]

        if len(values) == 0:
            return

        current_node = self.head
        while current_node.hasNext():
            current_node = current_node.next
        for value in values:
            current_node.next = MyNode(value)
            self.size += 1
            current_node = current_node.next

    def has(self, value):
        if self.head:
            current_node = self.head
            while current_node.hasNext():
                if current_node.value == value:
                    return True
                current_node = current_node.next

            if current_node.value == value:
                return True
        return False

    def get(self, index):
        if index < self.size and self.head:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            return current_node.value
        return None

    def get_index_of(self, value):
        if self.head:
            current_node = self.head
            index = 0
            while current_node.hasNext():
                if current_node.value == value:
                    return index
                current_node = current_node.next
                index += 1
            if current_node.value == value:
                return index
        return -1

    def remove(self, index):
        if index < self.size and self.head:
            if index == 0:
                to_be_removed = self.head
                self.head = self.head.next
                self.size -= 1
                return to_be_removed.value
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            to_be_removed = current_node.next
            new_next = to_be_removed.next
            current_node.next = new_next
            self.size -= 1
            return to_be_removed.value
        return None


class MyNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def hasNext(self):
        return True if self.next else False
