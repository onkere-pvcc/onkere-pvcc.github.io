def add_vectors(u, v):
    # Check if the input lists have the same length
    if len(u) != len(v):
        raise ValueError("Input lists must have the same length")

    # Initialize an empty list to store the sums of corresponding elements
    result = []

    # Calculate the sum of corresponding elements and append to the result list
    for i in range(len(u)):
        result.append(u[i] + v[i])

    return result

from vectors import add_vectors

def test(actual, expected):
    assert actual == expected, f"Expected: {expected}, but got: {actual}"

# Test cases
test(add_vectors([1, 1], [1, 1]), [2, 2])
test(add_vectors([1, 2], [1, 4]), [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]), [2, 6, 4])
