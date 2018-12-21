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
        self.folder_files = self.folder.readlines() # вот список всего, что есть в папке
        self.files_sp_normal =  list(map(lambda x: x[:-1], self.folder_files))
        # тоже, что и self.solder_files, только имена без \n в конце
        self.sp_files = []
        self.copy = open('copy.txt', 'r')
        self.sorting()


    def print_folder(self):
        print('/'.join(way))
        for name in self.files_sp_normal:
              print(name)
        print()


    def copy_arxiv(self, dir_copy):
        global copy_number
        global copy_max
        global first_time
        if dir_copy[0] == '-all':  
            dir_copy = self.files_sp_normal
            print(dir_copy) 
        for name in dir_copy:
            self.copy = (open('copy.txt', 'w') if first_time == True
                         else open('copy.txt', 'a'))
            first_time = False
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
                self.copy_arxiv(['-all'])
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
                f = self.files_sp_normal
                self.folder = open(self.full_name, 'w')
                for i in f:
                    if i != names:
                        self.folder.write(i)
                self.folder.close()
                self.update()


    def jump_folder(self, name_next_folder):
        if name_next_folder in self.files_sp_normal:
            try:
                self.folder.close()
                way.append(name_next_folder)
                self.__init__(f'{name_next_folder}')
                # весь код этой функции перезапускает init из новой папки
            except Exception as a:
                print(a)
                del way[-1]
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
        self.__init__(self.folder_name)
       

    def close(self):
        self.folder.close()


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


    def global_jump(self, new_way):
        global way
        self.old_way = way
        try:
            new_way =  new_way.split('/')
            if new_way[0] == '.':
                new_way = way + new_way[1:]
            way = new_way
            new_way, final_dir = '-'.join(new_way[:-1]), new_way[-1]
            open(f'folders/{final_dir}({new_way}).txt')
            new_way =  new_way.split('-')
            self.__init__(final_dir)
        except Exception:
            way = self.old_way
            print(f'папки {final_dir} не существует по данному пути')
            print('может быть вы имели ввиду:')
            self.find_file(final_dir)

        
    def content_folder(self):
        for file in self.files_sp_normal:
            if '.txt' in file:  
                self.sp_files.append(file)
        print(self.files_sp_normal)


    def korrect_name_file(self, name_file):#name = (file).txt
        place = name_file[:name_file.index('.')]
        if name_file in self.files_sp_normal:#проверка что он в папке
            self.name_file = f'files\{place}({way[-1]}).txt'
            self.file = open(self.name_file, 'r')
        else:
            print('Неподходящее имя файла')


    def content_file(self):
        print(self.file.read()) #вывести содержимое файла
    

    def put_up_file(self, name): #перетаскиваем скопированное в другой файл
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
        

    def insert_file(self, name):
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
        self.folder = open(self.full_name, 'a')
        self.folder.write(f'{name}' + '\n')
        self.update()
        place = name[:name.index('.')]
        new_file = open(f'files\{place}({way[-1]}).txt', 'w')
        new_file.close()

    def shablon(self):
        print('Шаблон ввода: (команда) (имя файла, если надо)')
        print('Список команд: Помощь, Копировать, Удалить, Содержимое, Инструкция,\n'
              'Переместиться(в папку, находящуюся в данной), Переход(при помощи пути),\n'
              'Вернуться, Создать, Вставить, Открыть, Найти, Завершить')
        

    
if __name__ == '__main__':
    sp_comand = ['копировать', 'удалить', 'содержимое', 'помощь',
                 'инструкция', 'переход', 'переместиться', 'вернуться',
                 'создать', 'вставить','открыть', 'найти', 'переход',
                 'завершить']
    print('Добро пожаловать')
    D = Folder('D')
    D.shablon() 
    stroka = ['']
    while stroka[0] != 'завершить':
        try:
            print('-'* 50)
            D.print_folder()
            stroka = str(input('>>>')).split()
            stroka[0] = stroka[0].lower()
            if stroka[0] not in sp_comand:
                print('Нет такой команды')
            if len(stroka) == 1: # думаю с этим будет проще. см Вставить для папок (Дима)
                stroka.append('')
            if stroka[0] == 'копировать' and '' != stroka[1]: 
                copy_number = 1
                copy_max = 1
                first_time = True
                D.copy_arxiv(stroka[1:])
            elif stroka[0] == 'переход' and '' != stroka[1]:
                D.global_jump(stroka[1])
            elif stroka[0] == 'найти' and '' != stroka[1]: 
                D.find_file(stroka[1])
            elif stroka[0] == 'удалить' and '' != stroka[1]:#удаляет файл, но не удаляет из списка
                D.del_folder(stroka[1:])               # теперь удаляет (Дима)
            elif stroka[0] == 'открыть' and '.txt' in stroka[1]:#работает для txt
                place = stroka[1]
                place = place[:place.index('.')]
                os.startfile(f'files\{place}({way[-1]}).txt')
            elif stroka[0] == 'помощь' and '' == stroka[1]:
                D.shablon()
            elif stroka[0] == 'инструкция' and '' == stroka[1]:
                f = open('README.txt').readlines()
                for h in f:
                    print(h[:-1])
            elif stroka[0] == 'открыть' and '.txt' not in stroka[1]:#напоминалка если введут не так
                print('Работает только для файлов!!!!')
                print('Для папок нажно использовать Переместиться')
            elif stroka[0] == 'переместиться' and '.txt' not in stroka[1]:#работает для папок
                D.jump_folder(stroka[1])
            elif stroka[0] == 'вернуться':#работет если мы не в D, если в D то Exception
                D.return_in_folder_up()
            elif stroka[0] == 'создать' and '.txt' in stroka[1]:#работает
                D.create_file(stroka[1])
            elif stroka[0] == 'создать' and '.txt' not in stroka[1]:#работает
                D.create_folder(stroka[1])
            elif stroka[0] == 'вставить' and '.txt' in stroka[1]:
                D.insert_file(stroka[1])
            elif stroka[0] == 'вставить' and '' == stroka[1]: #робит, но можешь проверить (Дима)
                D.insert_arxiv()
        except Exception as e:
            print(e)
            print('Поломка!!!!!!!!!')
    D.close()
    print('Окончание работы') 
    

    
    
    
    
