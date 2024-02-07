# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.

# Example:
    # h = 0
    # m = 1
    # s = 1

    # result = 61000

# Input constraints:
    # 0 <= h <= 23
    # 0 <= m <= 59
    # 0 <= s <= 59


#  My Solution
def past(h, m, s):
    # 1 second == 1,000 milliseconds
    # 1 minute = 60,000 milliseconds
    # 1 hour == 3,600,000 milliseconds
    
    milliseconds = (s * 1000) + (m * 60000) + (h * 3600000)
    
    return milliseconds