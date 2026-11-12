class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans={}
        for i in strs:
            a="".join(sorted(i))
            if a not in ans:
                ans[a]=[]
            ans[a].append(i)
        return list(ans.values())