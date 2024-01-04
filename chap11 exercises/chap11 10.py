def replace(s, old, new):
    # Split the string into parts using the old string as the delimiter
    parts = s.split(old)
    # Join the parts using the new string as the delimiter
    result = new.join(parts)
    return result

def test(actual, expected):
    assert actual == expected, f"Expected: {expected}, but got: {actual}"

# Test cases
test(replace("Mississippi", "i", "I"), "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am"), "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a"), "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
