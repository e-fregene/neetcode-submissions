class Solution:
    def isValid(self, s: str) -> bool:
        """
        U: string of chars, ->Boolean
        P: use a stack to match paies correctly
        I: loop through, adding to stack if valid, then
        check codntions, if failed false
        """

        brack= {')':'(', '}':'{', ']':'['}
        stack=[]
        for x in s:
            if x in brack:
                if stack and stack[-1] == brack[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        
        return len(stack)==0

