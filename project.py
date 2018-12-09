import os


class Desktop_my_computer:
    def __init__(self):
        pass

class Folser():
    def __init__(self):
        pass
    

class File:
    def __init__(self, name, resolution):
        self.name_file = name + '.' + resolution
        self.coping = []
        self.file()

    def file(self):
        if os.path.isfile(self.name_file):
            self.f = open(self.name_file, 'r')
        else:
            self.f = open(self.name_file, 'w')
            self.f.close()
            self.f = open(self.name_file, 'r')

    def content(self):
        self.file()
        print(self.f.read())

    def copy_file(self, row):
         self.coping.append(row)
         print(coping)
         
    def cutout(self):
        self.file()
        for row in self.f.read():
            copy_file(row)
        self.f.close()
        os.remove('my_file.txt')
        #os.rmdir('pap') удаляет папку

    def insert(self):
        f = open('pap/' + self.name_file, 'w')
        for row in self.coping.read():
            f.write(row)
        f.close()
        
    

fold = File('my_file','txt')
fold.cutout()
fold.copy()
