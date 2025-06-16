class Solution(object):
    def isSubsequence(self, s, t):
        t_index=0
        for char in s:
            t_index=t.find(char,t_index)
            if t_index==-1:
                return False
            t_index+=1
        return True