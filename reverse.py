# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:

# 输入: 123
# 输出: 321
#  示例 2:

# 输入: -123
# 输出: -321
# 示例 3:

# 输入: 120
# 输出: 21
# 解法一：
# 转化成list，运用list内置反转函数实现
# 以下是三种不同的写法
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            y = int(str(x)[::-1])
            if -2**31 <= y <= 2**31 - 1:
                return y
            else: return 0
        if x < 0:
            y = -int(str(-x)[::-1])
            if -2**31 <= y <= 2**31 - 1:
                return y
            else: return 0
                
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_VALUE = 2147483647
        MIN_VALUE = -2147483648
        x_list = [i for i in str(x)]
        if x_list[0] == '-':
            x_list.pop(0)
            x_list.append('-')       
        result = int(''.join(x_list[::-1]))
        if result not in range(MIN_VALUE, MAX_VALUE):
            return 0
        else:
            return result

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        st =str(x)
        tmp = list(st)
        if tmp[0] == '-':
            a = tmp.pop(0)
            tmp.reverse()
            tmp.insert(0,a)
            rest = "".join(tmp)
            answer = int(rest)
            if answer < (-2) **31:
                return 0
            return answer
        else:
            tmp.reverse()
            rest = "".join(tmp)
            answer = int (rest)
            if answer > (2 ** 31 -1):
                return 0
            return

# 解法二：按位数不断相除在重复加回

class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        elif x > 0:
            num = x
            sign = 1
        else:
            num = -x
            sign = -1

        rev = num % 10
        while num >= 10:
            num //= 10
            rev *= 10
            rev += num % 10

        INT_MAX_32 = 2**31 - 1
        if rev > INT_MAX_32:
            return 0
        else:
            return sign * rev