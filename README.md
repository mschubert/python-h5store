h5store
=======

Store arbitrary lists of `numpy` `array`s or `pandas` `DataFrame`s as HDF5
objects. The library handles the dimension names.

Objects are saved in HDF5 groups of `value` with their actual content and
`names_<1..n>` for their dimension names. Upon loading they are restored in
their original state.

### Installation

The package requires [h5py](http://www.h5py.org/) and
[pandas](http://pandas.pydata.org/).

```python
pip install git+https://github.com/mschubert/python-h5store.git
```

### Usage

`save(object, file_name)` saves an object the the file `file_name`.

`load(file_name, path)` loads an object from `file_name`, optionally only
subsetting `path`.
