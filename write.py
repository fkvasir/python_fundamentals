examplefile = open("file.txt", "r") # /only-reading-files/
print(examplefile.read())
examplefile.close()

examplefile = open("file.txt", "a") # /adding-some-other-data-to-the-existing-file/
examplefile.write("\nJelly - Biology")
examplefile.close()

examplefile = open("file.txt", "w") # /overwrite-the-existing-file/
examplefile.write("\nKelly - Biology") # /erasing-the-existing-file-and-writing-a-new-one/
examplefile.close()
