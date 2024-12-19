def isVowel(ch) -> bool: 
    # Make the list of vowels 
    str = "aeiouAEIOU"
    return (str.find(ch) != -1) 

def reverseVowels(s: str) -> str:
    chars=list(s)
    i=0
    j=len(chars)-1
    while i<j:
        while(i<j and not isVowel(chars[j])):
            j-=1
        
        while(i<j and not isVowel(chars[i])):
            i+=1

        if i<j:
            chars[i],chars[j]=chars[j],chars[i]
            i+=1
            j-=1

    return ''.join(chars) 

s = "IceCreAm"
print(reverseVowels(s))