# Critical Path Method

A critical path in project management is the longest sequence of activities that must be finished on time in order for the entire project to be complete. This program sets the activities on edges and calculates the early, late start time, and free float of the activities 
in addition to the critical path of the project. 

The code is structured in the [cpm] module, where the nodes and edges objects are defined in [Activity.py](./cpm/Activity.py), and the project in [CriticalPath.py](./cpm/CriticalPath.py).

The tests written in [test_Activity.py](./cpm/test_Activity.py) are based on Question 8.4.4 from Chapter 8 of Operations Research.
The tests written in [test_CriticalPath.py](./cpm/test_CriticalPath.py) are based on Question 8.4.10 from the same textbook.

## Requirements
To install the requirements please run:
```bash
$ pip install -r requirements.txt
```

## Running the tests
The tests are written in pytest format such that each crucial Python file with a name `x.py` has an accompanying test file `test_x.py`.  Hence, to run all the tests, simply run:
```bash
$ pytest
```

## Assumptions and Limitations
This program assumes that the user manually inputs the nodes and edges of the project network in order to calculate the critical path.
This could be automated further so the user only has to put in the activities, duration, and dependencies to pre-requisite activities.
In addition, the program only accepts projects with activities on edges, and not activities on nodes. 
