import os

try:
    from bs4 import BeautifulSoup
except ImportError:
    import pip
    pip.main(['install','bs4'])
    from bs4 import BeautifulSoup



home_dir = os.path.expanduser("~")

user_dir = input("Enter path to directory.\nExample Downloads\\Unit_1_Project\nPath: ")
path = home_dir + "\\" + user_dir

print("Creating .py scripts from all files in " + path)

directories = os.listdir(path)
for directory in directories:
    
    base_path = path + "\\" + directory
    subdirectories = os.listdir(base_path)
    
    for subdirectory in subdirectories:
        
        sub_path = base_path + "\\" + subdirectory
        
        for root, dirs, files in os.walk(sub_path):
            
            for file in files:
                
                if file[-4:] == "html":
                    
                    f = open(sub_path + "\\" + file, "r")
                    soup = BeautifulSoup(f, "html.parser")
                    text = soup.get_text("\n")
                    f.close()
                    
                    new_file_path = path + "\\" + directory
                    
                    print("creating file: " + new_file_path + ".py")
                    o = open(new_file_path + ".py", "w+")
                    o.write(text)
                    o.close()



