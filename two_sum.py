from typing import List, Optional


def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
	"""Return indices of the two numbers such that they add up to target.

	Uses a single-pass hash map storing value -> index.
	Runs in O(n) time and O(n) extra space.
	"""
	value_to_index: dict[int, int] = {}
	for index, number in enumerate(nums):
		complement = target - number
		if complement in value_to_index:
			return [value_to_index[complement], index]
		value_to_index[number] = index

	return None


if __name__ == "__main__":
	# Simple demo runs
	cases = [
		{"nums": [2, 7, 11, 15], "target": 9, "expect_any": [[0, 1]]},
		{"nums": [3, 2, 4], "target": 6, "expect_any": [[1, 2]]},
		{"nums": [3, 3], "target": 6, "expect_any": [[0, 1]]},
		{"nums": [1, 5, 3, 3], "target": 6, "expect_any": [[0, 2], [0, 3]]},
	]

	for i, case in enumerate(cases, start=1):
		result = two_sum(case["nums"], case["target"])
		ok = result in case["expect_any"]
		print(f"case {i}: nums={case['nums']} target={case['target']} -> {result} | ok={ok}")

