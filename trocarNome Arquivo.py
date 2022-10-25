import os

file_oldname = os.path.join("C:/Users/Gabriel/Desktop/", "trocarnome.txt")
file_newname_newfile = os.path.join("C:/Users/Gabriel/Desktop/novo_arquivo", "MudamosOnome.txt")

os.rename(file_oldname, file_newname_newfile)