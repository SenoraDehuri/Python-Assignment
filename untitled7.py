# =============================================================================
# Write a python function that takes a tuple of tuples and prints the sum of all numeric elements in the inner tuples
# =============================================================================
def sum_numeric_elements(tuples):
    total_sum = 0
    for inner_tuple in tuples:
        for element in inner_tuple:
            if isinstance(element, (int, float)):  # Check if the element is numeric
                total_sum += element
    print("Sum of all numeric elements:", total_sum)


example_tuple = ((1, 2, 'a'), (3.5, 'b', 4), (5, 6, 7))
sum_numeric_elements(example_tuple)