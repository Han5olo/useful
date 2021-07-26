"""
the source of the main function can be found here: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
"""
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
