import sys

filename = sys.argv[1]

print(filename)
print()

fh = open(filename , 'r')
lines_list = list()
line = fh.read()
fh.close()


print(line)
list_lines = line.split('\n')
print("number of lines in text file are:", len(list_lines))
number = 6
if(len(list_lines)==0) :
    print("file is empty")
elif (len(list_lines) < number) :
    print(list_lines[0 : len(list_lines) : ])
else :
    print(list_lines[len(list_lines)-number : len(list_lines) :])

    


