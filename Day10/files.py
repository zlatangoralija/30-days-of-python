fname = 'hello-word.txt'

#First way of opening files and inserting into them
# file_object = open(fname, 'w')
# file_object.write('Hello world')
# file_object.close()

#Another way of opening and inserting in file - w stands for writing
with open(fname, 'w') as file_object:
    file_object.write('Hello world again')

#Reading files - r stands for reading
with open(fname, 'r') as f:
    print(f.read())



