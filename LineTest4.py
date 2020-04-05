def solution(snapshots, transactions):
    trans = {}
    for i in transactions:
        trans[i[0]] = i[1:]
    Accounts = {}
    for i in snapshots:
        Accounts[i[0]] = int(i[1])

    for key, value in trans.items():

        try:
            if value[0] == 'SAVE':
                Accounts[value[1]] += int(value[2])

            elif value[0] == 'WITHDRAW':
                Accounts[value[1]] -= int(value[2])

        except:
            Accounts[value[1]] = int(value[2])

    answer = []
    for key, value in Accounts.items():
        answer.append([key, str(value)])
    return answer