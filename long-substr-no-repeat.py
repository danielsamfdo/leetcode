# from collections import deque
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        chDict = defaultdict(int)
        mxCnt = 0
        cnt = 0
        for idx, ch in enumerate(s):
            queue.append(ch)
            # print(chDict, mxCnt, cnt)
            if chDict[ch] == 0:
                chDict[ch] += 1
                cnt += 1
                if cnt > mxCnt:
                    mxCnt = cnt
            else:
                while(True):
                    x = queue.popleft()
                    if x != ch:
                        cnt -= 1
                        chDict[x] -= 1
                    else:
                        break
        return mxCnt
from collections import deque
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        chDict = defaultdict(int)
        mxCnt = 0
        cnt = 0
        for idx, ch in enumerate(s):
            queue.append(ch)
            # print(chDict, mxCnt, cnt)
            if chDict[ch] == 0:
                chDict[ch] += 1
                cnt += 1
                if cnt > mxCnt:
                    mxCnt = cnt
            else:
                while(True):
                    x = queue.popleft()
                    if x != ch:
                        cnt -= 1
                        chDict[x] -= 1
                    else:
                        break
        return mxCnt
