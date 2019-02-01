# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

#方法一
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res, last_match = 0, -1
        for i, c in enumerate(s):
            if c in dic and last_match < dic[c]:
                last_match = dic[c]
            res = max(res, i - last_match)
            dic[c] = i
        return 

#方法二
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        i = j = 0
        set = []
        while(i<len(s) and j<len(s)):
            if not(s[j] in set):
                set.append(s[j])
                j+=1
                maxLen = max(maxLen,j-i)
            else:
                set.remove(s[i])
                i+=1
        return ma