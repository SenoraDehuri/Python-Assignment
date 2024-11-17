# =============================================================================
# Twenty students were asked to rate on a scale of 1 to 5 the quality of the food in the student cafeteria, with 1 being "awful" and 5 being "excellent." Place the 20 responses in a list.
# 
# 1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5
# 
# Determine and display the frequency of each rating. Use the built-in (or user-defined) functions and statistics module functions to display the following response statistics: minimum, maximum, range, mean, median, mode, variance and standard deviation
# 
# 
# =============================================================================
import statistics
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
freq=[0]*5
for rating in responses:
    freq[rating-1]+=1
print("Frequency of each rating:")
for i in range(len(freq)):
    print(f"{i + 1}: {freq[i]}")
    
min_rating=min(responses)
max_rating=max(responses)
range_rating=max_rating-min_rating
mean_rating=statistics.mean(responses)
median_rating = statistics.median(responses)
mode_rating = statistics.mode(responses)
variance_rating = statistics.variance(responses)
std_deviation_rating = statistics.stdev(responses)

print("\nStatistics:")
print(f"Minimum: {min_rating}")
print(f"Maximum: {max_rating}")
print(f"Range: {range_rating}")
print(f"Mean: {mean_rating:.2f}")
print(f"Median: {median_rating}")
print(f"Mode: {mode_rating}")
print(f"Variance: {variance_rating:.2f}")
print(f"Standard Deviation: {std_deviation_rating:.2f}")
     
    