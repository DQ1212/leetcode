class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            flag = 1
        else:
            flag = -1
            x= x*-1
            
        x_reverse = int(str(x)[::-1])*flag
        if x_reverse > 2147483647 or x_reverse < -2147483648:
            return 0
        else:
            return x_reverse
