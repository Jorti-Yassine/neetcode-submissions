class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "EmptyTable404"
        return ";".join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="EmptyTable404":
            return []
        if not s:
            return [""]
        return s.split(";")
