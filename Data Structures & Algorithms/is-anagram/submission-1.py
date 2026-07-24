class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arrayt = {}
        arrays = {}
        for letter in range(len(s)):
            arrays[s[letter]] = 1 + arrays.get(s[letter],0)
            arrayt[t[letter]] = 1 + arrayt.get(t[letter],0)
        return arrays == arrayt

        