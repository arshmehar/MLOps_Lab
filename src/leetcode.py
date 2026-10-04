#Leetcode 2sum, sorted2sum and 3sum problem.

def validate_nums(nums):
    """
    Checks that nums is a list of numbers.
    Raises:
        ValueError: If nums is not a list or has non-numeric values.
    """
    if not isinstance(nums, list):
        raise ValueError("Input must be a list.")
    for n in nums:
        if not isinstance(n, (int, float)):
            raise ValueError("All elements must be numbers.")


def two_sum(nums, target):
    """
    Finds indices of two numbers that add up to target (LeetCode #1).
    Uses a hash map for O(n) time.
    Args:
        nums (list): List of numbers.
        target (int/float): Target sum.
    Returns:
        list: [i, j] indices of the two numbers, or [] if no pair exists.
    """
    validate_nums(nums)
    seen = {}  # value -> index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []


def two_sum_sorted(nums, start, target):
    """
    Finds all unique pairs in a sorted list (from index start onward)
    that add up to target. Uses two pointers.
    Args:
        nums (list): Sorted list of numbers.
        start (int): Index to start searching from.
        target (int/float): Target sum.
    Returns:
        list: List of [a, b] pairs with a <= b, no duplicates.
    """
    pairs = []
    left, right = start, len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            right -= 1
            # skip duplicates so each pair appears once
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif current < target:
            left += 1
        else:
            right -= 1

    return pairs


def three_sum(nums, target=0):
    """
    Finds all unique triplets that add up to target (LeetCode #15).
    Sorts the list, fixes one number, then uses two_sum_sorted
    on the rest. O(n^2) time.
    Args:
        nums (list): List of numbers.
        target (int/float): Target sum (default 0, as in LeetCode).
    Returns:
        list: List of [a, b, c] triplets in ascending order, no duplicates.
    """
    validate_nums(nums)
    nums = sorted(nums)  # sorted copy, so the input list is not changed
    result = []

    for i in range(len(nums) - 2):
        # skip duplicate fixed numbers so triplets aren't repeated
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for a, b in two_sum_sorted(nums, i + 1, target - nums[i]):
            result.append([nums[i], a, b])

    return result
