class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp can be ignored
        # new_node = TimestampNode(value, timestamp)
        if self.data.get(key) is None:
            self.data[key] = {"time": [timestamp], "value": [value]}
        else:
            item = self.data[key]  # root
            item["time"].append(timestamp)
            item["value"].append(value)

    def get(self, key: str, timestamp: int) -> str:
        # we conduct a binary search on [key]["time"]
        if self.data.get(key) is None:
            return ""

        item = self.data[key]
        times = item["time"]
        values = item["value"]
        low = 0
        high = len(times) - 1

        while low < high:
            mid = (low + high + 1) // 2
            time = times[mid]

            if timestamp == time:
                low = mid
                break
            elif timestamp > time:
                low = mid
            else:
                high = mid - 1

        if timestamp < times[0]:
            return ""

        return values[low]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == "__main__":
    map1 = TimeMap()
    map1.set("foo", "bar", 1)
    assert map1.get("foo", 1) == "bar"
    assert map1.get("foo", 3) == "bar"
    map1.set("foo", "bar2", 4)
    assert map1.get("foo", 4) == "bar2"
    assert map1.get("foo", 5) == "bar2"

    map2 = TimeMap()
    map2.set("love", "high", 10)
    map2.set("love", "low", 20)
    assert map2.get("love", 5) == ""
    assert map2.get("love", 10) == "high"
    assert map2.get("love", 15) == "high"
    assert map2.get("love", 20) == "low"
    assert map2.get("love", 25) == "low"
