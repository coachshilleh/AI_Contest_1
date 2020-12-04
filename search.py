# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    a = [problem.getStartState()] ## gives me (5,5)
    fringe = util.Stack()
    fringe.push(a)
    previous = a[0]
    counter = 0
    a = fringe.pop()
    c = a[0]
    visited_nodes = [a[0]]
    while problem.isGoalState(c) == False:
        counter += 1
        if counter == 1:
            for i in problem.getSuccessors(a[0]):
                if i[0] != previous and i[0] not in visited_nodes:
                    b = a + [i]
                    fringe.push(b)
        else:
            for i in problem.getSuccessors(a[-1][0]):
                if i[0] != previous and i[0] not in visited_nodes:
                    b = a + [i]
                    fringe.push(b)
        a = fringe.pop()
        c = a[-1][0]
        visited_nodes.append(c)
        previous = a[-2][0]
    directions = []
    for i in a[1:]:
        directions.append(i[1])
    return directions
    util.raiseNotDefined()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    a = [problem.getStartState()]
    fringe = util.Queue()
    fringe.push((a[0], []))
    visited_nodes = []
    expanded_nodes = a
    while fringe.isEmpty() == False:
        a = fringe.pop()
        visited_nodes.append(a[0])
        if problem.isGoalState(a[0]):
            return a[1]
        b = problem.getSuccessors(a[0])
        for (new_node, new_direction, _) in b:
            if new_node not in visited_nodes and new_node not in expanded_nodes:
                # Do not want to expand twice
                expanded_nodes.append(new_node)
                new_direction = a[1] + [new_direction]
                fringe.push((new_node, new_direction))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    a = [problem.getStartState()] ## gives me (5,5)

    # Use a priority queue for this algorithm
    fringe = util.PriorityQueue()

    # Initial Cost is Zero
    fringe.push((a[0], [], 0), 0)
    visited_nodes = []
    expanded_nodes = [problem.getStartState()]
    while fringe.isEmpty() == False:
        a = fringe.pop()
        visited_nodes.append(a[0])
        if problem.isGoalState(a[0]) == True:
            return a[1]
        b = problem.getSuccessors(a[0])
        for (new_node, new_direction, new_cost) in b:
            if new_node not in visited_nodes and new_node not in expanded_nodes:
                # Do not want to expand twice, was not passing until i write this if statement
                if problem.isGoalState(new_node) != True:
                    expanded_nodes.append(new_node)
                new_direction = a[1] + [new_direction]
                new_cost = a[2] + new_cost
                # Same thing as before but this time we actually use the cost in the fringe
                fringe.push((new_node, new_direction, new_cost), new_cost)
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def foodHeuristic(state, problem):

    unvisited_food = 0

    problem

    for i in range(0, len(state[1])):
        if state[1][i] == 0:
            # Record the corners univisted from that state
            unvisited_food += 1


    return unvisited_food # Default to trivial solution

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""


    a = [problem.getStartState()]
    fringe = util.PriorityQueue()

    # This time we implement an actual heuristic in the priority Queue
    fringe.push((a[0], [], 0), heuristic(a[0], problem))

    visited_nodes = []
    expanded_nodes = [problem.getStartState()]
    while fringe.isEmpty() == False:
        a = fringe.pop()
        visited_nodes.append(a[0])
        if problem.isGoalState(a[0]) == True:
            return a[1]
        b = problem.getSuccessors(a[0])
        for (new_node, new_direction, new_cost) in b:
            if new_node not in visited_nodes and new_node not in expanded_nodes:
                # Do not want to expand twice
                if problem.isGoalState(new_node) != True:
                    expanded_nodes.append(new_node)
                new_direction = a[1] + [new_direction]
                new_cost = a[2] + new_cost
                fringe.push((new_node, new_direction, new_cost), new_cost + heuristic(new_node, problem))
    return []
    util.raiseNotDefined()

def foodHeuristic(state, problem):

    unvisited_food = 0
    min_path = ()
    for i in range(0, state[1]):
        if state[1][i] == 0:
            # Record the corners univisted from that state
            unvisited_food += 1

    # If all corners are visited, return 0 because were done
    return unvisited_food # Default to trivial solution



