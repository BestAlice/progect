import os


        
class Folder():
    def __init__(self, name):
        self.folder_name = name
        #self.folder_up = self.folder 
        self.folder = open(name, 'r')
        self.folder_files = self.folder.readlines()
        self.copy = open('copy.txt', 'w')
        self.update()

    def del_folder(self, del_name, del_folders): # =self.folder
        file_del = open(f'{del_name}.txt').read()
        os.remove(file_del) #f"(del_name).txt"
        del_folders = del_folders.replace(f'{del_name}\n','')
        self.update()
        #проверить

    def create_folder(self, new_name):
        self.folder = open(self.folder_name, 'w')
        self.folder.write(new_name + '\n')
        self.new = open(f'{new_name}.txt', 'w')
        self.new.close()
        self.update()

    def rerurn_in_folder_up(self):
        self.folder.close()
        #self.folder = self.folder_up
        self.folder_files = self.folder.readlines()

    def copy_folder(self, name_copy):
        if type(name_copy) == str: 
            self.copy.write(name_copy)
        elif type(name_copy) == dir:
            for name in name_copy:
                self.copy.write(name + '\n')
        self.copy.close()
        self.copy_folder = self.folder

    def insert_folder(self, in_folder):  #добавить возможность перемещения по имени
        # можешь даже не пытаться читать. Просто знай, что это работает
        self.copy = open('copy.txt', 'r').readlines()
        sp_folder = self.helper_insert()
        self.folder = open(self.folder_name, 'a')
        for new in sp_folder:
            self.folder.write(new)
        self.folder.write('\n')
        self.folder.close()
        self.folder = open(self.folder_name, 'r')
        self.folder_files = self.folder.readlines()
        self.update()

    def helper_insert(self): # обработка одинаковых имён
        self.folder = open(self.folder_name)
        files_sp =  list(map(lambda x: x[:-1], self.folder.readlines()))
        sp_new_names = []
        for name in self.copy:
            i = 1
            new_name = name
            while new_name in files_sp:
                new_name = name + str(i)
                i += 1
            sp_new_names.append(new_name)
        return sp_new_names
            
        
    def cutout_folder(self, name_cutout):
        copy_folder(copy_folder)
        del(self.copy_folder) #должно срабатывать после копирования

    def sorting(self):
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
    D.insert_folder('фф')
    D.close()
    
    
