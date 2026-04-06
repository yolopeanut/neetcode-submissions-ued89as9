class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Check if is odd or even
        new_str = ''.join(filter(str.isalnum, s)).lower()
        print(new_str)
        for i in range(int(len(new_str)/2)):
            if new_str[i] != new_str[-(i+1)]:
                print(i)
                print(new_str[i],new_str[-i])
                return False
        return True