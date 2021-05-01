import tarfile
import os
from six.moves import urllib
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"

print(os.curdir)
print(os.path.abspath(os.curdir))