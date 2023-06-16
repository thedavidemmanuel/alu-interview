#!/usr/bin/python3
"""
    Python script that calculates how much water is retained after it rains
"""


def rain(walls):
    """
        Function that calculates how much water will be retained after it rains
        Return:
            int: amount of rainwater collected
    """
    if not walls:
        return 0

    water_collected = 0
    left, right = 0, len(walls) - 1
    max_left, max_right = walls[left], walls[right]

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] > max_left:
                max_left = walls[left]
            else:
                water_collected += max_left - walls[left]
            left += 1
        else:
            if walls[right] > max_right:
                max_right = walls[right]
            else:
                water_collected += max_right - walls[right]
            right -= 1

    return water_collected

