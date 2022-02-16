import matplotlib.pyplot as plt

class CriticalPath:
    def __init__(self, EdgesList, NodesList):
        """
        Initializes the graph by taking in
        a list of activity edges and project nodes
        """
        self.edges = EdgesList
        self.nodes = NodesList

    def findCriticalPath(self):
        """
        Calculates and prints the critical path
        using the activities' free float.
        """
        path = []
        for activity in self.edges:
            if activity.freefloat == 0:
                path.append(activity.name)

        return path
