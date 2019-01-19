# Python Package

This is a minimal python package for a CLI app with automated unit tests and continuous integration bundled using [poetry](https://poetry.eustace.io/).

## Features

 - It has a [LICENSE](./LICENSE) file
 - It has a [README.md](./README.md) file
 - It is bundled using [poetry](https://poetry.eustace.io/)
 - [mkdocs](https://www.mkdocs.org/) documentation published using [GitHub pages](https://pages.github.com/) on a [custom domain](https://python_package.modar.me)
 - Shipped with a [VS Code](https://code.visualstudio.com/)'s workspace [file](./vs.code-workspace) and recommended [extensions](./.vscode/extensions.json)
    - Configured for python linting with [pep8](https://pypi.org/project/pep8/), [pylint](https://www.pylint.org/), [mypy](http://mypy-lang.org/) and [pydocstyle](http://www.pydocstyle.org/en/3.0.0/usage.html)
    - Enables auto-formating with Google style using [yapf](https://github.com/google/yapf) and [isort](https://pypi.org/project/isort/)
 - An example package of an English dictionary with the following:
    - Follows the guidelines specified by the mentioned linters
    - Type hints and annotations with [mypy](http://mypy-lang.org/)
    - uses [pathlib](https://docs.python.org/3/library/pathlib.html) and [logging](https://realpython.com/python-logging/)
    - [TODO] has a CLI using [click](https://click.palletsprojects.com/en/7.x/)
    - [TODO] unit testing using [pytest](https://pytest.org) (and maybe [pytest-mock](https://pypi.org/project/pytest-mock/))
 - [TODO] automated testing using [tox](https://tox.readthedocs.io/en/latest/)
 - [TODO] continuous integration using [Travis-CI](https://travis-ci.com/)
 - [TODO] GitHub badges using [shields](https://shields.io/)
 - [TODO] MAYBE Makefile and VS Code tasks
 - [TODO] publish on [PyPI](https://pypi.org/) (and maybe [conda](https://conda.io))
 - [TODO] investigate [docker](https://www.docker.com/) and [kubernetes](https://kubernetes.io/)
 - [TODO] create a [cookiecutter](https://github.com/audreyr/cookiecutter)


## Requirements

The assumed operating system is Ubuntu and follow the [documentation](https://python_package.modar.me/requirements/):

 - [Install Python 3.7](https://python_package.modar.me/requirements/#installing-python-37-on-ubuntu-optional) (optional)
 - [Create a virtual environment](https://python_package.modar.me/requirements/#create-a-python-virtual-environment-on-ubuntu)
 - [Install JupyterLab](https://python_package.modar.me/requirements/#installing-jupyterlab-optional) (optional)
 - [Install Poetry](https://python_package.modar.me/requirements/#installing-poetry)

## Usage

We recommend using [VS Code](https://code.visualstudio.com/) and following the instructions provided [here](https://python_package.modar.me/usage/).

- [Documentation and GitHub Pages hosting](https://python_package.modar.me/usage/#documentation)

## License

[MIT](./LICENSE)

## Author

[Modar M. Alfadly](https://modar.me)

## Contributors

I would gladly accept any pull request to this repository.