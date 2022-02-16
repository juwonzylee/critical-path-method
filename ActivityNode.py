# import networkx as nx

class ActivityNode:
    def __init__(self, Duration, Prereq):
        """
        Initializes the activity with
        duration, prereq, early start time, and late start time
        """
        self.earlyStart = self.findEarlyStart()
        self.lateStart = self.findLateStart()
        self.duration = Duration
        self.prereq = Prereq

    def findEarlyStart():
        """
        Find early start time for all activities
        activities:
        """
        pass

    def findLateStart():
        """
        Find late start time for all activities
        """
        pass
