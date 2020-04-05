import itertools as it


class Cheat():

    def __init__(self, answer_sheet):
        self.answer_sheet = answer_sheet

    def CheatValue(self, sheet1, sheet2):
        cheatList = []
        for i in range(len(self.answer_sheet)):
            if self.answer_sheet[i] != sheet1[i] and sheet1[i] == sheet2[i]:
                cheatList.append(1)
            else:
                cheatList.append(0)
        return cheatList



def solution(answer_sheet, sheets):
    x = it.combinations(range(len(sheets)), 2)
    CheatV = 0
    cheat = Cheat(answer_sheet)
    cheatL = []
    for i in x:
        same = 0
        l = cheat.CheatValue(sheets[i[0]], sheets[i[1]])
        for j in l:
            same += j

        l.append(0)
        n = len(l)
        cnt = 0
        cntlist = []
        for j in range(n):
            if l[j] == 1:
                if cnt == 0:
                    cnt += 1
                if l[j + 1] == 1:
                    cnt += 1
                else:
                    cntlist.append(cnt)
                    cnt = 0

        cntlist.append(0)

        cheatL.append(same + max(cntlist) ** 2)
    answer = max(cheatL)
    return answer