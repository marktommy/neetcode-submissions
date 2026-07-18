class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = {} # resets after each word
            for letter in word:
                counts[letter] = counts.get(letter, 0) + 1 # counts how many letters there are in each word
            signature = tuple(sorted(counts.items())) # sorts counts so "eat" and "tea" would be identical
            groups.setdefault(signature, []).append(word)
        return list(groups.values())