def reverse_ascending(numbers):
    if not numbers:  #  if the list is empty
        return []
    
    result = []  
    temp_subseq = [numbers[0]]  # Initialize the first element
    
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:  # Check if the current number is greater than the previous one
            temp_subseq.append(numbers[i])  # If so, it's part of an ascending subsequence
        else:
            # If not, the current ascending subsequence end here, so reverse and append it to the result
            
            result.extend(temp_subseq[::-1])
            temp_subseq = [numbers[i]]  # Start a new subsequence with the current number
    
    # add the last subsequence after exiting the loop
    result.extend(temp_subseq[::-1])
    
    return result

# ask user to enter number by separate by space
user_input = input("Enter a list of numbers separated by space: ")
nums = user_input.split() # split each number
for num in  range(len(nums)):

    nums[num] = int(nums[num])

     #Convert the input string to a list of integers

print(reverse_ascending(nums))
