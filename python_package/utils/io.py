"""Set of utilities for input/output operations.

This module can be used to illustrate common typing usages and mishaps.
"""
import os
import sys
from logging import getLogger
from pathlib import Path
from tempfile import TemporaryFile
from typing import IO, Dict, Optional, Text, TextIO, Union, cast

del Optional  # for pylint-W0611 because mypy

__all__ = [
    'CaptureStdStreams', 'open_text_file', 'read_dict', 'TypePath',
    'TypePathOrIO', 'TypePathOrDict'
]

TypePath = Union[Path, Text]
TypePathOrIO = Union[TypePath, IO, TextIO]
TypePathOrDict = Union[TypePath, Dict]
del IO, Text, TextIO, Union

_log = getLogger(__name__)


class _ReadDict:

    supported_types = ('.yml', '.json')

    def __call__(self, a_dict=None, env_key=None):
        # type: (Optional[TypePathOrDict], Optional[Text]) -> Dict
        """Get a dict from file.

        Args:
            a_dict: It can be a dictionary or a file path.
                If dict, return it as is. Otherwise, it has to be one of
                the file types in `{type(self).supported_types}`.
                If `env_key` is defined and valid, use it instead.
            env_key: An environment variable for the file path.

        Returns:
            The loaded dict.

        Raises:
            FileNotFoundError: If file not found.
            ValueError: Invalid file or `a_dict` and `env_key` are None.
                The error message is the file absolute path or empty.
            NotImplementedError: Supported but not implemented type.

        """
        path = None  # type: Optional[TypePath]
        if env_key is not None:
            path = os.getenv(env_key)
        if not path:
            if isinstance(a_dict, Dict):
                return a_dict
            if not a_dict:
                raise ValueError()
            path = a_dict
        path = Path(path).expanduser().absolute()
        if not path.exists():
            raise FileNotFoundError(str(path))
        supported = _ReadDict.supported_types
        if path.suffix not in supported:
            raise ValueError(str(path))
        with path.open('rt') as f:
            if path.suffix == '.yml':
                import yaml
                return yaml.safe_load(f.read())
            if path.suffix == '.json':
                import json
                return json.load(f)
        msg = (f'`{path.suffix}` is in the supported list: {supported}. '
               f'However, there is no implementation for this type.')
        try:
            raise NotImplementedError
        except:
            _log.error(msg, exc_info=True)
            raise


# https://github.com/python/mypy/issues/2087
read_dict = _ReadDict()


def open_text_file(path=None, append=False):
    # type: (Optional[TypePathOrIO], bool) -> TextIO
    """Open a file in the specified path and create it if doesn't exist.

    Args:
        path: The path of the file or an oppend text file.
            If None, create a temporary file.
            If an open file, pass it through.
        append: Whether to open in an appending mode.

    Returns:
        An oppend file.

    """
    if not path:
        return cast(TextIO, TemporaryFile('w+t'))
    if hasattr(path, 'write') and hasattr(path, 'close'):
        return cast(TextIO, path)
    path = cast(TypePath, path)
    path = Path(path).expanduser().absolute()  # get full path
    path.parent.mkdir(exist_ok=True)  # create if doesn't exist
    return cast(TextIO, path.open('a' if append else 'w'))


class CaptureStdStreams:
    """Context manager to capture the standard streams to files."""

    def __init__(
            self,
            stdout=None,  # type: Optional[TypePathOrIO]
            stderr=None,  # type: Optional[TypePathOrIO]
            suppress_stdout=True,  # type: bool
            suppress_stderr=True,  # type: bool
            append=False  # type: bool
    ):  # type: (...) -> None
        """Mirror the output and error streams to files.

        Args:
            stdout: The text file to save the standard output to.
            stderr: The text file to save the standard error to.
            suppress_stdout: Whether to suppress output to `sys.stdout`.
            suppress_stderr: Whether to suppress output to `sys.stderr`.
            append: Whether to append to the file.

        """

        def file_stream(file, stream, suppress):
            # type: (Optional[TypePathOrIO], TextIO, bool) -> TextIO
            if file is None:
                _log.debug('Creating suppressed stream')
                file = open(os.devnull, 'w')
            else:
                _log.debug('Creating file stream')
                file = open_text_file(file, append=append)
            file_write = file.write
            file_flush = file.flush

            def write(message):
                # type: (Text) -> None
                if not suppress:
                    stream.write(message)
                file_write(message)

            def flush():
                # type: () -> None
                if not suppress:
                    stream.flush()
                file_flush()

            setattr(file, 'original_stream', stream)
            setattr(file, 'write', write)
            setattr(file, 'flush', flush)
            return file

        self.stdout = file_stream(stdout, sys.stdout, suppress_stdout)
        self.stderr = file_stream(stderr, sys.stderr, suppress_stderr)

    def __enter__(self):
        # type: () -> None
        """Switch the standard streams."""
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        _log.debug('Switched standard streams')

    def __exit__(self, exception, instance, traceback):
        # type: ignore  # will be called by built-in with statement
        """Restore the standard streams."""
        try:
            self.stdout.flush()
            self.stderr.flush()
        except:  # pylint: disable=W0702
            _log.warning('Could not flush streams', exc_info=True)
        finally:
            try:
                self.stdout.close()
                self.stderr.close()
            except:  # pylint: disable=W0702
                _log.ward('Could not close streams', exc_info=True)
            finally:
                sys.stdout = self.stdout.original_stream
                sys.stderr = self.stderr.original_stream
                _log.debug('Back to original streams')
