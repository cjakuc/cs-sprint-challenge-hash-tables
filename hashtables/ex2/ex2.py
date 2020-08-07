#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination



def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * (length)
    hash_table = {}
    # hash_table["NONE"] = tickets[tickets.index()].destination
    for t in tickets:
        hash_table[t.source] = t.destination
    dest = hash_table["NONE"]
    i = 0
    while dest != None:
        route[i] = dest
        if dest == "NONE":
            break
        dest = hash_table[dest]
        i += 1

    return route
