class Directory():
    def __init__(self):
        self.root = {}

    def Directorys(self, directorys):

        try:

        except:

        return 0

    def mkDirec(Direc):
        return 0

    def rmDirec(Direc):
        return 0

    def cpDirec(Direc, Destiny):
        return 0

    def Command(self, cmd):
        cmd = cmd.split()
        if cmd[0] == 'mkdir':
            self.mkDirec(cmd[1])
        elif cmd[0] == 'rm':
            self.rmDirec(cmd[1])
        elif cmd[0] == 'cp':
            self.cpDirec(cmd[1], cmd[2])


def solution(directory, command):
    directorys = Directory()

    answer = []
    return answer