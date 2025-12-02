# define a function called categorize_rating that thakes a list of customer ratings as input.
# Each rating is a whole number between 1 and 10.  The function will categorized low 1-4, medium 5-7 and High 8-10
# Print output with three statements from low to high.

def categorize_ratings(rating_list): 
    low = 0 
    medium = 0 
    high = 0 
 
    for rating in rating_list: 
        if 1 <= rating <= 4: 
            low += 1 
        elif 5 <= rating <= 7: 
            medium += 1 
        elif 8 <= rating <= 10: 
            high += 1 
 
    print(f"Low: {low}") 
    print(f"Medium: {medium}") 
    print(f"High: {high}") 

categorize_ratings([1, 3, 5, 7, 8, 9])
print("Expected Output:\nlow: 2\nMedium: 2\High: 2")
)
