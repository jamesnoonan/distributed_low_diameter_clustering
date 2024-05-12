from enum import Enum

# | Node |
NodeColor = Enum('NodeColor', ['RED', 'BLUE', 'NONE'])

class Node:
  def __init__(self, node_id: int, adjacent_nodes: list[int] = [], parent: int = None, deleted: bool = False):
    self.og_id = node_id
    self.id = node_id
    self.adjacent_nodes = adjacent_nodes
    
    self.parent = parent # None if it is a terminal
    self.deleted = deleted

# | Message |
MessageType = Enum('MessageType', ['COLOR', 'REQUEST', 'CONFIRM'])

class Message:
  def __init__(self, sender_id: int, recipient_id: int, type: MessageType, payload: str | int):
    self.sender_id = sender_id
    self.recipient_id = recipient_id
    self.type = type
    self.payload = payload

# Define Example Graphs
example_graph_1 = [
  Node(0, [1, 2, 3, 5]),
  Node(1, [0, 2, 3]),
  Node(2, [0, 1, 3]),
  Node(3, [0, 1, 2, 3]),
  Node(4, [3, 5]),
  Node(5, [0, 4]),
]