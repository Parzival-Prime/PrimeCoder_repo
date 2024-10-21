def sorted_squares(nums: list[int]) -> list[int]:
    squares = [x**2 for x in nums]
    squares.sort()
    return squares