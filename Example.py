from cpm.CriticalPath import CriticalPath
from cpm.Activity import (
    ActivityEdge,
    ProjectNode
)


# Initializing the activities
A = ActivityEdge(5, [])
B = ActivityEdge(4, [A])
C = ActivityEdge(5, [A])
D = ActivityEdge(3, [A])
E = ActivityEdge(2, [B])
F = ActivityEdge(2, [C, E])
G = ActivityEdge(1, [D, F])
H = ActivityEdge(1, [G])

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

# Calculate free float for all activity edges
_ = A.findFreeFloat((p1, p2))
_ = B.findFreeFloat((p2, p3))
_ = C.findFreeFloat((p2, p4))
_ = D.findFreeFloat((p2, p5))
_ = E.findFreeFloat((p3, p4))
_ = F.findFreeFloat((p4, p5))
_ = G.findFreeFloat((p5, p6))
_ = H.findFreeFloat((p6, p7))

# Initialize project with nodes and edges
proj = CriticalPath([A, B, C, D, E, F, G, H],
                    [p1, p2, p3, p4, p5, p6, p7])

# Calculate the critical path
# res_path = proj.findCriticalPath()
