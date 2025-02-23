import heapq


def calculateMaxProcessingThroughput(n, serverTasks):
    costs = {}
    min_cost_i = -1
    min_cost = float("inf")
    heap = []
    heapq.heapify(heap)
    reverse_item = {}
    result = 0
    for i in range(len(serverTasks)):
        from_server = i
        # this is greedy algorithm
        to_server = serverTasks[from_server]
        costs[from_server] = serverTasks[from_server]

        if to_server == from_server:
            result += to_server
            continue

        heapq.heappush(
            heap,
            (
                costs[from_server],
                {"from_server": from_server, "to_server": to_server},
            ),
        )
        reverse_item[to_server] = from_server

    if len(heap) == 0:
        return result

    # we start from the lowest cost
    least_cost_item = heapq.heappop(heap)[1]
    result += least_cost_item["to_server"]

    banned_server = {}
    banned_server[least_cost_item["from_server"]] = True
    if banned_server.get(reverse_item[least_cost_item["from_server"]]) is None:
        result += least_cost_item["from_server"]

    # we can ignore the server that has "to_server"
    while len(heap) > 0:
        item = heapq.heappop(heap)[1]
        # first check if it is banned one
        if banned_server.get(item["to_server"]) is not None:
            continue
        else:
            if banned_server.get(reverse_item[item["from_server"]]) is not None:
                result += item["from_server"]
            banned_server[item["from_server"]] = True
            print(item["to_server"])
            result += item["to_server"]

    print("Result", result)
    return result


if __name__ == "__main__":
    assert calculateMaxProcessingThroughput(3, [0, 1, 2]) == 3
    assert calculateMaxProcessingThroughput(3, [0, 4, 2, 1, 3]) == 9
