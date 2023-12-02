class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current:
            if count == position - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1
        raise IndexError("Index out of range")

    def delete(self, data):
        current = self.head
        if current is not None and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current:
            if current.data == data:
                break
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage:
my_list = LinkedList()
my_list.append(5)
my_list.append(10)
my_list.append(15)

my_list.display()  # Output: 5 -> 10 -> 15 -> None

my_list.insert(12, 2)
my_list.display()  # Output: 5 -> 10 -> 12 -> 15 -> None

my_list.delete(10)
my_list.display()  # Output: 5 -> 12 -> 15 -> None