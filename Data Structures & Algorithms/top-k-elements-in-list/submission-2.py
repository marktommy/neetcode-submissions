class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for item in nums:
            hashmap[item] = hashmap.get(item, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in hashmap.items():
            buckets[freq].append(num)
        print(buckets)

        output = []
        for freq in range(len(buckets) - 1, 0, -1): # goes through items in bucket from highest index, increment by -1
            for num in buckets[freq]: # there might by multiple numbers in each bucket
                output.append(num)
                if len(output) == k: 
                    return output
        
