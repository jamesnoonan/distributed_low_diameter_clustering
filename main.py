from graph import Node, Message, MessageType, example_graph_1

def get_binary_list(num: int) -> list[int]:
    return [int(x) for x in bin(num)[2:]]

def cluster_distributed(graph: list[Node]):
    highest_id = max(graph, key=lambda n: n.og_id).og_id
    rounds = len(get_binary_list(highest_id))

    for round in range(rounds):
        for node in graph:
            distributed_round(node, round)

def distributed_round(node: Node, round: int, messages: list[Message] = []) -> list[Message]:
    if (not node.deleted):
        print(f"Round {round} for Node {node.og_id}")

        # TODO: Implement
        return [Message(node.og_id, node.adjacent_nodes[0], MessageType.COLOR, "RED")]
    
    return []

cluster_distributed(example_graph_1)
