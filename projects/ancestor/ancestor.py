
def earliest_ancestor(ancestors, starting_node):
    stack = []
    visited = set()
    stack.append([starting_node])  # [ [2] ]
    maxList = []
    while len(stack) > 0:
        path = stack.pop()  # [2]
        v = path[-1]  # 2
        if v not in visited:
            visited.add(v)  # { 2 }
            for neighbors in ancestors:
                if v == neighbors[-1]:  # 2 != neighbors.. False
                    current = [*path, neighbors[0]]
                    if len(current) > len(maxList):
                        maxList = [*current]
                    if len(current) == len(maxList):
                        if current[-1] < maxList[-1]:
                            maxList = [*current]
                    stack.append(current)
    # since line 13 is False, maxList never gets updated since it doesnt have a parent.
    if len(maxList) == 0:
        return -1
    return maxList[-1]


"""
Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.


find starting node inside ancestor list


returns their earliest known ancestor – the one at the farthest distance from the input individual.
max = []
if len(current) > len(max):
    max = [*current]

# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
if len(current) == len(max):
    if current[-1] < max[-1]:
        max = [*current]
return max[-1]
"""
