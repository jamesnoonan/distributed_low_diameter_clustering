import math
from graph import Node, NodeColor, Message, MessageType, example_graph_1

def get_binary_list(num: int) -> list[int]:
    return [int(x) for x in bin(num)[2:]]

# Run the distributed clustering algorithm on a graph, sending messages between nodes
def cluster_distributed(graph: list[Node]):
    n = len(graph)

    # Get the highest ID in the graph to determine the number of rounds
    highest_id = max(graph, key=lambda n: n.og_id).og_id
    b = len(get_binary_list(highest_id))

    messages = []

    for round in range(b):
        # There are four communication steps, and then steps needed to propogate the decision down the subtree
        steps_in_round = math.ceil(round * math.log2(n)) + 4
        
        for step in range(steps_in_round):
            next_messages = []

            # Iterate over all nodes (simulating a distributed system)
            for node in graph:
                # Filter messages for this node
                node_input_messages = [m for m in messages if m.recipient_id == node.og_id]

                # Run a single round on one node
                node_output_messages = distributed_step(node, round, step, node_input_messages)

                # Add the output messages to the list of messages
                next_messages.extend(node_output_messages)

            messages = next_messages

# A single step of the distributed algorithm for a single node
def distributed_step(node: Node, round: int, step: int, messages: list[Message] = []) -> list[Message]:
    if (not node.deleted):
        print(f"Round {round} for Node {node.og_id} [Received messages from {', '.join([str(m.sender_id) for m in messages])}]")

        # Compute the color of the node based on the round, red clusters can only grow and blue clusters can only shrink
        node_color = NodeColor.RED if get_binary_list(node.id)[round] == 1 else NodeColor.BLUE

        if step == 0: # In the first step of each round, every node sends its color to all its neighbors
            # TODO: send size of subtree as well
            return [Message(node.og_id, neighbor_id, MessageType.COLOR, node_color) for neighbor_id in node.adjacent_nodes]
        elif step == 1: # In the second step of each round, each blue node propose to join adjacent red nodes
            if (node_color == NodeColor.BLUE):
                # In each step, every node in a blue cluster neighboring with a red cluster proposes to join an
                # arbitrary neighboring red cluster
                pass
        elif step == 2: # In the third step of each round, red nodes decide to accept or reject the proposals
            if (node_color == NodeColor.RED):
                # For a given red cluster C, if the total number of proposing blue nodes is at least |C|/(2b), then C
                # decides to grow by adding all the proposing blue nodes to the cluster
                pass
        elif step == 3: # In the fourth step of each round, blue nodes either join a red cluster or are deleted
            if (node_color == NodeColor.BLUE):
                # If a blue node joins a red cluster, it stops being a terminal

                # The proposing nodes are deleted which results in C not being adjacent to any other blue nodes until
                # the end of the phase
                pass
        else: # Send decision down subtree to children
            if (node_color == NodeColor.BLUE):
                # If a message is received from parent, update current node and resend to children
                pass
    
    return []

# Run the distributed clustering algorithm on the example graph
cluster_distributed(example_graph_1)
