import os
from os import listdir
from os.path import isfile, join

import candidates

candidate = [
{
    'type': '.ttf',
    'fun': getattr(candidates, 'ttf_woff2')
},
{
    'type': '.otf',
    'fun': getattr(candidates, 'otf_woff2')  
}
]
def any_to_candidates(path):
    count = 0
    def get_type(arr, type):
        values = []
        for obj in arr:
            for key in obj.keys():
                if key == type:
                    values.append(obj[key])
        return values
    candidates_ext = get_type(candidate, "type")
    for f in listdir(path):
        file = join(path,f)
        ext = os.path.splitext(file)[1]
        if isfile(file) and ext in candidates_ext:
            print(candidate[candidates_ext.index(ext)]['fun'](file, f))
if __name__ == "__main__": 
    current_directory = os.path.abspath(os.getcwd())
    any_to_candidates(current_directory)