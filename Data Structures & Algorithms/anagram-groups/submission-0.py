class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_dic = {}
        for s in strs:
            ana="".join(sorted(s))
            if ana in counter_dic:
                counter_dic[ana]=counter_dic[ana]+"*"+s
            else:
                counter_dic[ana]=s
        res=[]
        for v in counter_dic.values():
            res.append(v.split("*"))
        return res