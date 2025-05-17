import os
class Personal_diary :
    def __init__(self):
        print("Welcome to your personal diary!")
        self.fun_choose()
    def fun_choose(self):  
        try: 
            self.choose_user =int(input("Please choose an option: \n1. Write a new diary entry\n2. Read existing diary entries\n3. delete line \n4. exit\n"))
            if self.choose_user == 1:
                self.fun_wirte_diary()
            elif self.choose_user == 2: 
                self.fun_read_diary()
            elif self.choose_user == 3: 
                self.fun_delete_diary()
            elif self.choose_user == 4:
                print("Goodbye!")
                exit()
            else:
                print("please choose between 1-4")
                self.fun_choose()
        except Exception as ex:
            print(f"Please enter a  number only ")
            self.fun_choose()
        
       
   
    

    def fun_wirte_diary(self):
        try:
            self.user_input = input("Please enter your diary entry: \n")
            # if exists
            if os.path.exists("diarty.txt"):
                self.file = open("diarty.txt","a")
                self.file.write(self.user_input+"\n")
                self.file.close()
                print("exists")
            # if not exists
            else:
                self.file = open("diarty.txt","a")
                self.file.write(self.user_input+"\n")
                self.file.close()
                print("not exists")
        except Exception as ex:
            print("Please enter a valid diary entry.")
            print(f"error is: {ex}")
            self.fun_wirte_diary()

    def fun_read_diary(self):
        self.file = open("diarty.txt","r")
        print("Your diary entries are:")
        print(self.file.read())
        self.file.close()

    def fun_delete_diary(self):
        try:
            self.user_input_line = int(input("Please enter the line number you want to delete: \n"))
            self.file = open("diarty.txt","r")
            self.list_lines = self.file.readlines()
            del self.list_lines[self.user_input_line]
            self.file = open("diarty.txt","w")
            self.file.writelines(self.list_lines)
            self.file.close()
        except Exception as ex:
            print(f"Please enter a  number only ")
            self.fun_delete_diary()





darry = Personal_diary()
