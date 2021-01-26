import os


for path in os.listdir('./'):
    filename, file_extension = os.path.splitext(path)
    if file_extension == '.dat':
        f = open(filename + file_extension)
