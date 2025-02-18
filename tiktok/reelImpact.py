# lined list problem
class Node:
    def __init__(self, prev, next, item, count):
        self.prev = prev
        self.next = next
        self.item = item
        self.count = count


def getTotalImpact(initialReelImpacts, newReelImpacts, k):
    m = len(initialReelImpacts)
    n = len(newReelImpacts)
    sorted_init = sorted(initialReelImpacts)
    result = 0

    prev = None
    item_dict: dict[int, Node] = {}
    highest_node = None
    for item in sorted_init:
        if item_dict.get(item) is None:
            node = Node(prev, None, item, 1)
            if prev is not None:
                item_dict[prev.item].next = node
            item_dict[item] = node
            prev = node
            highest_node = node
        else:
            item_dict[item].count += 1

    target_node = highest_node
    for i in range(k - 1):
        target_node = target_node.prev

    result += target_node.item
    for i in range(n):
        new_impact = newReelImpacts[i]
        if new_impact < target_node.item:
            result += target_node.item
            continue
        new_impact_node = item_dict.get(new_impact)
        if new_impact_node is not None:
            # we do not need to check if there is already the item
            continue
        else:
            new_impact_node = Node(None, None, new_impact, 1)
            # now we should set the prev and next
            before_node = target_node
            next_node = target_node.next
            while next_node is not None:
                if next_node.item > new_impact:
                    break
                before_node = next_node
                next_node = next_node.next
            before_node.next = new_impact_node
            if next_node is not None:
                next_node.prev = new_impact_node
            new_impact_node.prev = before_node
            new_impact_node.next = next_node
            target_node = target_node.next

        result += target_node.item
    return result


if __name__ == "__main__":
    assert getTotalImpact([2, 3], [4, 5, 1], 2) == 13
