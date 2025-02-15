#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поиск файла с определённым расширением. В файловом дереве
существует множество файлов с разными расширениями. Найти все файлы с
расширением .log , используя алгоритм итеративного углубления.
Ограничение: дерево содержит не менее 10 уровней.
"""
import math
import sys

from problem import Node, Problem, expand, is_cycle, path_states


LIFOQueue = list
failure = Node("failure", path_cost=math.inf)
cutoff = Node("cutoff", path_cost=math.inf)


class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.value}>"


class FilesProblem(Problem):
    def __init__(self, initial=None, goal=None, **kwds):
        self.__dict__.update(initial=initial, goal=goal, **kwds)

    def actions(self, state):
        return [child.value for child in state.children]

    def result(self, state, action):
        for child in state.children:
            if child.value == action:
                return child
        return None

    def is_goal(self, state):
        return state.value.endswith(self.goal)

    def __str__(self):
        return f"Problem({self.initial}, {self.goal})"


def dls(problem: Problem, limit=10):
    frontier = LIFOQueue([Node(problem.initial)])
    result = failure

    result_path = []
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            result_path.append(path_states(node))
        elif len(node) >= limit:
            result = cutoff
        elif not is_cycle(node):
            for child in expand(problem, node):
                frontier.append(child)

    if result == failure:
        return result_path
    return result


def ids(problem):
    for limit in range(1, sys.maxsize):
        result = dls(problem, limit)
        if result != cutoff:
            return result


def main():
    root = TreeNode("dir1")

    current = root
    for i in range(2, 11):
        new_dir = TreeNode(f"dir{i}")
        current.add_child(new_dir)
        current = new_dir

    root.children[0].add_children(TreeNode("file1.txt"), TreeNode("log1.log"))
    root.children[0].children[0].add_children(
        TreeNode("file2.doc"), TreeNode("log2.log")
    )
    root.children[0].children[0].children[0].add_child(TreeNode("log3.log"))
    root.children[0].children[0].children[0].children[0].add_child(
        TreeNode("log4.log")
    )

    problem = FilesProblem(initial=root, goal=".log")
    result = ids(problem)

    if result:
        for path in result:
            p = [i.value for i in path]
            print(f"{' -> '.join(p)}")
    else:
        print("Файлы с расширением .log не найдены.")


if __name__ == "__main__":
    main()
