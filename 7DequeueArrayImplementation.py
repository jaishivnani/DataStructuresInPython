from exceptions import Empty

class ArrayDequeue:

    def __init__(self):
        '''Since we don't have array's in python we will use self._data = [List] to implement Dequeue's using array's'''
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._data[-1]

    def add_first(self,e):
        self._data.insert(self._front,e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Dequeue is Empty')
        value = self._data.pop(self._front)
        return value

    def delete_last(self):
        if self.is_empty():
            raise Empty('Dequeue is Empty')
        value = self._data.pop()
        return value



d = ArrayDequeue()

d.add_last(50)
d.add_last(60)
d.add_last(70)
d.add_last(80)

d.add_first(40)
d.add_first(30)
d.add_first(20)
d.add_first(10)

print('Deque: ', d._data)
print('Length: ', len(d))
print('Delete First: ', d.delete_first())
print('Length: ', len(d))
print('Deque: ', d._data)
print('Delete Last: ', d.delete_last())
print('Length: ', len(d))
print('Deque: ', d._data)
print('First: ', d.first())
print('Last: ', d.last())






