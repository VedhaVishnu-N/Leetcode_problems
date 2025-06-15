class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        lst=list(map(str,s.split(" ")))
        return len(lst[-1])
        