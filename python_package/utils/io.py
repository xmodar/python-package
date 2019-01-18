"""Set of utilities for input/output operations.

This module can be used to illustrate common typing usages and mishaps.
"""
import os
import sys
from pathlib import Path
from tempfile import TemporaryFile
from typing import IO, Optional, Text, TextIO, Union, cast

__all__ = ['CaptureStdStreams', 'open_text_file', 'TypePath', 'TypePathOrIO']

TypePath = Union[Path, Text]
TypePathOrIO = Union[IO, TextIO, TypePath]


def open_text_file(path='', append=False):
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
                file = open(os.devnull, 'w')
            else:
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

    def __exit__(self, exception, instance, traceback):
        # type: ignore  # will be called by built-in with statement
        """Restore the standard streams."""
        try:
            self.stdout.flush()
            self.stderr.flush()
        finally:
            try:
                self.stdout.close()
                self.stderr.close()
            finally:
                sys.stdout = self.stdout.original_stream
                sys.stderr = self.stderr.original_stream
