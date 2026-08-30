class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # String s, uppercase letters. int k(choose k chars)

        # return len(longest subsrting) - max(dict vals)

        #keep track of current char replace with that k times, and count


        res=0
        chars={}

        l=0
        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)

            while (r-l+1) - max(chars.values()) > k:
                chars[s[l]] -=1
                l+=1

            res =  max(res, r-l+1)

        return res


        