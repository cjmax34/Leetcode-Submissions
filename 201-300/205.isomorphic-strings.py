class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashh = {}

        for sc, tc in zip(s, t):
            if sc in hashh:
                if hashh[sc] != tc:
                    return False
            elif tc in hashh.values():
                return False

            hashh[sc] = tc

        return True