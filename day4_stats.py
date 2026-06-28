def day4_stats(numbers):
    if not numbers:
        return None, None, None
    #1. calculate mean
    mean = sum(numbers) / len(numbers)
    #2. calculate median
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) % 2 ==0 :
        median = (sorted_numbers[len(sorted_numbers) // 2 - 1] + sorted_numbers[len(sorted_numbers) // 2]) / 2
    else:
        median = sorted_numbers[len(sorted_numbers) // 2]
    #3. calculate mode
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    max_count = max(counts.values())
    # Handle case where all numbers appear equally
    if max_count == 1 and len(numbers) > 1:
        modes = []  # No unique mode
    else:
        modes = [k for k, v in counts.items() if v == max_count]

    return mean, median, modes
# 1. Ask the user to type numbers
user_input = input("Enter numbers separated by spaces: ")
# 2. Turn those typed words into a list of numbers
user_data = [float(x) for x in user_input.split()]
# Send their data to the function
mean_val, median_val, mode_val = day4_stats(user_data)

# Print the answers
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")