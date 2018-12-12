import os
    
way = ['D']
      
class Folder():
    def __init__(self, name):
        global way
        self.folder_name = name
        self.folder = open(name)
        self.folder_files = self.folder.readlines() # вот список всего, что есть в папке
        self.files_sp_normal =  list(map(lambda x: x[:-1], self.folder_files))
        # тоже, что и self.solder_files, только имена без \n в конце
        self.copy = open('copy.txt', 'w')
        self.sp_files = []
        self.update()

    def del_folder(self, del_folder):
        self.folder = open(self.folder_name, 'w')
        for names in self.files_sp_normal: # действует по принципу:
                                           #отчисти и вставь всё, кроме удалённого файла
            if names != del_folder:
                self.folder.write(names + '\n')
        self.folder.close()
        os.remove(f"{del_folder}.txt") # удаляет файл txt папки 
        self.update()


    def jump_folder(self, name_next_folder):
        if name_next_folder in self.files_sp_normal: # проверка наличия в данной папке
            self.folder.close()
            self.copy.close()
            way.append(name_next_folder)
            self.__init__(f'{name_next_folder}.txt')
            # весь код этой функции перезапускает init из новой папки
        else:
            print('Невозможно')


    def rerurn_in_folder_up(self):
        self.folder.close()
        self.copy.close()
        if len(way) > 1: # проверка, что мы не в папке D
            del way[-1]
            self.__init__(f'{way[-1]}.txt')
        else:
            print('Невозможно')


    def create_folder(self, new_name):
        new_name = self.helper_insert([new_name])[0]
        # эксплуатирую чужую вспомогательную функцию для проверки имени на оригинальность
        self.folder = open(self.folder_name, 'a')
        self.folder.write(new_name + '\n')
        self.new = open(f'{new_name}.txt', 'w')
        self.new.close()
        self.update()


    def copy_folder(self, name_copy):
        if name_copy == '-all':
            print(self.files_sp_normal)
            name_copy = self.files_sp_normal
        self.copy = open('copy.txt', 'w')
        if type(name_copy) == str: 
            self.copy.write(name_copy)
        elif type(name_copy) == dir:
        # если будем переносить несколько папок,
        #хотя надо бы сделать единую функцию для копирования и папок, и файлов 
            for name in name_copy:
                self.copy.write(name + '\n')
        self.copy.close()
        self.copy_folder = self.folder


    def insert_folder(self): 
        self.copy = open('copy.txt', 'r').readlines()
        sp_folder = self.helper_insert(self.copy)
        self.folder = open(self.folder_name, 'a')
        for new in sp_folder:
            self.folder.write(new)
        self.folder.close()
        self.folder = open(self.folder_name, 'r')
        self.folder_files = self.folder.readlines()
        self.copy = open('copy.txt', 'w')
        self.update()


    def helper_insert(self, spisok): # обработка одинаковых имён(не советую разбираться)
        self.folder = open(self.folder_name)
        sp_new_names = []
        for name in spisok:
            i = 1
            new_name = name
            while new_name in self.files_sp_normal:
                new_name = name + '_' + str(i)
                i += 1
            if name != new_name: 
                new_folder = open(f'{new_name}.txt', 'w')
                old_folder = open(f'{name}.txt').readline()
                new_folder.write(old_folder)
                new_folder.close()
            sp_new_names.append(new_name)
        return sp_new_names

        
    def cutout_folder(self, name_cutout):  # не проверено
        copy_folder(copy_folder)
        del(self.copy_folder) #должно срабатывать после копирования


    def sorting(self): # чтобы все имена были по алфавиту
        self.folder = open(self.folder_name, 'r')
        self.folder_files = self.folder.readlines()
        self.folder_files.sort()
        self.folder = open(self.folder_name, 'w')
        for i in self.folder_files:
            i = i[:-1] if '\n' in i else i
            self.folder.write(i + '\n')
        self.folder.close()

    def update(self):
        self.sorting()
        self.folder = open(self.folder_name, 'r')
        self.folder_files = self.folder.readlines()
        for file in self.files_sp_normal:#надо чтобы список файлов уже был готов
            #if '.txt' in file:
                self.sp_files.append(file)
        
    def content_folder(self):
        print(self.sp_files)
        print(self.files_sp_normal)

    def close(self):
        self.folder.close()
    
#------------------------------------------------------------------------------

    def create_file(self, name_new_file):#создаём файл и задаём ему имя
        self.sp_files.append(name_new_file)
        f = open(name_new_file, 'w')
        f.close

        
    def open_file_in_folder(self, name_file):#начинаю совмещать 2 класса
        if name_file in self.sp_files:
            self.name_file = name_file
            self.file = open(self.name_file, 'r')
        else:
            print('Невозможно открыть файл')


    def content_file(self):
        print(self.file.read()) #вывести содержимое файла
    

    def put_up_file(self, name): #перетаскиваем скопированное в другой файл
        put_up_in_newfile = open(name, 'w') #куда мы сохраняем
                                            #скопированые данные
        self.copyfile = open('copyfile.txt', 'r')#Открываем для чтения из него
        for row in self.copyfile.read():
            put_up_in_newfile.write(row)
        #with open('copyfile.txt', 'w'): pass #Очищает copy.txt
        self.copyfile.close()
        put_up_in_newfile.close()


    def copy_file(self):
        self.copyfile = open('copyfile.txt', 'w')
        self.copyfile.write(self.file.read())
        self.copyfile.close()
        
         
    def cutout_file(self, name):
        self.copy_file() #копируем
        del(self.file) #удаляем
        self.insert_file(name) 
        

    def insert_file(self, name):
        self.newfile = open(name, 'w')
        self.copyfile = open('copyfile.txt', 'r')
        for row in self.copyfile.read():
            self.newfile.write(row)
        self.copyfile.close()
        self.newfile.close()


      
        
    
if __name__ == '__main__':
    D = Folder('D.txt')

