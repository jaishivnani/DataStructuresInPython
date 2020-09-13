from exceptions import Empty

class CircularLinkedList:

    class _Node:
        '''Instance variables'''
        __slots__ = '_element','_next'

        def __init__(self, element, next):
            self._element  = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self,e):
        '''Step 1 - Creating New Node'''
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
            newest._next = newest

        else:
            '''Pointing tail to newest and Pointing newest_next to self._head (Old) and self._head = newest'''
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size+=1

    def add_last(self,e):
        '''Step 1 - Creating New Node'''
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
            newest._next = newest
        else:
            '''Step 2 - Pointing newest_next to tail in circular format'''
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size+=1

    def add_any(self,e,pos):
        '''Step 1 - Creating New Node'''
        newest = self._Node(e, None)
        '''Step 2 - Creating a temporary head named as thead and Point it to head.'''
        thead = self._head
        i = 1
        '''Step 3 - Move thead to the respective position after which you need to insert'''
        while i < pos:
            thead = thead._next
            i = i + 1
        newest._next = thead._next
        thead._next = newest
        self._size+=1

    def remove_first(self):
        if self.is_empty():
            raise Empty('Linked List Empty')
        oldhead = self._tail._next
        self._tail._next = oldhead._next
        self._head = oldhead._next
        self._size-=1
        if self.is_empty():
            self._tail = None
        return oldhead._element

    def remove_last(self):
        if self.is_empty():
            raise Empty('List is Empty')
        thead = self._head
        i = 0
        while i < len(self)-2:
            thead = thead._next
            i = i + 1
        self._tail = thead
        self._tail._next = self._head
        thead = thead._next
        value = thead._element
        self._size -= 1
        return value

    def remove_any(self,pos):
        thead = self._head
        i = 1
        while i < pos - 1:
            thead = thead._next
            i = i + 1
        del_element = thead._next._element
        thead._next = thead._next._next
        self._size-=1
        return del_element

    def display(self):
        thead = self._head
        i = 0
        while i<len(self):
            print(thead._element, end='-->')
            thead = thead._next
            i = i + 1
        print()



CL = CircularLinkedList()
CL.add_last(10)
CL.add_last(20)
CL.add_last(30)
CL.add_last(40)
CL.display()
print('Delete First: ', CL.remove_first())
CL.display()
CL.add_first(70)
CL.display()
print('Delete Last: ', CL.remove_last())
CL.display()
CL.add_any(100,2)
CL.display()
CL.remove_any(2)
CL.display()




