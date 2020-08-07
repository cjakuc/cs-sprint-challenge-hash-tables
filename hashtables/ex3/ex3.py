def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    for lst in arrays:
        for num in lst:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
    result = []
    for k, v in hash_table.items():
        if v == len(arrays):
            result.append(k)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
