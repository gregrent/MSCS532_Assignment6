########################################
# MSCS 532 Assignment 6 (Part 2)
# Elementary Data Structures
########################################

class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            raise IndexError("Index out of range")

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        else:
            raise IndexError("Index out of range")

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __str__(self):
        return str(self.data)


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def access(self, row, col):
        return self.data[row][col]

    def insert(self, row, col, value):
        self.data[row][col] = value

    def delete(self, row, col):
        self.data[row][col] = 0  # set to default (0)

    def __str__(self):
        return '\n'.join(str(row) for row in self.data)
    
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        raise IndexError("Dequeue from empty queue")

    def front(self):
        if self.queue:
            return self.queue[0]
        raise IndexError("Front from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, value):
        temp = self.head
        prev = None
        while temp:
            if temp.data == value:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
        raise ValueError("Value not found")

    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    def traverse(self, level=0):
        print('  ' * level + str(self.value))
        for child in self.children:
            child.traverse(level + 1)

# Array
arr = Array()
arr.insert(0, 10)
arr.insert(1, 20)
print("Array:", arr)

# Stack
stack = Stack()
stack.push(1)
stack.push(2)
print("Stack pop:", stack.pop())

# Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print("Queue dequeue:", queue.dequeue())

# Linked List
ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_beginning(5)
print("Linked List traversal:", ll.traverse())

# Rooted Tree
root = TreeNode("Root")
child1 = TreeNode("Child1")
child2 = TreeNode("Child2")
root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode("Grandchild1"))
root.traverse()


