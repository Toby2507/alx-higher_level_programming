#!/usr/bin/python3
"""
This module contains the class definition of a Linked list Node
"""


class Node:
    """Defines the Nodes of a Linked List"""
    def __init__(self, data, next_node=None):
        """Initializes the node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, data):
        """data setter"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        """next_node setter"""
        if next_node != None or not isinstance(node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = node


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
       """constructor"""
       self.__head: Node = none

    def __str__(self):
        """to string method"""
        s = []
        node: Node = self.__head
        while node is not None:
            s.append(str(node.data))
            node = node.next_node
        return '\n'.join(s)

    def sorted_insert(self, value):
        """inserts a new node to the list in a sorted format"""
        new_node: Node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        node = self.__head
        while node.next_node is not None and value > node.next_node.data:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
