import os

way = ['D']
      
class Folder():
    def __init__(self, name):
        global way
        global copy_number
        global copy_max
        self.folder_name = name
        self.full_name = f"folders/{name}(" + '-'.join(way[:-1]) + ").txt"
        self.folder = open(self.full_name)
        self.folder_files = self.folder.readlines()
        self.files_sp_normal =  list(map(lambda x: x[:-1], self.folder_files))
        self.sp_files = []
        self.copy = open('copy.txt', 'r')


    def print_folder(self):
        print('/' + '/'.join(way))
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
                    print('new copy_max =', copy_max)
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
                    self.folder.close()
                    self.jump_folder(names)
                    self.del_folder('-all')
                    self.return_in_folder_up()
                    os.remove(f'folders/{names}(' + '-'.join(way) + ").txt")
                else:
                    t = open(f'files/{names}(' + '-'.join(way) + ").txt", 'w')
                    t.close()
                    os.remove(f'files/{names}(' + '-'.join(way) + ").txt")
                self.folder.replace(names + '\n', '')
        self.folder = open(self.full_name, 'w')
        self.folder.close()
        self.update()


    def jump_folder(self, name_next_folder):
        if name_next_folder in self.files_sp_normal:
            try:
                self.folder.close()
                way.append(name_next_folder)

                self.__init__(f'{name_next_folder}')
            except Exception as a:
                print(a)
                del way[-1]
        else:
            print('Невозможно')


    def return_in_folder_up(self):
        self.folder.close()
        if len(way) > 1:
            del way[-1]
            self.__init__(f'{way[-1]}')
        else:
            print('Невозможно')


    def create_folder(self, new_name):
        new_name = self.name_tester(new_name)
        self.folder = open(self.full_name, 'a')
        self.folder.write(new_name + '\n')
        self.new = open(f"folders/{new_name}(" + '-'.join(way) + ").txt", 'w')
        self.new.close()
        self.update()


    def insert_arxiv(self):
        global copy_max
        self.copy = open('copy.txt', 'r').readlines()
        self.folder = open(self.full_name, 'a')
        for i in range(1, copy_max+2):
            for file in self.copy:
                name, file_way, level = file.split()
                if level == str(i):
                    local_way = file_way[file_way.rfind('(')+1:-5].split('-')
                    if str(i) == '1':
                        local_way =[]
                        self.folder.write(name + '\n')
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
                        new_files.write(old_files[j] + '\n')
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
    

    def sorting(self):
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
        self.__init__(self.folder_name)
       

    def close(self):
        self.folder.close()
        
#-V-------------------------------Поиск----------------------------------V
    def find_file(self, file):
        print()
        if '.' in file:
         for name in os.listdir(path="./files"):
             if name[:name.rfind('(')] == file:
                 print(name[:name.rfind('.')].replace('-','/'))
        else:
         for name in os.listdir(path="./folders"):
             if name[:name.rfind('(')] == file:
                 print(name[:name.rfind('.')].replace('-','/'))

        
    def content_folder(self):
        for file in self.files_sp_normal:
            if '.txt' in file:  
                self.sp_files.append(file)
        print(self.files_sp_normal)


    def korrect_name_file(self, name_file):
        place = name_file[:name_file.index('.')]
        if name_file in self.files_sp_normal:
            self.name_file = f'files/{place}(' + '-'.join(way) + ').txt'
            self.file = open(self.name_file, 'r')
        else:
            print('Неподходящее имя файла')


    def put_up_file(self, name): 
        put_up_in_newfile = open(name, 'w') 
        self.copyfile = open('copyfile.txt', 'r')
        for row in self.copyfile.read():
            put_up_in_newfile.write(row)
        self.copyfile.close()
        put_up_in_newfile.close()


    def copy_file(self, name):
        self.copyfile = open('copyfile.txt', 'w')
        self.korrect_name_file(name)
        self.copyfile.write(self.file.read())
        self.copyfile.close()

    
    def del_file(self, name):
        self.folder = open(self.full_name, 'w')
        for row in self.folder_files:
            if row != (name + '\n'):
                self.folder.write(row)
        self.update()
        place = name[:name.index('.')]
        os.remove(f'files/{place}(' + '-'.join(way) + ').txt')
        

    def insert_file(self, name):
        place = name[:name.index('.')]
        if name not in self.sp_files:
            file = open(f'files/{place}(' + '-'.join(way) + ').txt', 'w')
        else:
            file = open(f'files/{place}(' + '-'.join(way) + ').txt', 'a')
        self.copyfile = open('copyfile.txt', 'r')
        for row in self.copyfile.read():
            file.write(row)
        self.folder = open(self.full_name, 'a')
        self.folder.write(name + '\n')
        self.update()
        self.copyfile.close()
        file.close()


    def create_file(self, name):
        self.folder = open(self.full_name, 'a')
        self.folder.write(f'{name}' + '\n')
        self.update()
        place = name[:name.index('.')]
        new_file = open(f'files/{place}(' + '-'.join(way) + ').txt', 'w')
        new_file.close()

    
if __name__ == '__main__':
    sp_comand = ['Копировать', 'Удалить', 'Содержимое',
                 'Переместиться', 'Вернуться', 'Создать', 'Вставить',
                 'Открыть', 'Поиск', 'Выйти']
    print('Добро пожаловать')
    print('Шаблон ввода: (команда) (имя файла)')
    print('Список команд: Копировать, Удалить, Содержимое,\n'
          'Переместиться, Вернуться, Создать, Вставить, Открыть,\n'
          'Поиск, Выйти')
    print('Для Вернуться имя файла не обязательно')
    D = Folder('D')
    stroka = ['']
    while stroka[0] != 'Выйти':
        try:
            print('-'* 50)
            D.print_folder()
            stroka = str(input('>>>')).split() 
            if stroka[0] not in sp_comand:
                print('Нет такой команды')
            if len(stroka) == 1: # думаю с этим будет проще. см Вставить для папок (Дима)
                stroka.append('')
            if stroka[0] == 'Копировать' and '.txt' in stroka[1]:#работает
                D.copy_file(stroka[1])
            elif stroka[0] == 'Копировать' and '' != stroka[1]: #робит, но можешь проверить (Дима)
                copy_number = 1
                copy_max = 1
                D.copy_arxiv(stroka[1:])
            elif stroka[0] == 'Поиск' and '' != stroka[1]:  #добавил новый метод
                D.find_file(stroka[1])
            elif stroka[0] == 'Удалить' and '.txt' not in stroka[1]:#удаляет файл, но не удаляет из списка
                D.del_folder(f'/folders/{stroka[1]}')               # теперь удаляет (Дима)
            elif stroka[0] == 'Удалить' and '.txt' in stroka[1]:
                D.del_file(stroka[1])
            elif stroka[0] == 'Открыть' and '.txt' in stroka[1]:#работает для txt
                place = stroka[1]
                place = place[:place.index('.')]
                os.startfile(f'files/{place}(' + '-'.join(way) + ').txt')
            elif stroka[0] == 'Открыть' and '.txt' not in stroka[1]:#напоминалка если введут не так
                print('Работает только для файлов!!!!')
                print('Для папок нажно использовать Переместиться')
            elif stroka[0] == 'Переместиться' and '.txt' not in stroka[1]:#работает для папок
                D.jump_folder(stroka[1])
            elif stroka[0] == 'Вернуться':#работет если мы не в D, если в D то Exception
                D.return_in_folder_up()
            elif stroka[0] == 'Создать' and '.txt' in stroka[1]:#работает
                D.create_file(stroka[1])
            elif stroka[0] == 'Создать' and '.txt' not in stroka[1]:#работает
                D.create_folder(stroka[1])
            elif stroka[0] == 'Вставить' and '.txt' in stroka[1]:#работает
                D.insert_file(stroka[1])
            elif stroka[0] == 'Вставить' and '' == stroka[1]: #робит, но можешь проверить (Дима)
                D.insert_arxiv()
            #elif stroka[0] == 'Вырерать' and '.txt' in stroka[1]:
                #D.copy_file(stroka[1])
            #elif stroka[0] == 'Вырезать' and '.txt' not in stroka[1]:
                #D.copy_arxiv(stroka[1]) делать ли их вообще???
                #D.del_folder(stroka[1])
            print(stroka)
        except Exception as e:
            print('Что-то не так')
    D.close()
    print('Окончание работы')
    

    
    
    
    
