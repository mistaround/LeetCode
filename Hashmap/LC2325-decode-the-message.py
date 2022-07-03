class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        subs = {}
        count = 0
        for c in key:
            if count == 26:
                break
            if c != " " and c not in subs:
                subs[c] = chr(ord('a') + count)
                count += 1
        print(subs)
        text = ""
        for c in message:
            if c == " ":
                text += " "
            else:
                text += subs[c]
        return text
                