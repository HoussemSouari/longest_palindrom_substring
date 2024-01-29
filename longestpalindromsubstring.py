
def around_center(s:str, left:int, right:int) -> str :
    while left >=0 and right < len(s) and s[left] == s[right] :
        left -=1
        right += 1
    return s[left+1:right] 

def longestpalindrom(s:str) -> str :
        longest= ""
        for i in range(len(s)):
            #even length
            even_length = around_center(s, i, i+1)
            #odd length 
            odd_length = around_center(s, i, i)
            if len(odd_length) > len(longest) :
                longest = odd_length
            if len(even_length) > len(longest) :
                longest = even_length
        return longest 

