class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))
            encoded_string += '#'
            encoded_string += word
        return encoded_string
    #.  5#Hello5#World
    def decode(self, s: str) -> List[str]: 
        decoded_strs= []
        x=0
        while x < len(s):
            y=x
            while s[y] != '#':
                y+=1
            length = int(s[x:y]) # Extract word length

            y+=1 # move y to start of word
            word = s[y:y+length]
            x = y + length # +y to account for word lentgh and #
            decoded_strs.append(word)
            

        return decoded_strs




"""
Encoded starts off as List of strings, Want to Tranform to indvidual strings

Decoded should transform string back into list with same og format

** NEed way to remember each complete word)

Implimenting: Since starting off as list, itertating through keeps record 
of everything we need to know. So we can track length

Ex: [Hello, WOrld]

"#5Hello, #5World" 

"""