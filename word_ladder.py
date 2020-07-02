from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = self.construct_dict(wordList)
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        
        q = deque([(beginWord,1)])
        visited = {}
        
        while q:
            first = q.popleft()
            print(first)
            word,lvl = first
            if word not in visited:
                visited[word] = 1
                if word == endWord:
                    return lvl
                for i in range(len(word)):
                    curr = word[:i] + "_" + word[i+1:]
                    neigh = wordDict.get(curr,[])
                    for n in neigh:
                        if n not in visited:
                            q.append((n,lvl+1))
        
        return(0)
        
        
        
    def construct_dict(self,word_list):
        d = {}
        for word in word_list:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                d[s] = d.get(s, []) + [word]
        return d