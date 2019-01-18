"""English dictionary package."""
from .english import *

# hide these items from the package
for k in ['english']:
    globals().pop(k, None)
del k
