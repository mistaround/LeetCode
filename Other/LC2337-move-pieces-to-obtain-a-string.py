class Solution:
    def canChange(self, start: str, target: str) -> bool:
        "R___L"
        "__L_R"
        "R_L_"
        "__LR"
        slc, src = 0, 0
        tlc, trc = 0, 0
        n = len(start)
        
        for i in range(n):
            if start[i] == "L":
                slc += 1
            elif start[i] == "R":
                src += 1
            if target[i] == "L":
                tlc += 1
            elif target[i] == "R":
                trc += 1
            
            if slc > tlc:
                return False
            if src < trc:
                return False 
            if target[i] == "L" and src > trc:
                return False
            
        return True if (slc == tlc and src == trc) else False