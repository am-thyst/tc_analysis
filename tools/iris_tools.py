import iris
import glob

def merge_files(file_type,out_name):
    files = glob.glob('*' + str(file_type) + '*.pp')
    df =iris.load(files)
    iris.save(df, out_name)
