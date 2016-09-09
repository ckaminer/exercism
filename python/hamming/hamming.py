def distance(first, second):
    distance = 0
    if len(first) == len(second):
        for idx, val  in enumerate(first):
            if first[idx] != second[idx]:
                distance += 1
    return distance
