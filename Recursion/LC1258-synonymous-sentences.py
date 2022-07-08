class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        lookup = defaultdict(list)
        for x,y in synonyms:
            lookup[x].append(y)
            lookup[y].append(x)
            
        s = text.split()
        n = len(s)
        ans = []
        
        def helper(word, visited, synos):
            if word not in visited and word in lookup:
                visited.add(word)
                for w in lookup[word]:
                    if w not in visited:
                        synos.append(w)
                        helper(w, visited, synos)
        
        def dfs(i, prev):
            if i == n:
                prev = prev[1:len(prev)]
                ans.append(prev)
                return
            word = s[i]
            dfs(i+1, prev + " " + word)
            
            synos = []
            visited = set()
            helper(word, visited, synos)
            for w in synos:
                dfs(i+1, prev + " " + w)
        dfs(0, "")
        ans.sort()
        return ans