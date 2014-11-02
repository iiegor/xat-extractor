from workers import Extractor

class Commander:
    Commands = {}

    def register(self, command):
        command = command.split(' ')

        commandName = command[0]
        values = command[1].replace('<','').replace('>','').split('/')

        self.Commands[commandName] = values

    def showHelp(self):
        for commandName in self.Commands:
            print """
            {0} {1}
            """.format(commandName, self.Commands[commandName])

    def listen(self):
        self.showHelp()
        try:
            nb = raw_input('> ')
            parsed = nb.split(' ')

            if parsed[0] in self.Commands:
                if len(parsed) < 2:
                    print 'You didn\'t defined the action'
                else:
                    if parsed[1] not in self.Commands[parsed[0]]:
                        print 'Action not found!'
                    else:
                        self.call(parsed[0], parsed[1])
            else:
                print 'Command not found!'
        except Exception, ex:
            print ex

    def call(self, command, action):
        Extractor().do(command, action)
