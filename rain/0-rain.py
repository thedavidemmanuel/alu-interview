#!/usr/bin/python3
def rain(walls):
    """Calculates the amount of water retained after it rains.

    Args:
        walls: A list of non-negative integers representing the heights of walls with unit width 1.

    Returns:
        Integer indicating total amount of rainwater retained.
    """

    # Initialize the amount of water retained
    water = 0

    # Iterate through the walls
    for i in range(1, len(walls) - 1):
        # Find the highest wall to the left and right of the current wall
        left_wall = max(walls[:i])
        right_wall = max(walls[i + 1:])

        # Calculate the amount of water that can be retained by the current wall
        water += min(left_wall, right_wall) - walls[i]

    return water

