# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:

# 所有输入只包含小写字母 a-z 。
# 拿第一个子串做标准，循环剩余所有字串，分别一个一个元素对比，如果相等就把该元素相加


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=""
        if len(strs) > 0:
            x = strs[0]
            for i, n in enumerate(x):
                for j in range(1,len(strs)):
                    if i<= (len(strs[j])-1) and n == strs[j][i]:
                        continue
                    else:
                        return result
                result += n
            return result
        else:
            return result