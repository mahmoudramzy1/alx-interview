#!/usr/bin/python3
"""module for solve lock boxes problem"""
import queue


def canUnlockAll(boxes):
    """function to solve this problem"""
    if not boxes:
        return False
    if not boxes[0]:
        return False
    if len(boxes) == 1:
        return True

    keys = set(boxes[0])
    q = queue.Queue()  # Correct usage of queue.Queue
    q.put(0)
    visited = set()
    visited.add(0)  # Use 'add' instead of 'put' to add to a set

    while not q.empty():
        box = q.get()
        for key in boxes[box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                q.put(key)
                keys.add(key)

    return len(visited) == len(boxes)
