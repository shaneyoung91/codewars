# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
    # high_and_low("1 2 3 4 5")  # return "5 1"
    # high_and_low("1 2 -3 4 5") # return "5 -3"
    # high_and_low("1 9 3 4 -5") # return "9 -5"

# Notes
    # All numbers are valid Int32, no need to validate them.
    # There will always be at least one number in the input string.
    # Output string must be two numbers separated by a single space, and highest number is first.
    

# My Solution
def high_and_low(numbers):
    split_num = numbers.split()
    
    for i in range(0, len(split_num)):
        split_num[i] = int(split_num[i])
    
    sort_num = sorted(split_num)
    max_num = str(max(sort_num))
    min_num = str(min(sort_num))
    
    return max_num + " " + min_num