import os


way = ['D']

        
class Folder():
    def __init__(self, name):
        global way
        self.folder_name = name 
        self.folder = open(name, 'r')
        self.folder_files = self.folder.readlines()
        self.files_sp_normal =  list(map(lambda x: x[:-1], self.folder_files))
        self.copy = open('copy.txt', 'w')
        self.update()

    def del_folder(self, del_folder):
        self.folder = open(self.folder_name, 'w')
        for names in self.files_sp_normal:
            if names != del_folder:
                self.folder.write(names + '\n')
        self.folder.close()
        os.remove(f"{del_folder}.txt")
        self.update()

    def jump_folder(self, name_next_folder):
        if name_next_folder in self.files_sp_normal:
            self.folder.close()
            self.copy.close()
            way.append(name_next_folder)
            self.__init__(f'{name_next_folder}.txt')
        else:
            print('Невозможно')

    def rerurn_in_folder_up(self):
        self.folder.close()
        self.copy.close()
        if len(way) > 1:
            del way[-1]
            self.__init__(f'{way[-1]}.txt')
        else:
            print('Невозможно')

    def create_folder(self, new_name):
        new_name = self.helper_insert([new_name])[0]
        self.folder = open(self.folder_name, 'a')
        self.folder.write(new_name + '\n')
        self.new = open(f'{new_name}.txt', 'w')
        self.new.close()
        self.update()

    def copy_folder(self, name_copy):
        if name_copy == '-all':
            name_copy = self.files_sp_normal
        self.copy = open('copy.txt', 'w')
        if type(name_copy) == str: 
            self.copy.write(name_copy)
        elif type(name_copy) == dir:
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

    def helper_insert(self, spisok): # обработка одинаковых имён
        self.folder = open(self.folder_name)
        sp_new_names = []
        for name in spisok:
            i = 1
            new_name = name
            while new_name in self.files_sp_normal:
                new_name = name + str(i)
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

    def sorting(self):
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

    def close(self):
        self.folder.close()
        
      
if __name__ == '__main__':
    D = Folder('D.txt')
    D.copy_folder('papka')
    D.jump_folder('papka')
    D.insert_folder()
    D.copy_folder('-all')  # на этой команде почему-то крашится, если хочешь, то можешь потестировать
    D.del_folder('papka')
    D.rerurn_in_folder_up()
    #D.insert_folder()
    D.close()
    
    
