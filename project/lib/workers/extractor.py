from urllib import urlretrieve, urlopen
from threading import Thread, activeCount
from time import sleep
from json import loads
from os import path
from sys import exit

class Extractor:
    Pending = []
    __Limit = 100
    __Dist = 'sm2'

    def do(self, command, action, other):
        if not path.isdir(self.__Dist) or not path.exists(self.__Dist):
            print 'The destination folder doesn\'t exists: ' + self.__Dist
            exit()

        self.parse(action, other, self.fetch('http://xat.com/web_gear/chat/pow2.php'))
        self.download()

    def fetch(self, url):
        fetched = urlopen(url)
        fetched = fetched.read()

        try:
                parsed = loads(fetched)

                return parsed
        except Exception, e:
                print e
                return []

    def parse(self, action, other, data):
        if action == 'pss':
            data = data[5][1]

            for key in data:
                self.Pending.append(key)
        elif action == 'topsh':
            data = data[3][1]

            for key in data:
                self.Pending.append(key)


    def download(self):
        try:
            i = 0
            while i < len(self.Pending):
                while activeCount() < self.__Limit and i < len(self.Pending):
                    print 'Downloading: ', self.Pending[i], '{0}/{1}'.format(i + 1, len(self.Pending))
                    Thread(target = self.retrieve, args = [self.Pending[i]]).start()
                    i += 1
                sleep(1)
        except Exception, ex:
            print ex

    def retrieve(self, name):
        while True:
            try:
                urlretrieve("http://xat.com/images/sm2/" + name + ".swf", self.__Dist + "/" + name + ".swf")
                break
            except Exception, e:
                print e
                pass
