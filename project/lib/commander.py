from workers import Extractor

class Commander:
    Commands = {}

    def register(self, command):
        # Parse
        command = command.split(' ')

        commandName = command[0]
        actions = command[1].replace('<','').replace('>','').split('/')
        other = command[2].replace('<','').replace('>','').split('/')

        # Prepare
        self.Commands[commandName] = {}

        # Register
        self.Commands[commandName]['actions'] = actions
        self.Commands[commandName]['other'] = other

    def showHelp(self):
        for commandName in self.Commands:
            print """
            {0} {1} {2}
            """.format(commandName, self.Commands[commandName]['actions'], self.Commands[commandName]['other'])

    def listen(self):
        self.showHelp()
        try:
            nb = raw_input('> ')
            parsed = nb.split(' ')

            if parsed[0] in self.Commands:
                if len(parsed) < 3:
                    print 'You didn\'t defined the action'
                else:
                    if parsed[1] not in self.Commands[parsed[0]]['actions'] or parsed[2] not in self.Commands[parsed[0]]['other']:
                        print 'Command not found!'
                    else:
                        self.call(parsed[0], parsed[1], parsed[2])
            else:
                print 'Command not found!'
        except Exception, ex:
            print ex

    def call(self, command, action, other):
        Extractor().do(command, action, other)
