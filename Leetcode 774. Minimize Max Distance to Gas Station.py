"""
774. Minimize Max Distance to Gas Station

On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

stations.length will be an integer in range [10, 2000].
stations[i] will be an integer in range [0, 10^8].
K will be an integer in range [1, 10^6].
Answers within 10^-6 of the true value will be accepted as correct.
"""

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        import math

        dist = [stations[i] - stations[i-1] for i in range(1, len(stations))]
        lo, hi = 0.0, 10 ** 8
        while hi - lo >= 1e-6:
            mid = (lo + hi) / 2
            cnt = 0
            for d in dist:
                cnt += math.ceil(d / mid) - 1
            if cnt > K:
                lo = mid
            else:
                hi = mid
        return lo