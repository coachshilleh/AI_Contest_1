



# myAgents.py
# ---------------
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

from game import Agent
from searchProblems import PositionSearchProblem
from game import Directions
from game import Actions

import util
import time
import search



def createAgents(num_pacmen, agent='MyAgent'):
    global a
    a = [0 for i in range(0, num_pacmen)]
    global path
    path = [[] for i in range(0, num_pacmen)]
    global number
    number = num_pacmen
    return [eval(agent)(index=i) for i in range(num_pacmen)]


class MyAgent(Agent):

    def findPathToClosestDot(self, gameState):
        FOOD = gameState.getFood()
        print(FOOD)
        if path[self.index] == []:
            startState = gameState.getPacmanPosition(self.index)
            if number < 2:
                problem = AnyFoodSearchProblem2(gameState, self.index, a, FOOD, startState)
                path[self.index] = breadthFirstSearch(problem)
            else:
                problem = AnyFoodSearchProblem(gameState, self.index, a, FOOD, startState)
                path[self.index] = breadthFirstSearch(problem)
        elif FOOD[a[self.index][0]][a[self.index][1]] is False:
            startState = gameState.getPacmanPosition(self.index)
            problem = AnyFoodSearchProblem(gameState, self.index, a, FOOD, startState)
            path[self.index] = breadthFirstSearch(problem)
        if path[self.index] == []:
            problem2 = AnyFoodSearchProblem2(gameState, self.index, a, FOOD, startState)
            path[self.index] = breadthFirstSearch(problem2)
        return path[self.index].pop(0)


    def getAction(self, state):
        return self.findPathToClosestDot(state)


"""
Put any other SearchProblems or search methods below. You may also import classes/methods in
search.py and searchProblems.py. (ClosestDotAgent as an example below)
"""

class AnyFoodSearchProblem(PositionSearchProblem):


    def __init__(self, gameState, agentIndex, current_goals, food, SS):

        self.food = food
        self.current_goals = current_goals
        self.other_goals = [self.current_goals[i] for i in range(0, number) if i != agentIndex]
        self.walls = gameState.getWalls()
        self.agentIndex = agentIndex
        self.startState = SS
        self.costFn = lambda x: 1
        self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

    def isGoalState(self, state) :

        x, y = state
        if self.food[x][y]:
            if (x,y) not in self.other_goals:
                a[self.agentIndex] = (x,y)
                return True
        return False

class AnyFoodSearchProblem2(PositionSearchProblem):


    def __init__(self, gameState, agentIndex, current_goals, food, SS):

        self.food = food
        self.current_goals = current_goals
        self.walls = gameState.getWalls()
        self.agentIndex = agentIndex
        self.startState = SS
        self.costFn = lambda x: 1
        self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

    def isGoalState(self, state) :

        x, y = state
        if self.food[x][y]:
            a[self.agentIndex] = (x,y)
            return True
        return False

def breadthFirstSearch(problem):

    a = [problem.getStartState()]
    fringe = util.Queue()
    fringe.push((a[0], []))
    visited_nodes = []
    expanded_nodes = a
    while fringe.isEmpty() is False:
        a = fringe.pop()
        visited_nodes.append(a[0])
        if problem.isGoalState(a[0]):
            return a[1]
        b = problem.getSuccessors(a[0])
        for (new_node, new_direction, _) in b:
            if new_node not in visited_nodes:
                if new_node not in expanded_nodes:
                # Do not want to expand twice
                    expanded_nodes.append(new_node)
                    new_direction = a[1] + [new_direction]
                    fringe.push((new_node, new_direction))
    return []



