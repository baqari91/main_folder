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
            nodes.append(repr(curr))    #  nodes - სიაში ამატებს მნიშვნელობებს. მონაცემები ინახება სტრინგ ტიპად
            curr = curr.next            # ყოველი დამატების შემდეგ ,მიმდინარე კვანძს მიენიჭება შემდეგი კვანძის მისამართი. როცა სია დასრულდება გადაეცება none da ციკლის გაჩერდება

        return '[' + ', '.join(nodes) + ']'  # აბრუნებს nodes-სიაში შეგროვებულ მონაცემებს, სიას დამსგავსებული ვიზუალით

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        self.head-is ადგილზე ემატება prepend-ის data-პარამეტრში შეყვანილი ინფორმაცია.
        """
        self.head = ListNode(data=data, next=self.head) #listnode აბრუნებს data-ს ხოლო next-ს ანიჭებს ჩამადებამდე არსებულ პირველ ელემენტს- იგივე self.head-ს

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        append იღებს data პარამეტრს რომელიც ემატება სიის ბოლოს
        """
        if not self.head:  # თუ სია ცარიელია ანუ თუ self.head უდრის nones-s მაშინ self.head გახდეს მიღებული დატა
            self.head = ListNode(data=data)
            return              # თუ შესრულდა პირობა return დაასრულებს მეთოდის მუშაობას და აღარ გაგრძელდება ქვედა კოდი
        curr = self.head      # ეს თუ გაეშვა ესეიგი არსებობს უკვე self.head ობიექტი. curr ცვლადს გადაეცემა  data და next ატრიბუტები და მნიშვნელობას იღებს სიის პირველი ნომრის
        while curr.next:     # ციკლლმა იმუშაოს იქამდე სანამ არ გახდება None
            curr = curr.next  # ყოველ შემდეგ ჯერზე curr გახდეს შემდეგი მნიშნვლეობა
        # გაირბენს სიის თავიდან ბოლოში
        curr.next = ListNode(data=data)  # curr.next -ს მიენიჭოს append-ით შემოტანილი data. რაც გახდება სიის ბოლო მონაცემი

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.

        თუ curr.data არ უდრის key-ს იმუშაოს ციკლმა.
        ხოლო თუ უდრის ციკლი გაჩერდება და ეს იმას ნიშნავს რომ
         curr-ს მინიჭებული მნიშვნელობა უდრის key-s მნიშვნლობას
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.

         თუ remove-დან მიღებული key უდრის სიის პირველ მონაცემს while ციკლი არ ჩაირთვება,
        შესრულდება მხოლოდ if ბლოკი და წაიშლება სიის პირველი მონაცემი.
        სხვა შემთხვევაში while ციკლი იპოვის key-ს და ამოშლის elif ბლოკის დახმარებით
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


linked_list = SinglyLinkedList()
linked_list.append([3, 6, 7])
linked_list.append(0)
linked_list.append('2')
linked_list.append(True)
linked_list.append(1)
test = linked_list.find(1)

print(linked_list)

print(test)

