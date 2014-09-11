import h5py
import pandas as pd

def load(file, path="/"):
    def path2value(path):
        fpk = file[path].keys()
        if 'value' in fpk:
            value = file[path]["value"].value
            nidx = ["names_"+str(i+1) for i in range(len(value.shape))]
            names = [file[path][n].value.tolist()
                     if n in fpk else None for n in nidx]

            if (len(value.shape) == 1):
                return pd.DataFrame(value, index=names[0])
            if (len(value.shape) == 2):
                return pd.DataFrame(value.transpose(), index=names[0], columns=names[1])
            else:
                raise Exception("only 1d/2d arrays supported so far")
        else:
            return {n:path2value("/".join([path, n])) for n in fpk}

    file = h5py.File(file, 'r')
    return path2value(path)
