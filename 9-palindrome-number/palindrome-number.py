class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            y = str(x)
            r_lst = []
            for i in range(len(y)-1, -1,-1):
                r_lst.append(y[i])
            num = int("".join(r_lst))
            if num != x:
                return False
            else:
                return True
        