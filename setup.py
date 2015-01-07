from distutils.core import setup

setup(
    name='h5store',
    version='0.0.1',
    author='Michael Schubert',
    author_email='mschu.dev+h5@gmail.com',
    packages=['h5store'],
#    scripts=['bin/stowe-towels.py'],
#    url='http://pypi.python.org/pypi/h5shuttle/',
#    license='LICENSE.txt',
#    description='Useful towel-related stuff.',
#    long_description=open('README.txt').read(),
    install_requires=[
        "h5py",
        "pandas"
    ],
)
