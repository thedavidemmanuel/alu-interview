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


def main():
    # Test cases
    walls = []
    assert rain(walls) == 0

    walls = [2, 0, 2]
    assert rain(walls) == 4

    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    assert rain(walls) == 6

    walls = [1, 1, 2, 0, 1, 1, 1]
    assert rain(walls) == 3

    walls = [0, 2, 1, 0, 1, 3, 1, 2, 1, 1, 2, 1]
    assert rain(walls) == 10

    walls = [2, 0, 0, 0, 0, 3, 0]
    assert rain(walls) == 6

    walls = [1]
    assert rain(walls) == 0

    walls = [3, 3]
    assert rain(walls) == 6


if __name__ == "__main__":
    main()

