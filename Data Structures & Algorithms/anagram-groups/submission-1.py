class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_dic = defaultdict(list)
        for s in strs:
            ana="".join(sorted(s))
            counter_dic[ana].append(s)
        res=[]
        for v in counter_dic.values():
            res.append(v)
        return res