import bisect

class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = ([], [])
        self.timemap[key][0].append(timestamp)
        self.timemap[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        times, vals = self.timemap[key]
        idx = bisect.bisect_right(times, timestamp)
        
        if idx == 0:
            return ""
        
        return vals[idx - 1]
