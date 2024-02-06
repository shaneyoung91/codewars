# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

# Constraint:
    # 1 <= month <= 12


# My Solution
def quarter_of(month):
    if month <= 3:
        return 1
    elif month > 3 and month <= 6:
        return 2
    elif month > 6 and month <= 9:
        return 3
    elif month > 9 and month <= 12:
        return 4