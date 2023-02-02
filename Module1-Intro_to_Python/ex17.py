from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Coping from {from_file} to {to_file}")

#we could do these twi on one line, how?
in_file = open(from_file) # ex7_text.txt
indata = in_file.read()

print (f"The inpurt file is {len(indata)} bytes long")
print (f"Does the output file exist? {exists(to_file)}")
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input (">>")

out_file = open(to_file, 'w') #ex7_output.txt
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()