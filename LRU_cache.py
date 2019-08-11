# Least Recently Used Cache
# Default capacity is 5
# Fast Lookups : Hash Table
# Fast Removals : Double Linked List

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.ItemsInCache = 0
        self.lookups = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key):
        if key in self.lookups:
            node = self.lookups[key]
            self.remove(node)
            seld.add(node)
            return node.value

    def put(self, key, value):
        if key in self.lookups:
            self.remove(self.lookups[key])
        node = Node(key, value)
        self.add(node)
        self.lookups[key] = node
        if len(self.lookups) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dict[node.key]

    def add(self, node):
        previous = self.tail.previous
        previous.next = node
        self.tail.previous = node
        node.previous = previous
        node.next = self.tail

    def remove(self, node):
        preious = node.prevous
        next = node.next
        previous.next = next
        next.previous = previous
