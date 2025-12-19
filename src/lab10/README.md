# Лабораторная работа №10

## A
```python 
rom collections import deque

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        return self._data[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        return self._data[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"Queue({list(self._data)})"


if __name__ == "__main__":
 
    print("ТЕСТЫ: Stack и Queue")
    
    print("Stack (LIFO):")
    s = Stack()
    
    print(f"   Создан: {s}")
    print(f"   Пуст: {s.is_empty()}")
    
    s.push(10); s.push(20); s.push(30)
    print(f"   push(10,20,30) → {s}")
    print(f"   Размер: {len(s)}")
    print(f"   peek(): {s.peek()}")
    
    print(f"   pop(): {s.pop()} → {s}")
    print(f"   pop(): {s.pop()} → {s}")
    print(f"   Пуст: {s.is_empty()}")
    
    print("Queue (FIFO):")
    q = Queue()
    
    print(f"   Создана: {q}")
    print(f"   Пуста: {q.is_empty()}")
    
    q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
    print(f"   enqueue(A,B,C) → {q}")
    print(f"   Размер: {len(q)}")
    print(f"   peek(): {q.peek()}")
    
    print(f"   dequeue(): {q.dequeue()} → {q}")
    print(f"   dequeue(): {q.dequeue()} → {q}")
    print(f"   Пуста: {q.is_empty()}")

    print("Обработка ошибок:")
    
    try:
        empty_stack = Stack()
        empty_stack.pop()
    except IndexError as e:
        print(f"   Stack.pop() из пустого: {e}")
    
    try:
        empty_queue = Queue()
        empty_queue.dequeue()
    except IndexError as e:
        print(f"   Queue.dequeue() из пустой: {e}")

    print("Сравнение поведения:")
    print("   Stack: push(1,2,3) → pop() вернет 3,2,1")
    print("   Queue: enqueue(1,2,3) → dequeue() вернет 1,2,3")
```
![47](/images/lab10/img01.png)

## B

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"index {idx} out of range")
        
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self._size += 1

    def remove(self, value):
        if self.is_empty():
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                self._size -= 1
                return True
            current = current.next
        return False

    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError(f"index {idx} out of range")
        
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            value = current.next.value
            current.next = current.next.next
            if current.next is None:
                self.tail = current
        
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"SinglyLinkedList({list(self)})"


if __name__ == "__main__":
    print("=" * 40)
    print("ТЕСТЫ SinglyLinkedList")
    print("=" * 40)
    
    lst = SinglyLinkedList()
    print(f"Создан: {lst}, пуст: {lst.is_empty()}")
    
    print("Добавление:")
    for i in [10, 20, 30]:
        lst.append(i)
    print(f"   append(10,20,30) → {lst}")
    
    lst.prepend(5)
    print(f"   prepend(5) → {lst}")
    
    lst.insert(2, 15)
    print(f"   insert(2,15) → {lst}")
    
    print(f"   Размер: {len(lst)}")
    print(f"   Элементы: {list(lst)}")
    
    print("Удаление:")
    lst.remove(15)
    print(f"   remove(15) → {lst}")
    
    removed = lst.remove_at(1)
    print(f"   remove_at(1) → {removed}, список: {lst}")
    
    print(f"Крайние случаи:")
    empty = SinglyLinkedList()
    print(f"   Пустой список: {empty}")
    print(f"   remove(99) на пустом: {empty.remove(99)}")
    
    try:
        empty.remove_at(0)
    except IndexError as e:
        print(f"   Ошибка remove_at(0): {e}")
```

![47](/images/lab10/img02.png)