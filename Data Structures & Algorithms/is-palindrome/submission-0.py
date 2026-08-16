class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        
        
        for string in s:
            if string.isalnum():
                
                arr.append(string.strip().lower())
                
        if arr==arr[::-1]:
            return True
        else:
            return False