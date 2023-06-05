import os
from os import listdir,getcwd
from os.path import isfile, join, abspath, splitext
candidates = [
    ".woff2",
    ".woff"
]
def main(path):
    with open("font.css", "w") as css:
        for f in listdir(path):
            file = join(path,f)
            ext = splitext(file)[1]
            print(ext)
            if isfile(file) and ext in candidates: 
                css.write("@font-face")
                css.write("{")
                css.write(f"\n\tfont-family: '{f.split('.')[0].replace('-',' ')}';")
                css.write(f"\n\tsrc: url('{f}');")
                css.write("\n}\n")
if __name__ == '__main__':
    current_directory = abspath(getcwd())
    main(current_directory)