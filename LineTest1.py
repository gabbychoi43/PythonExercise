def solution(inputString):
    Strings = {}
    Strings['('] = ')'
    Strings['{'] = '}'
    Strings['['] = ']'
    Strings['<'] = '>'
    cnt = 0
    Flag = True
    while Flag:
        for i in Strings:

            if i in inputString:
                if inputString.index(i) < inputString.index(Strings[i]):
                    cnt += 1
                    inputString.replace(i, '')
                else:
                    return -1
            else:
                Flag = False

    return cnt