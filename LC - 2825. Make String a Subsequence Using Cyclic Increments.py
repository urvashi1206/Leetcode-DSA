# You are given two 0-indexed strings str1 and str2.

# In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

# Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

# Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

def canMakeSubsequence(str1: str, str2: str) -> bool:
    i=0
    j=0
    while(i<len(str1) and j<len(str2)):
        current_char=str1[i]
        if(current_char=='z'):
            next_char='a'
        else:
            next_char=chr(ord(str1[i])+1)
        if(str2[j]==current_char or str2[j]==next_char):
            j+=1
        i+=1

    if(j==len(str2)):
        return True
    else:
        return False
            

str1="abc"
str2="ad"
print(canMakeSubsequence(str1,str2))