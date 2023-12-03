class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.

        nodes ლისტში აგროვებს მნიშვნელობებს while ციკლის დახმარებით იქამდე სანამ curr არ გახდება none, ანუ სანამ
        დაკავშირებულ სიას ბოლომდე არ ჩაივლის.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))    #  nodes - სიაში ამატებს მნიშვნელობებს. მონაცემები იცვლება სტრინგ ტიპად
            curr = curr.next

        return '[' + ', '.join(nodes) + ']'  # აბრუნებს nodes-სიაში შეგროვებულ მონაცემებს, სიას დამსგავსებული ვისუალით

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
linked_list = SinglyLinkedList()
linked_list.append([3,6,7])
# linked_list.append(1)
linked_list.append(0)
linked_list.append('2')
linked_list.append(1)
linked_list.append(True)

test = linked_list.find([3,6,7])
print(type(test))
print(linked_list)
