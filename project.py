import os
    
way = ['', 'D']
copy_number = 1
copy_max = 1
      
class Folder():
    def __init__(self, name):
        global way
        global copy_number
        global copy_max
        self.folder_name = name
        self.full_name = f"folders/{name}(" + '-'.join(way[:-1]) + ").txt"
        self.folder = open(self.full_name)
        self.folder_files = self.folder.readlines() # вот список всего, что есть в папке
        self.files_sp_normal =  list(map(lambda x: x[:-1], self.folder_files))
        # тоже, что и self.solder_files, только имена без \n в конце
        self.sp_files = []
        self.copy = open('copy.txt', 'r')
        self.update()

    def print_folder(self):
        print('/'.join(way))
        for name in self.files_sp_normal:
              print(name)
        print()

    def copy_arxiv(self, dir_copy):
        global copy_number
        global copy_max
        if dir_copy == '-all':  
            dir_copy = self.files_sp_normal
        self.copy = open('copy.txt', 'w') if copy_number == 1 else open('copy.txt', 'a')
        for name in dir_copy:
            directory = 'files' if '.txt' in name else 'folders'
            this_way = f'{directory}/{name}(' + '-'.join(way) +')'
            self.copy.write(f"{name} {this_way}.txt {copy_number}\n")
            if not '.txt' in name:
                copy_number += 1
                if copy_number > copy_max:
                    copy_max = copy_number 
                else:
                    copy_max = copy_max
                self.copy.close()
                self.jump_folder(name)
                self.copy_arxiv('-all')
                self.return_in_folder_up()
                copy_number -= 1
        self.copy.close()
        self.update()

    def del_folder(self, del_folders):
        if del_folders == '-all':  
            del_folders = self.files_sp_normal 
        for names in self.files_sp_normal:
            if names in del_folders:
                if not '.txt' in names:
                    self.folders.close()
                    self.jump_folder(names)
                    self.del_folder('-all')
                    self.return_in_folder_up()
                    os.remove(f'folders/{names}(' + '-'.join(way) + ").txt")
                else:
                    t = open(f'files/{names}(' + '-'.join(way) + ").txt", 'w')
                    t.close()
                    os.remove(f'files/{names}(' + '-'.join(way) + ").txt")
        self.folders = open(self.full_name, 'w')
        for names in self.files_sp_normal:
            if not names in del_folders:
                self.folder.write(names + '\n')
        self.folder.close()
        print(list(filter(lambda x: not '.txt' in x, del_folders)))
        for one_folder in list(filter(lambda x: not '.txt' in x, del_folders)):
            os.remove(f"folders/{one_folder}(" + '-'.join(way) + ").txt") 
        self.update()

    def jump_folder(self, name_next_folder):
        if name_next_folder in self.files_sp_normal:
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
        new_name = self.name_tester(new_name)
        # эксплуатирую чужую вспомогательную функцию для проверки имени на оригинальность
        self.folder = open(self.full_name, 'a')
        self.folder.write(new_name + '\n')
        self.new = open(f"folders/{new_name}(" + '-'.join(way) + ").txt", 'w')
        self.new.close()
        self.update()

    def insert_arxiv(self):
        self.copy = open('copy.txt', 'r').readlines()
        self.folder = open(self.full_name, 'a')
        for i in range(1, copy_max+2):
            for file in self.copy:
                name, file_way, level = file.split()
                if level == str(i):
                    local_way = file_way[file_way.rfind('(')+1:-5].split('-')
                    if str(i) == '1':
                        local_way =[]
                    elif str(i) == '2':
                        local_way[-1] = '-' + local_way[-1]
                    else:
                        local_way[-i+1] = '-' + local_way[-i+1]
                    if '.txt' in name:
                        new_files = open(f"files/{name}(" + '-'.join(way) +
                                         '-'.join(local_way[-i+1:]) + ").txt",'a')
                    else:
                        new_files = open(f"folders/{name}(" + '-'.join(way) +
                                      '-'.join(local_way[-i+1:]) + ").txt",'a')
                    old_files = open(file_way).readlines()
                    for j in range(len(old_files)):
                        new_files.write(old_files[j])
                    new_files.close()
        self.update()
                
    def name_tester(self, test_name):
        self.folder = open(self.full_name)
        sp_new_names = []
        i = 1
        new_name = test_name
        while new_name in self.files_sp_normal:
            new_name = test_name + '_' + str(i)
            i += 1
        return new_name
        
    def cutout_folder(self, name_cutout):  # не работает
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
            self.name_file = f'files/{name_file}(' + '-'.join(way[:-1]) + ').txt'
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
            file = open(f'files/{name}(' + '-'.join(way[:-1]) +').txt', 'w')
        else:
            file = open(f'files/{name}(' + '-'.join(way[:-1]) +').txt', 'a')
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
        new_file = open(f'files/{name}(' + '-'.join(way[:-1]) +').txt', 'w')
        new_file.close()

    
if __name__ == '__main__':
    sp_comand = ['Копировать', 'Удалить', 'Содержимое',
                 'Переместиться', 'Вернуться', 'Создать', 'Вставить',
                 'Закрыть программу']
    print('Добро пожаловать')
    print('Шаблон ввода: (команда) (имя файла)')
    print('Список команд: Копировать, Удалить, Содержимое,'
          'Переместиться, Вернуться, Создать, Вставить, Закрыть программу')
    print('Изначально вы находитесь в папке D')
    D = Folder('D')s
    stroka = str(input())
    while stroka != 'Закрыть программу':
        stroka = stroka.split()
        if stroka[0] not in sp_comand:
            print('Нет такой команды')
        if stroka[0] == 'Копировать' and '.txt' in stroka[1]:
            D.copy_file(stroka[1])
        elif stroka[0] == 'Удалить' and '.txt' not in stroka[1]:
            D.del_folder(stroka[1])
        elif stroka[0] == 'Содержимое' and '.txt' in stroka[1]:
            D.content_file(stroka[1][:stroka[1].index('.txt')])
        elif stroka[0] == 'Содержимое' and '.txt' not in stroka[1]:
            D.print_folder()
        elif stroka[0] == 'Переместиться' and '.txt' not in stroka[1]:
            D.jump_folder(stroka[1])
        elif stroka[0] == 'Вернуться' and '.txt' not in stroka[1]:
            D.return_in_folder_up()
        elif stroka[0] == 'Создать' and '.txt' in stroka[1]:
            D.create_file(stroka[1])
        elif stroka[0] == 'Создать' and '.txt' not in stroka[1]:
            D.create_folder(stroka[1])
        elif stroka[0] == 'Вставить' and '.txt' in stroka[1]:
            D.insert_file(stroka[1])
        elif stroka[0] == 'Вставить' and '.txt' not in stroka[1]:
            D.insert_arxiv(way[-1])
        elif stroka[0] == 'Вырерать' and '.txt' in stroka[1]:
            D.copy_file(stroka[1])
        elif stroka[0] == 'Вырезать' and '.txt' not in stroka[1]:
            D.copy_arxiv(stroka[1])
            D.del_folder(stroka[1])
        stroka = str(input())
    

    
    
    
    
