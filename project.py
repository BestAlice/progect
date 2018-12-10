import os


class Desktop_my_computer:
    def __init__(self):
        pass

class Folser():
    def __init__(self):
        pass
    

class File:
    def __init__(self, name):
        self.name_file = name
        self.file = open(self.name_file, 'r')
        self.copy = open('copy.txt', 'w')

    def content_file(self):
        print(self.file.read())

    def copy_file(self):
        self.copy.write(self.file.read())
        self.copy.close()
        
         
    def cutout_file(self):
        for row in self.f.read():
            copy_file(row)
        self.f.close()
        os.remove('my_file.txt')
        #os.rmdir('pap') удаляет папку

    def insert_file(self):
        f = open('pap/' + self.name_file, 'w')
        for row in self.coping.read():
            f.write(row)
        f.close()
        
    
if __name__ == '__main__':
    filyk = File('my_file.txt')
    filyk.copy_file()        

