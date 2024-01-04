def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

# Test cases
print(compare(5, 4))  # Should print 1
print(compare(7, 7))  # Should print 0
print(compare(2, 3))  # Should print -1
print(compare(42, 1)) # Should print 1
