from sys import argv
from os.path import exists

script, num1, num2, num3, num4, num5, out_filename = argv

file_exists = exists(out_filename)
print("Does the output file exist? {}".format(file_exists))
print("Writing output to {}".format(out_filename))

out_file = open(out_filename, "w")
outdata = out_file
print("Waiting... Type the RETURN key to continue")
input()
      
answer = (float(num1) + float(num2) + float(num3) + float(num4) + float(num5)) / (len(argv) - 2) #compensating

out_file.write("{:.2f}\n".format(answer))
print("\a")
out_file.close()