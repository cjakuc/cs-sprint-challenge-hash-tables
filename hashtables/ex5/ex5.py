# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result = []
    for q in queries:
        hash_table[q] = ""
    for f in files:
        count = f.count("/")
        f_name = f.split('/', count)
        f_name = f_name[-1]
        if f_name in hash_table:
            result.append(f)


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
