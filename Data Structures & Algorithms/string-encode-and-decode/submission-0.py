class Solution:

    def encode(self, strs: List[str]) -> str:
        numelements = len(strs)
        str = ""
        for word in strs:
            str += ";"
            str += word
        return str

    def decode(self, s: str) -> List[str]:
        thelist = []
        i = -1
        for char in s:
            if char == ";":
                thelist.append("")
                i+=1
            else:
                thelist[i] += char
        return thelist
            
