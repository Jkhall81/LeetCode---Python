from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)

    top_k = count.most_common(k)

    return [num for num, freq in top_k]


# no collections
def topKFrequent(nums: list[int], k: int) -> list[int]:
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return [num for num, freq in sorted_items[:k]]


# bucket sort
def topKFrequent(nums: list[int], k: int) -> list[int]:
    counts= {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) -1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result