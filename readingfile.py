demo_file = open('demo.txt','r')
print(demo_file.readable())
#print(demo_file.readlines()[2]) -->  we can print third line of the file
#print(demo_file.redlines()) --> print the first line of the file
for lines in demo_file.readlines():
    print(lines)
demo_file.close()



