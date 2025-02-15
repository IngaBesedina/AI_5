#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from problem import Problem
from problem import iterative_deepening_search as ids


"""
Представьте себе систему управления доступом, где каждый пользователь
представлен узлом в дереве. Каждый узел содержит уникальный идентификатор
пользователя. Ваша задача — разработать метод поиска, который позволит
проверить существование пользователя с заданным идентификатором в системе,
используя структуру дерева и алгоритм итеративного углубления.
"""


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


class UsersProblem(Problem):
    def __init__(self, initial=None, goal=None, **kwds):
        self.__dict__.update(initial=initial, goal=goal, **kwds)

    def actions(self, state):
        """Возвращает возможные действия на текущем узле."""
        actions = []
        if state.left:
            actions.append("go_left")
        if state.right:
            actions.append("go_right")
        return actions

    def result(self, state, action):
        """Возвращает новый узел после выполнения действия."""
        if action == "go_left":
            return state.left
        elif action == "go_right":
            return state.right

    def is_goal(self, state):
        """Проверяет, является ли текущий узел целевым."""
        return state.value == self.goal

    def action_cost(self, s, a, s1):
        return 1

    def h(self, node):
        return 0

    def __str__(self):
        return f"Problem({self.initial}, {self.goal})"


def main():
    root = BinaryTreeNode(1)
    left_child = BinaryTreeNode(2)
    right_child = BinaryTreeNode(3)
    root.add_children(left_child, right_child)
    right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))
    left_child.add_children(BinaryTreeNode(6), BinaryTreeNode(7))

    goal = 8

    problem = UsersProblem(initial=root, goal=goal)

    result = ids(problem)

    if result:
        print(bool(result))
        print(f"Пользователь с id {goal} найден")
    else:
        print(bool(result))
        print(f"Пользователь с id {goal} не найден")


if __name__ == "__main__":
    main()
