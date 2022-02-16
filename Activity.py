# import networkx as nx

class Activity:
    def __init__(self, Duration, Prereq, Nodepath):
        """
        Initializes the activity with
        duration, list of prerequisites, early start time, late start time,
        and path of the nodes connecting the activity edge.
        """
        self.path = Nodepath
        self.earlyStart
        self.lateStart
        self.duration = Duration
        self.prereq = Prereq

    def calculate(activity):
        """
        Recursively calculate late start time
        """
        pass

    def findEarlyStart(self):
        """
        Find early start time for all activities
        """
        # if no prereq, early start time is 0
        if self.prereq is None:
            self.earlyStart = 0
        # if one prereq, add duration of prereq + prereq's early start
        elif len(self.prereq) == 1:
            prereq = self.prereq[0]
            self.earlyStart = prereq.earlyStart + prereq.duration
        # if more than one prereq, find the maximum
        else:
            max_prereq = 0
            for prereq in self.prereq:
                tmp_et = prereq.earlyStart + prereq.duration
                if tmp_et > max_prereq:
                    max_prereq = tmp_et
            self.earlyStart = max_prereq

        return self.earlyStart

    def findLateStart():
        """
        Find late start time for all activities
        """
        pass
