def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    for i, x in enumerate(weights):
        if x in hash_table and limit == 2*x:
            return (i, hash_table[x])
        if limit-x in hash_table:
            # hash_table[x] = i
            if hash_table[limit-x] >= i:
                return (hash_table[limit-x],i)
            elif hash_table[limit-x] < i:
                return (i,hash_table[limit-x])
        else:
            hash_table[x] = i

    return None
