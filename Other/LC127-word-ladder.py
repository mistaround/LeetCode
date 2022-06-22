class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        
        beginSet = set()
        endSet = set()
        beginSet.add(beginWord)
        endSet.add(endWord)
        
        step = 1
        while len(beginSet) != 0 and len(endSet) != 0:
            step += 1
            # To speed up
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            for s in beginSet:
                if s in wordSet:
                    wordSet.remove(s)
            for s in endSet:
                if s in wordSet:
                    wordSet.remove(s)
            
            next = set()
            
            for s in beginSet:
                for i in range(len(s)):
                    char = s[i]
                    for c in range(ord('a'),ord('z')+1):
                        s = s[:i] + chr(c) + s[i+1:]
                        if s in endSet:
                            return step
                        if s not in wordSet:
                            continue
                        next.add(s)
                    s = s[:i] + char + s[i+1:]
            beginSet = next
        
        return 0