def listFiles(path='',filetype = ''):
    from os import listdir
    from os.path import isfile, join
    dirfiles = [f for f in listdir(path) if isfile(join(path, f))]
    files = list()
    for file in dirfiles:
        if file[-len(filetype):] == filetype and filetype != '':
            files.append(file)
        elif filetype == '':
            files.append(file)    
    return files
print(listFiles('RAWData'))
