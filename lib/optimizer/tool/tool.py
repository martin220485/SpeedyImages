from subprocess import call

class tool:

    def __init__(self, file):
        self.file = file

    def before(self):
        pass

    def after(self):
        pass

    def compress(self):
        self.before()
        call(self.getCommand(), stdout = open(devnull, 'w'))
        self.after()

    def getCommand(self):
        raise 'tool.py!!!!'
        toolDir = ''
        return [toolDir + self.tool] + self.commands + [self.file]
