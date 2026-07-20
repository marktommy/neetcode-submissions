class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []
        for item in nums:
            hashmap[item] = hashmap.get(item, 0) + 1
        sortedhash = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            output.append(sortedhash[i][0])
        return(output)  
