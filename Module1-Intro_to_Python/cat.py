from sys import argv
script, file_name = argv

file = open(file_name) # Allows you to get access to the file
file_content = file.read() #read() reads all of the contents from the file and returns it
print (file_content)

file.close() #close() closes the file - no more reads from or writes to the file can occur

