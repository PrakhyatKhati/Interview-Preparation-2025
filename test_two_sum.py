from two_sum import two_sum


def test_basic_case():
	assert two_sum([2, 7, 11, 15], 9) in ([0, 1], [1, 0])


def test_multiple_solutions_but_any_valid_ok():
	# For [1,5,3,3] target 6, either (0,2) or (0,3) is valid depending on scan order.
	assert two_sum([1, 5, 3, 3], 6) in ([0,1],[0, 2], [0, 3])


def test_duplicates():
	assert two_sum([3, 3], 6) in ([0, 1], [1, 0])


def test_no_solution_returns_none():
	assert two_sum([1, 2, 3], 100) is None


def test_negative_numbers():
	assert two_sum([-3, 4, 3, 90], 0) in ([0, 2], [2, 0])

