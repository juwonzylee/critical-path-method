from Activity import (
    ActivityEdge,
    ProjectNode
)

# Initializing the activities
A = ActivityEdge(5, 'A', [])
B = ActivityEdge(4, 'B', [A])
C = ActivityEdge(5, 'C', [A])
D = ActivityEdge(3, 'D', [A])
E = ActivityEdge(2, 'E', [B])
F = ActivityEdge(2, 'F', [C, E])
G = ActivityEdge(1, 'G', [D, F])
H = ActivityEdge(1, 'H', [G])

# Initializing the project nodes
p1 = ProjectNode([])
p2 = ProjectNode([(A, p1)])
p3 = ProjectNode([(B, p2)])
p4 = ProjectNode([(C, p2), (E, p3)])
p5 = ProjectNode([(D, p2), (F, p4)])
p6 = ProjectNode([(G, p5)])
p7 = ProjectNode([(H, p6)])

def test_findEarlyStart():
    assert p1.findEarlyStart() == 0
    assert p2.findEarlyStart() == 5
    assert p3.findEarlyStart() == 9
    assert p4.findEarlyStart() == 11
    assert p5.findEarlyStart() == 13
    assert p6.findEarlyStart() == 14
    assert p7.findEarlyStart() == 15


def test_findLateStart():
    maxDuration = p7.findEarlyStart()
    assert p7.findLateStart(maxDuration, []) == 15
    assert p6.findLateStart(maxDuration, [(H, p7)]) == 14
    assert p5.findLateStart(maxDuration, [(G, p6)]) == 13
    assert p4.findLateStart(maxDuration, [(F, p5)]) == 11
    assert p3.findLateStart(maxDuration, [(E, p4)]) == 9
    assert p2.findLateStart(maxDuration, [(B, p3), (C, p4), (D, p5)]) == 5
    assert p1.findLateStart(maxDuration, [(A, p2)]) == 0


def test_findFreeFloat():

    try:
        edge1 = ActivityEdge(1, "edge1", [])
        edge2 = ActivityEdge(2, "edge2", [edge1])
        node1 = ProjectNode([])
        node2 = ProjectNode([node1])
    except NameError as e:
        assert False, e

    node1.earlyStart = 0
    node2.lateStart = 3
    assert edge2.findFreeFloat((node1, node2)) == 1
    assert edge1.findFreeFloat((node1, node2)) == 2

    assert A.findFreeFloat((p1, p2)) == 0
    assert B.findFreeFloat((p2, p3)) == 0
    assert C.findFreeFloat((p2, p4)) == 1
    assert D.findFreeFloat((p2, p5)) == 5
    assert E.findFreeFloat((p3, p4)) == 0
    assert F.findFreeFloat((p4, p5)) == 0
    assert G.findFreeFloat((p5, p6)) == 0
    assert H.findFreeFloat((p6, p7)) == 0
