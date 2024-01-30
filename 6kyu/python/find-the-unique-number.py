# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.


# My Solution
from collections import Counter

def find_uniq(arr):
    # Use Counter method
    # Access key-value pairs using items method
    # Return key with value == 1
    
    hashmap = Counter(arr)
    
    for key, value in hashmap.items():
        if value == 1:
            return key
        