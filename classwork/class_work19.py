# class ListNode:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#     def __repr__(self):
#         return str(self.value)
        

# class LinkedList:
#     def __init__(self,value):
#         self.head = ListNode(value)
#         self.length = 1

#     def append(self, value):
#         current_node = self.head 

#         while current_node.next is not None:
#             current_node = current_node.next
        
#         new_node = ListNode(value)
#         current_node.next = new_node

#         self.length += 1

#     def instert (self, value , index):
#         last_index =  self.length - 1
#         i = 0
#         if index == 0:
#             old_head = self.head
#             self.head = ListNode(value)
#             self.head.next = old_head
#             self.length += 1
#         elif index == last_index + 1:
#             self.append(value)
#         elif 0 < index < last_index +1:
#             current_node  = self.head
#             while i != index -1:
#                 current_node = current_node.next
#                 i += 1
#             new_node = ListNode(value)
#             new_node.next = current_node.next
#             current_node.next = new_node
#             self.length += 1

#         elif index > last_index +1 or index <0:
#             print('our index is out of range!')
#     def remove(self,index):
#         last_index =  self.length - 1
#         i = 0
#         if index  == 0:
#             self.head = self.head.next
#             self.length -= 1
#         elif index == last_index:
#             current_node = self.head
#             while i < last_index - 1:
#                 current_node = current_node.next
#                 i += 1
#             current_node.next = None
#             self.length -= 1

#         elif 0 < index < last_index:
#             current_node =self.head
#             while i != index - 1:
#                 current_node = current_node.next
#                 i += 1
#             deleted_element = current_node.next
#             current_node.next = deleted_element.next
#             self.length -=1
#         elif index > last_index or index < 0:
#             print('our index is out of range!')
            
#     def printlist(self):
#         current_node = self.head
#         print(current_node, end="==>")
        
#         while current_node.next is not None:
#             current_node = current_node.next
#             print(current_node, end="==>")

# myList = LinkedList(1)
# for i in range(2,10):   
#     myList.append(i)
# myList.printlist()





# class StackNode:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#     def __repr__(self):
#         return str(self.value)
    
# class Stack:
#     def __init__(self,value):
#         self.head = StackNode(value)
#         self.lenght = 1
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next
#     def printlist(self):
#         for node in self:
#             print(f'{node}-->', end='')
#         print()
#     def size(self):
#         return self.lenght
#     def empty(self):
#         return self.lenght == 0
#     def push(self, value):
#         old_head = self.head
#         self.head = StackNode(value)
#         self.head.next = old_head
#         self.lenght+=1

    

#     def top(self):
#         if self.empty():
#             raise Exception('The stack is empty!')
#         return self.head
    
#     def pop(self):
#         if self.empty():
#             raise Exception('The stack is empty!')
#         removed = self.head
#         self.head = self.head.next
#         self.length +=1
#         return removed
# stack1 = Stack(1)
# for i in range(2,19):
#     stack1.push(i)

# print(stack1.size())
# stack1.printlist()


# from collections import deque

# queue1 = deque()
# queue1.append(1)
# queue1.append(2)
# queue1.append(3)
# print(queue1)
# print(queue1.popleft())
# print(queue1)



# from queue import Queue
# queue1 = Queue(maxsize=5)
# queue1.put(1)
# queue1.put(2)
# queue1.put(3)
# queue1.put(4)
# queue1.put(4)

# print(queue1.full())
# print(queue1.qsize())


