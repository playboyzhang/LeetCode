# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:

# 输入: 121
# 输出: true
# 示例 2:

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。




# 将整数转化为字符串，然后反向排序进行比较
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >=0:
            y = str(x)[::-1]
            if int(x)== int(y):
                return True
            else:
                return False
        else:
                return False

# 直接对整数处理，不转化为字符串
class Solution:
    def isPalindrome(self, x):
      
        if x < 0:
            return False
        else:
            length = len(str(x))
            Y = 0
            y = x
            while x!= 0:
                Y = Y + (x % 10) * 10** (length-1)
                x = x // 10
                length = length - 1
            if Y == y:
                return True
            else:
                return False