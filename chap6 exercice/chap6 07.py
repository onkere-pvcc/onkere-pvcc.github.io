def to_secs(hours, minutes, seconds):
    if hours >= 0 and minutes >= 0 and seconds >= 0:
        return hours * 3600 + minutes * 60 + seconds
    else:
        return hours * 3600 - minutes * 60 - abs(seconds)

# Test cases
print(to_secs(2, 30, 10))     # Should print 9010
print(to_secs(2, 0, 0))       # Should print 7200
print(to_secs(0, 2, 0))       # Should print 120
print(to_secs(0, 0, 42))      # Should print 42
print(to_secs(0, -10, 10))    # Should print -590
