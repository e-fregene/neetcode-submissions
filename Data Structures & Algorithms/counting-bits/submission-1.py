class Solution:
    def countBits(self, n: int) -> List[int]:
        binary_representation =[]



# We are given an integer of the amount of ones
# find way to convert interger 
# whats one way to remove all needed if statments
        for one in range(n+1):
            a= one //2

            #if one % 2 == 0 and one != 0:
              #  one = 1
            #if one == 0:
               # one = 0
           # if one % 2 == 1 and one != 1:
               # one = 2
           # if one == 1:
               # one = 1
            binary_representation.append(bin(one).count('1'))
        return binary_representation

        