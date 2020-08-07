def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result = []
    for i, x in enumerate(a):
        if abs(x) in hash_table:
            result.append(abs(x))
        else:
            hash_table[abs(x)] = i
    
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
