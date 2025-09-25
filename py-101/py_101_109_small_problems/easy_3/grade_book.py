# Write a function that determines the mean (average) of the three scores passed to it, 
# and returns the letter associated with that grade.

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'
# Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.

def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def get_grade(score1, score2, score3):
    average = calculate_average(score1, score2, score3)
    match average // 10:
        case 9 | 10:
            return 'A'
        case 8:
            return 'B'
        case 7:
            return 'C'
        case 6:
            return 'D'
        case _:
            return 'F'
        
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True