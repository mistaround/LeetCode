class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r"[!?\',;.\"]+", " ", paragraph)
        word  = paragraph.split()
        print(word)
        banned = set(banned)
        count = {}
        for i in range(len(word)):
            w = word[i].lower()
            if w not in banned:
                count[w] = count.get(w, 0) + 1
        return Counter(count).most_common(1)[0][0]
        