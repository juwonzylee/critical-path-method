from CriticalPath import CriticalPath
from Activity import (
    ActivityEdge,
    ProjectNode
)
import matplotlib.pyplot as plt
import networkx as nx

# Initializing the activities
A = ActivityEdge(3, 'A', [])
B = ActivityEdge(2, 'B', [A])
C = ActivityEdge(6, 'C', [A])
D = ActivityEdge(2, 'D', [C])
E = ActivityEdge(3, 'E', [A])
F = ActivityEdge(3, 'F', [B])
G = ActivityEdge(5, 'G', [C])
H = ActivityEdge(1, 'H', [C])
I1 = ActivityEdge(1.5, 'I', [F, H])
J = ActivityEdge(2, 'J', [I1])
Dummy = ActivityEdge(0, "Dummy", [])

# Initializing the project nodes
p1 = ProjectNode([])
p2 = ProjectNode([(A, p1)])
p3 = ProjectNode([(B, p2)])
p4 = ProjectNode([(C, p2)])
p5 = ProjectNode([(F, p3), (H, p4)])
p6 = ProjectNode([(I1, p5)])
p7 = ProjectNode([(D, p4)])
p8 = ProjectNode([(E, p2), (G, p4), (J, p6), (Dummy, p7)])

# Calculating early start times for all project nodes
_ = p1.findEarlyStart()
_ = p2.findEarlyStart()
_ = p3.findEarlyStart()
_ = p4.findEarlyStart()
_ = p5.findEarlyStart()
_ = p6.findEarlyStart()
_ = p7.findEarlyStart()
_ = p8.findEarlyStart()

# Calculating late start times for all project nodes
maxDuration = p8.findEarlyStart()
_ = p8.findLateStart(maxDuration, [])
_ = p7.findLateStart(maxDuration, [(Dummy, p8)])
_ = p6.findLateStart(maxDuration, [(J, p8)])
_ = p5.findLateStart(maxDuration, [(I1, p6)])
_ = p4.findLateStart(maxDuration, [(H, p5), (G, p8), (D, p7)])
_ = p3.findLateStart(maxDuration, [(F, p5)])
_ = p2.findLateStart(maxDuration, [(B, p3), (C, p4), (E, p8)])
_ = p1.findLateStart(maxDuration, [(A, p2)])

# Calculate free float for all activity edges
_ = A.findFreeFloat((p1, p2))
_ = B.findFreeFloat((p2, p3))
_ = C.findFreeFloat((p2, p4))
_ = D.findFreeFloat((p4, p7))
_ = E.findFreeFloat((p2, p8))
_ = F.findFreeFloat((p3, p5))
_ = G.findFreeFloat((p4, p8))
_ = H.findFreeFloat((p4, p5))
_ = I1.findFreeFloat((p5, p6))
_ = J.findFreeFloat((p6, p8))


def test_findCriticalPath():
    proj = CriticalPath([A, B, C, D, E, F, G, H, I1, J],
                        [p1, p2, p3, p4, p5, p6, p7, p8])
    # assert proj.plotGraph()
    assert proj.findCriticalPath() == ['A', 'C', 'G']


def test_visualize():
    """
    Visualizes the network problem used in the test file
    """
    # set up the tasks:
    tasks = [("A", {"Duration": 3}),
             ("B", {"Duration": 2}),
             ("C", {"Duration": 6}),
             ("D", {"Duration": 2}),
             ("E", {"Duration": 3}),
             ("F", {"Duration": 3}),
             ("G", {"Duration": 5}),
             ("H", {"Duration": 1}),
             ("I", {"Duration": 1.5}),
             ("J", {"Duration": 3})]

    # set up the dependencies along all paths:
    dependencies = [("A", "B"),
                    ("A", "C"),
                    ("C", "D"),
                    ("A", "E"),
                    ("B", "F"),
                    ("C", "G"),
                    ("C", "H"),
                    ("F", "I"),
                    ("H", "I"),
                    ("I", "J")]

    # initialize (directed) graph
    G_test = nx.DiGraph()

    # add tasks and dependencies (edges)
    G_test.add_nodes_from(tasks)
    G_test.add_edges_from(dependencies)

    # set up position nodes
    pos_nodes = {"A": (1, 1),
                 "B": (2, 1),
                 "C": (2, 3),
                 "D": (3, 5),
                 "E": (2, 0),
                 "F": (3, 1),
                 "G": (3, 3),
                 "H": (3, 2),
                 "I": (4, 1),
                 "J": (5, 1)}

    # drawing the project diagram
    nx.draw(G_test, with_labels=True, pos=pos_nodes,
            node_color='lightblue', arrowsize=20)
    pos_attrs = {node: (coord[0], coord[1] + 0.2)
                 for node, coord in pos_nodes.items()}
    attrs = nx.get_node_attributes(G_test, 'Duration')
    nx.draw_networkx_labels(G_test, pos=pos_attrs, labels=attrs)
    plt.margins(0.1)
    plt.savefig("./example.jpg")
