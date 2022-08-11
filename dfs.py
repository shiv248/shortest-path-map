#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# Shivanshu Gupta - Oct 5th, 2021
#


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    rootNode = Node(problem.start) #head of the search tree

    if (problem.is_goal(rootNode.loc)): #if the head is already the solution
        return rootNode

    sett = Frontier(rootNode, True) #make a Frontier of the rootNode
    if (repeat_check):
        reachedSet = list()
        reachedSet.append(rootNode.loc) #create a new set of states we have looked at

    while(not(sett.is_empty())): #go through and get the elements
        takenNode = sett.pop()

        if (problem.is_goal(takenNode.loc)): #if that node is the answer
            return takenNode

        explored = takenNode.expand(problem) #if its not we check against other nodes we already know
        for i in explored:
            if (repeat_check):
                if (not(reachedSet.__contains__(i.loc))): #if its not already in it, we add it to both sets
                    sett.add(i)
                    reachedSet.append(i.loc)
            else:
                sett.add(i)

    return None
