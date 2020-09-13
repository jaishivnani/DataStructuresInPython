from exceptions import Empty

class LinkedList:

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
        else:
            '''Step 2 - Assigning Next Member of New Node Ex-70 to self._head (10-1st Node)'''
            newest._next = self._head
        self._head = newest
        self._size+=1

    def add_last(self,e):
        '''Step 1 - Creating New Node'''
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            '''Step 2 - Assigning Next Member of Last Node to New Node Ex-70'''
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
            raise Empty('List is Empty')
        del_element = self._head._element
        self._head = self._head._next
        self._size-=1
        if self.is_empty():
            self._head = None
            self._head = None
        return del_element

    def remove_last(self):
        if self.is_empty():
            raise Empty('List is Empty')
        thead = self._head
        i = 0
        while i < len(self)-2:
            thead = thead._next
            i = i + 1
        self._tail = thead
        thead = thead._next
        del_element = thead._element
        self._tail._next = None
        self._size-=1
        return del_element

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
        while thead:
            print(thead._element, end='-->')
            thead = thead._next
        print()



L = LinkedList()
L.add_last(10)
L.add_last(20)
L.add_last(30)
L.add_last(40)
L.display()
print('Delete First: ', L.remove_first())
L.display()
L.add_first(70)
L.display()
print('Delete Last: ', L.remove_last())
L.display()
L.add_any(100,2)
L.display()
L.remove_any(2)
L.display()




