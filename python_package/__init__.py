"""English dictionary package."""
from logging import NullHandler, getLogger
from pathlib import Path
from typing import Dict, Text, Union

from . import cli
from .__version__ import __version__
from .english import *
from .utils.io import read_dict

del Path, Dict, Text, Union  # for pylint-W0611 because mypy

# hide these items from the package
for _to_hide in ['english']:
    globals().pop(_to_hide, None)
del _to_hide

# http://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
getLogger(__name__).addHandler(NullHandler())
del getLogger, NullHandler


# source: https://realpython.com/python-logging/#other-configuration-methods
# source: https://docs.python.org/3/library/logging.html#logrecord-attributes
# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
class _SetupLogging:

    read_dict = read_dict

    env_key = __name__.upper() + '_LOGGING_CONFIG'

    supported_types = ['.conf', '.ini'] + list(read_dict.supported_types)

    def __call__(self, config=None):
        # type: (Union[Dict, Text, Path, None]) -> None
        """Configure logging.

        https://docs.python.org/3/library/logging.config.html#logging-config-api

        Args:
            config: The configuration as specified in the above link.
                It can be the configuration dictionary or a file path.
                It supports {type(self).supported_types} types.
                If `{type(self).env_key}` was defined, it will be loaded.

        Raises:
            Everything raised by `read_dict()`,
            `logging.config.dictConfig` and `logging.config.fileConfig`.

        """
        import logging.config
        try:
            config_dict = type(self).read_dict(
                a_dict=config, env_key=type(self).env_key)
            logging.config.dictConfig(config_dict)
        except ValueError as p:
            path = str(p)
            if any(path.endswith(e) for e in type(self).supported_types):
                logging.config.fileConfig(path, disable_existing_loggers=False)
            else:
                raise


# https://github.com/python/mypy/issues/2087
setup_logging = _SetupLogging()
del read_dict, _SetupLogging
