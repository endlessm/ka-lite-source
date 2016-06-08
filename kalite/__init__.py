import os
import sys

from version import *


__version__ = VERSION

# ROOT_DATA_PATH is *not* where the source files live. It's a place where non-user-writable data files may be written.
ROOT_DATA_PATH = None

# Consider KALITE_DIR here or we will keep pointing to the sys.prefix (e.g. /usr)
# even in envorinments when it does not make any sense (e.g. flatpak bundles).
if 'KALITE_DIR' in os.environ:
    ROOT_DATA_PATH = os.environ['KALITE_DIR']
else:
    ROOT_DATA_PATH = os.path.join(sys.prefix, 'share', 'kalite')
