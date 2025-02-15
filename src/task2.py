#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Рассмотрим задачу поиска информации в иерархических структурах данных,
например, в файловой системе, где каждый каталог может содержать подкаталоги
и файлы. Алгоритм итеративного углубления идеально подходит для таких задач,
поскольку он позволяет исследовать структуру данных постепенно, углубляясь на
один уровень за раз и возвращаясь, если целевой узел не найден. Для этого
необходимо:
Построить дерево, где каждый узел представляет каталог в файловой
системе, а цель поиска — определенный файл.
Найти путь от корневого каталога до каталога (или файла), содержащего
искомый файл, используя алгоритм итеративного углубления.
"""


from problem import Problem
from problem import iterative_deepening_search as ids
from problem import path_states


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
        actions = []
        for child in state.children:
            actions.append(child.value)
        return actions

    def result(self, state, action):
        for child in state.children:
            if child.value == action:
                return child
        return None

    def is_goal(self, state):
        return state.value == self.goal

    def action_cost(self, s, a, s1):
        return 1

    def h(self, node):
        return 0

    def __str__(self):
        return f"Problem({self.initial}, {self.goal})"


def main():
    root = TreeNode("dir1")
    root.add_child(TreeNode("dir2"))
    root.add_child(TreeNode("dir3"))
    root.children[0].add_child(TreeNode("file4"))
    root.children[1].add_child(TreeNode("file5"))
    root.children[1].add_child(TreeNode("file6"))
    root.children[1].add_child(TreeNode("dir4"))
    root.children[1].children[2].add_child(TreeNode("file7"))

    goal = "file7"

    problem = FilesProblem(initial=root, goal=goal)

    result = ids(problem)

    if result:
        path = [i.value for i in path_states(result)]
        print(f"{' -> '.join(path)}")
    else:
        print(f"Файл {goal} не найден.")


if __name__ == "__main__":
    main()
