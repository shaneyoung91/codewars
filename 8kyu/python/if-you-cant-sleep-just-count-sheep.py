# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


#  My Solution
def count_sheep(n):
    if n == 0:
        return ""
    
    result = ""
    for i in range(1, n+1):
        result += f"{i} sheep..."
        
    return result