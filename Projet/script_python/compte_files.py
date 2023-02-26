import os, os.path

def count_files(folder):
    # simple version for working with CWD
    return len([name for name in os.listdir(folder) if os.path.isfile(name)])

    # path joining version for other paths
    #DIR = '/tmp'
    #return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])