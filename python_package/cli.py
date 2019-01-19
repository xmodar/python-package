"""Command line interface (CLI) for an English dictionary."""
from logging import getLogger
from pathlib import Path

import click

from .__version__ import __version__
from .english import English

__all__ = ['main', 'meanings', 'synonyms', 'antonyms', 'suggestions']

DEBUG = False
PREFIX = Path(__file__).parent.name.upper()

_log = getLogger(__name__)


class Config:

    def __init__(self):
        self.debug = DEBUG  # type: bool
        self.en = English()  # type: English


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option(
    '-r/-d',
    '--run/--debug',
    'run_mode',
    is_flag=True,
    default=not DEBUG,
    show_default=True,
    envvar='_'.join([PREFIX, 'RUN']),  # get environment variable if defined
    help='Whether to run without debugging.')
@click.version_option(__version__, '-v', '--version')
@pass_config
def main(config, run_mode):
    # type: (Config, bool) -> None
    """English dictionary."""
    config.debug = not run_mode
    _log.debug('Running in debug mode: %s', config.debug)


@main.command()
@click.argument('word')
@pass_config
def meanings(config, word):
    # type: (Config, str) -> None
    """Get the different meanings of a given word.

    word: The word to use.

    """
    for category, definitions in config.en.meanings(word).items():
        click.echo(category + ':')
        for definition in definitions:
            click.echo('\t' + definition)


@main.command()
@click.argument('word')
@pass_config
def synonyms(config, word):
    # type: (Config, str) -> None
    """Get the different synonyms of a given word.

    word: The word to use.

    """
    click.echo('Synonym:')
    for synonym in config.en.synonyms(word):
        click.echo('\t' + synonym)


@main.command()
@click.argument('word')
@pass_config
def antonyms(config, word):
    # type: (Config, str) -> None
    """Get the different antonyms of a given word.

    word: The word to use.

    """
    click.echo('Antonyms:')
    for antonym in config.en.antonyms(word):
        click.echo('\t' + antonym)


@main.command()
@click.argument('word')
@pass_config
def suggestions(config, word):
    # type: (Config, str) -> None
    """Get the different suggestions of a given word.

    word: The word to use.

    """
    click.echo('Suggestions:')
    for suggestion in config.en.suggest(word):
        click.echo('\t' + suggestion)
