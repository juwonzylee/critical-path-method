class ActivityEdge:
    def __init__(self, Duration, Prereq, Nodepath):
        """
        Initializes the activity edges with
        duration, list of prerequisites,
        and a tuple of the nodes connecting the activity edge.
        """
        self.path = Nodepath
        self.duration = Duration
        self.prereq = Prereq
        self.freefloat = 0

    def findFreeFloat():
        """
        Calculates the free float of the activity
        based on the early start time and late start time of
        node path.
        """
        pass


class ProjectNode:
    def __init__(self, inputPaths):
        """
        Initializes the project nodes with input activities and nodes
        and early start time.
        """
        self.inputPaths = inputPaths
        self.earlyStart = 0
        self.lateStart = 0

    def findEarlyStart(self):
        """
        Find early start time for all project nodes
        """
        # if no prereq, early start time is 0
        if self.inputPaths is None:
            self.earlyStart = 0
        # if one prereq, add duration of prereq + previous node's early start
        elif len(self.inputPaths) == 1:
            prereq, prenode = self.inputPaths[0]
            self.earlyStart = prereq.duration + prenode.earlyStart
        # if more than one prereq, find the maximum
        else:
            max_time = 0
            for prereq, prenode in self.inputPaths:
                tmp_et = prenode.earlyStart + prereq.duration
                if tmp_et > max_time:
                    max_time = tmp_et
            self.earlyStart = max_time

        return self.earlyStart

    def findLateStart(self, maxDuration, outputPaths):
        """
        Find late start time for all project nodes
        """
        # if last project node as output path, equal to early start time
        if outputPaths is None:
            self.lateStart = self.earlyStart
        elif len(outputPaths) == 1:
            act, node = outputPaths[0]
            self.lateStart = node.lateStart - act.duration
        else:
            min_time = maxDuration
            for act, node in outputPaths:
                tmp_lt = node.lateStart - act.duration
                if tmp_lt < min_time:
                    min_time = tmp_lt
            self.lateStart = min_time

        return self.lateStart
