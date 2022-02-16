from cpm.Activity import (
    ActivityEdge,
    ProjectNode
)
# from cpm.CriticalPath import CriticalPath

# Initializing the activities
A = ActivityEdge(5, [], (1, 2))
B = ActivityEdge(4, [A], (2, 3))
C = ActivityEdge(5, [A], (2, 4))
D = ActivityEdge(3, [A], (2, 5))
E = ActivityEdge(2, [B], (3, 4))
F = ActivityEdge(2, [C, E], (4, 5))
G = ActivityEdge(1, [D, F], (5, 6))
H = ActivityEdge(1, [G], (6, 7))

# Initializing the project nodes
p1 = ProjectNode([])
p2 = ProjectNode([(A, p1)])
p3 = ProjectNode([(B, p2)])
p4 = ProjectNode([(C, p2), (E, p3)])
p5 = ProjectNode([(D, p2), (F, p4)])
p6 = ProjectNode([(G, p5)])
p7 = ProjectNode([(H, p6)])

# Calculating early start times for all project nodes
_ = p1.findEarlyStart()
_ = p2.findEarlyStart()
_ = p3.findEarlyStart()
_ = p4.findEarlyStart()
_ = p5.findEarlyStart()
_ = p6.findEarlyStart()
_ = p7.findEarlyStart()

# Calculating late start times for all project nodes
maxDuration = p7.findEarlyStart()
_ = p7.findLateStart(maxDuration, [])
_ = p6.findLateStart(maxDuration, [(H, p7)])
_ = p5.findLateStart(maxDuration, [(G, p6)])
_ = p4.findLateStart(maxDuration, [(F, p5)])
_ = p3.findLateStart(maxDuration, [(E, p4)])
_ = p2.findLateStart(maxDuration, [(B, p3), (C, p4), (D, p5)])
_ = p1.findLateStart(maxDuration, [(A, p2)])
