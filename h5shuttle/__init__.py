import h5py
import pandas as pd
# alternative: use PyTables format, write R wrapper so it can read them?
# this would be quite a bit of work still..

class _H5Node(dict):
    def __init__(self, kwargs):
        for k,v in kwargs.iteritems():
            setattr(self, k, v)
        self.update(kwargs)

def save(X, file):
    def value2path(file, path, node):
        if (type(node) == "dict"):
            file.create_group(path)
            for k,v in node.iteritems():
                value2path(file, "/".join([path, k]), v)
        else:
            if type(node) == type(np.array(1)):
                val = node
            else:
                val = node.values

            file.create_dataset("/".join([path, "value"]), data=val)


    h5f = h5py.File(file)
    value2path(h5f, "", X)
    h5f.close()

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
                #TODO: use hierarchical indexing here
                raise Exception("only 1d/2d arrays supported so far")
        else:
            return _H5Node({n: path2value("/".join([path, n])) for n in fpk})

    with h5py.File(file, 'r') as file:
        return path2value(path)
