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
    
print(reverse_ascending([1, 2, 3, 4, 5]))  
print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))  
print(reverse_ascending([5, 4, 3, 2, 1]))  
print(reverse_ascending([])) 
