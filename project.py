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


    def content_file(self):
        print(self.file.read()) #вывести содержимое файла
    

    def put_up_file(self, name): #перетаскиваем скопированное в другой файл
        put_up_in_newfile = open(name, 'w') #куда мы сохраняем
                                            #скопированые данные
        self.copy = open('copy.txt', 'r')#Открываем для чтения из него
        for row in self.copy.read():
            put_up_in_newfile.write(row)
        with open('copy.txt', 'w'): pass #Очищает copy.txt
        self.copy.close()
        put_up_in_newfile.close()


    def copy_file(self):
        self.copy = open('copy.txt', 'w')
        self.copy.write(self.file.read())
        self.copy.close()
        
         
    def cutout_file(self, name):
        self.copy_file() #копируем
        del(self.file) #удаляем
        self.insert_file(name) 
        #os.rmdir('pap') удаляет папку
        

    def insert_file(self, name):
        self.newfile = open(name, 'w')
        self.copy = open('copy.txt', 'r')
        for row in self.copy.read():
            self.newfile.write(row)
        self.copy.close()
        self.newfile.close()
    
        
    
if __name__ == '__main__':
    filyk = File('my_file.txt')


    #filyk.copy_file()
    #filyk.put_up_file('for_put_up.txt')для этой комбинации не записывает
    #filyk.cutout_file('for_cutout.txt') в for_cotout.txt скопированный текст

