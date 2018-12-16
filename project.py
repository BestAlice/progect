import os
    
way = ['', 'D']
      
class Folder():
    def __init__(self, name):
        global way
        self.full_name = f'folders/{name}({way[-2]}).txt'
        self.folder = open(self.full_name)
        self.folder_files = self.folder.readlines() # вот список всего, что есть в папке
        self.files_sp_normal =  list(map(lambda x: x[:-1], self.folder_files))
        # тоже, что и self.solder_files, только имена без \n в конце
        if '(' in name and ')' in name:
            normal_name = ''
            for i in name:
                if i == '(':
                    break
                normal_name += i
            name = normal_name
        self.folder_name = name
        self.sp_files = []
        self.copy = open('copy.txt', 'r')
        self.update()

    def del_folder(self, del_folder):
        self.folder = open(self.full_name, 'w')
        for names in self.files_sp_normal: # действует по принципу:
                                           #отчисти и вставь всё, кроме удалённого файла
            if names != del_folder:
                self.folder.write(names + '\n')
        self.folder.close()
        os.remove(f"folders/{del_folder}({way[-2]}).txt") # удаляет файл txt папки 
        self.update()

    def jump_folder(self, name_next_folder):
        if name_next_folder in self.files_sp_normal: # проверка наличия в данной папке
            self.folder.close()
            way.append(name_next_folder)
            self.__init__(f'{name_next_folder}')
            # весь код этой функции перезапускает init из новой папки
        else:
            print('Невозможно')

    def return_in_folder_up(self):
        self.folder.close()
        if len(way) > 1: # проверка, что мы не в папке D
            del way[-1]
            self.__init__(f'{way[-1]}')
        else:
            print('Невозможно')

    def create_folder(self, new_name):
        new_name = self.helper_insert([new_name])[0]
        # эксплуатирую чужую вспомогательную функцию для проверки имени на оригинальность
        self.folder = open(self.full_name, 'a')
        self.folder.write(new_name + '\n')
        self.new = open(f'folders/{new_name}({way[-1]}).txt', 'w')
        self.new.close()
        self.update()

    def copy_folder(self, name_copy):
        if name_copy == '-all':  
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
        self.copy_from = way[-1]
        self.copy_folder = self.folder

    def insert_folder(self):
        self.copy.close()
        self.copy = open('copy.txt', 'r').readlines()
        sp_folder = self.helper_insert(self.copy)
        self.folder = open(self.full_name, 'a')
        for new in sp_folder:
            self.folder.write(new)
        self.folder.close()
        self.folder = open(self.full_name, 'r')
        self.folder_files = self.folder.readlines()
        self.update()

    def helper_insert(self, spisok): # обработка одинаковых имён(не советую разбираться)
        self.folder = open(self.full_name)
        sp_new_names = []
        for name in spisok:
            i = 1
            new_name = name
            while new_name in self.files_sp_normal:
                new_name = name + '_' + str(i)
                i += 1 
            new_folder = open(f'folders/{new_name}({way[-1]}).txt', 'w')
            old_folder = open(f'folders/{name}({way[-1]}).txt').readline()
            new_folder.write(old_folder)
            new_folder.close()
            sp_new_names.append(new_name)
        return sp_new_names
        
    def cutout_folder(self, name_cutout):  # не проверено
        copy_folder(copy_folder)
        del(self.copy_folder) #должно срабатывать после копирования

    def sorting(self): # чтобы все имена были по алфавиту
        self.folder = open(self.full_name, 'r')
        self.folder_files = self.folder.readlines()
        self.folder_files.sort()
        self.folder = open(self.full_name, 'w')
        for i in self.folder_files:
            i = i[:-1] if '\n' in i else i
            self.folder.write(i + '\n')
        self.folder.close()

    def update(self):
        self.sorting()
        self.folder = open(self.full_name, 'r')
        self.folder_files = self.folder.readlines()

    def close(self):
        self.folder.close()
#------------------------------------------------------------------------------
    def content_folder(self):
        for file in self.files_sp_normal:
            if '.txt' in file:  
                self.sp_files.append(file)
        print(self.files_sp_normal)
#------------------------------------------------------------------------------

    def korrect_name_file(self, name_file):
        if (name_file + '.txt') in self.files_sp_normal:#проверка что он в папке
            self.name_file = f'files/{name_file}({way[-1]}).txt'
            self.file = open(self.name_file, 'r')
        else:
            print('Неподходящее имя файла')


    def content_file(self):
        print(self.file.read()) #вывести содержимое файла
    

    def put_up_file(self, name): #перетаскиваем скопированное в другой файл
        put_up_in_newfile = open(name, 'w') #куда мы сохраняем
                                            #скопированые данные
        self.copyfile = open('copyfile.txt', 'r')#Открываем для чтения из него
        for row in self.copyfile.read():
            put_up_in_newfile.write(row)
        self.copyfile.close()
        put_up_in_newfile.close()


    def copy_file(self, name):
        self.copyfile = open('copyfile.txt', 'w')
        self.korrect_name_file(name)
        self.copyfile.write(self.file.read())
        self.copyfile.close()
        
         
    def cutout_file(self, name_for_del, name_for_insert):
        #self.copy_file(name_for_del) #копируем
        #os.remove(f"files/{name_for_del}({way[-1]}).txt") # удаляем
        #self.folder = open(self.full_name, 'w')
        #for line in self.folder_files:                         #НА ДОРАБОТКЕ!!!!!!!
            #if line != name_for_del + '.txt' + '\n':
                #self.folder.write(line)
        #self.insert_file(name_for_insert)
        pass
        

    def insert_file(self, name):#куда мы будем вставлять
        if name not in self.sp_files:
            file = open(f'files/{name}({way[-1]}).txt', 'w')
        else:
            file = open(f'files/{name}({way[-1]}).txt', 'a')
        self.copyfile = open('copyfile.txt', 'r')
        for row in self.copyfile.read():
            file.write(row)
        self.copyfile.close()
        file.close()


    def create_file(self, name):
        #new_name = self.helper_insert([name])[0] тут происходит какая то фигня ибо файл тогда
        #записывается в файл D и в папку folder, вместо файла D
        self.folder = open(self.full_name, 'a')
        self.folder.write(f'{name}.txt' + '\n')
        self.update()
        new_file = open(f'files/{name}({way[-1]}).txt', 'w')
        new_file.close()

    
if __name__ == '__main__':
    D = Folder('D')
    
    
    
    
