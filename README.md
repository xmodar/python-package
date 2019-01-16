# Python Package

This is a minimal python package for a CLI app with automated unit tests and continuous integration bundled using [poetry](https://poetry.eustace.io/).

## Features

 - It has a [LICENSE](./LICENSE) file
 - It has a [README.md](./README.md) file
 - It is bundled using [poetry](https://poetry.eustace.io/)
 - Shipped with a [VS Code](https://code.visualstudio.com/)'s workspace [file](./vs.code-workspace)
    - VS Code [Version: 1.30.2] extensions:
        - Sublime Text Keymap and Settings Importer: [ms-vscode.sublime-keybindings](https://marketplace.visualstudio.com/items?itemName=ms-vscode.sublime-keybindings)
        - Code Spell Checker: [streetsidesoftware.code-spell-checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
        - Better TOML: [bungcip.better-toml](https://marketplace.visualstudio.com/items?itemName=bungcip.better-toml)
        - Python: [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
        - CTags Support: [jaydenlin.ctags-support](https://marketplace.visualstudio.com/items?itemName=jaydenlin.ctags-support)
    - Configured for python linting with [pep8](https://pypi.org/project/pep8/) and [pylint](https://www.pylint.org/)
    - Enables auto-formating with Google style using [yapf](https://github.com/google/yapf)
 - [TODO] CLI using [click](https://click.palletsprojects.com/en/7.x/)
 - [TODO] using [logging](https://docs.python.org/3/library/logging.html) and [pathlib](https://docs.python.org/3/library/pathlib.html)
 - [TODO] generate documentation using [mkdocs](https://www.mkdocs.org/) and publish on [GitHub pages](https://pages.github.com/)
 - [TODO] unit testing using [pytest](https://pytest.org) (and maybe [pytest-mock](https://pypi.org/project/pytest-mock/))
 - [TODO] automated testing using [tox](https://tox.readthedocs.io/en/latest/)
 - [TODO] continuous integration using [Travis-CI](https://travis-ci.com/)
 - [TODO] GitHub badges using [shields](https://shields.io/)
 - [TODO] type hints and annotations with [mypy](http://mypy-lang.org/)
 - [TODO] MAYBE Makefile and VS Code tasks
 - [TODO] publish on [PyPI](https://pypi.org/) (and maybe [conda](https://conda.io))
 - [TODO] investigate [docker](https://www.docker.com/) and [kubernetes](https://kubernetes.io/)
 - [TODO] create a [cookiecutter](https://github.com/audreyr/cookiecutter)


## Requirements

We will need [python](https://www.python.org/) to be installed but we don't want to use [conda](https://conda.io) the package manager. The main reason for this, is to break free from the conflict issues mentioned [here](https://www.anaconda.com/blog/developer-blog/understanding-conda-pip/) and to only use semi-standard tools like [poetry](https://poetry.eustace.io/) with [pip](https://pip.pypa.io/en/stable/). We can go the route of using [Docker](https://www.docker.com/) containers to install python as described [here](https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3) and run it using bash aliases similar to [this](https://hub.docker.com/r/chenzj/dfimage/). However, we will use a different approach.

### Installing python 3.7 on Ubuntu (optional)

You are encouraged not to override the default python installation in your linux machine. Instead, have an independent installation which you use to create virtual environments.

```sh
# source: https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/

# install the dependencies
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

# download the source code
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
sudo tar xvf Python-3.7.2.tar.xz

# compile the source code
cd Python-3.7.2
sudo ./configure --enable-optimizations
sudo make altinstall  # use altinstall to prevent replacing the default python

# if you faced a warning message in the make like
# "... directory is not owned by the current user and the cache has been disabled ...", do the following
sudo chown $USER: /home/$USER/.cache/pip

# now it should be installed and available if you run
python3.7 -V
pip3.7 -V

# now create a root virtual environment
```

### Create a python virtual environment on Ubuntu

You are always encouraged to use virtual environments instead of working on the original python installation. Therefore, we will install `venv` and use it to create a root virtual environment and put it in `~/.python/bin`.

```sh
python3.7 -m venv ~/.python --prompt py
```

If you didn't install Python 3.7, you can use this:

```sh
sudo apt-get install python3-venv
python3 -m venv ~/.python
```

This way, even if we missed up when installing dependencies and we wanted to start from a clean python installation, we can just delete the environment and create a clean new one.

```sh
rm -rf ~/.python
python3.7 -m venv ~/.python --prompt py
```

To activate the environment:

```sh
source ~/.python/bin/activate
```

In [vs.code-workspace](./vs.code-workspace), we are making this as the default virtual environment. However, we will be overriding it with the virtual environment that will be created later using poetry.

### Installing jupyterlab (optional)

Refer to the documentation [page](https://jupyterlab.readthedocs.io/en/stable/):

```sh
~/.python/bin/pip install jupyterlab

# create a link and make jupyter and ipython available anywhere (assumes ~/.local/bin is in PATH)
ln -s ~/.python/bin/jupyter ~/.local/bin/
ln -s ~/.python/bin/ipython ~/.local/bin/
```

To see the list of added kernels to jupyter and edit them:

```sh
jupyter kernelspec list
# jupyter kernelspec uninstall bad_kernel
```

To list any newly created virtual environment in jupyter, you need to activate it first then:

```sh
pip install ipykernel
python -m ipykernel install --user --name awesome_kernel
```

Now to run jupyterlab:

```sh
jupyter lab
```

### Installing poetry

Refer to the GitHub [page](https://github.com/sdispater/poetry):

```sh
~/.python/bin/pip install poetry
ln -s ~/.python/bin/poetry ~/.local/bin/
poetry config settings.virtualenvs.in-project true
```

To enable tab completion for Bash, run this and restart the terminal:

```sh
poetry completions bash > poetry.bash-completion
sudo mv poetry.bash-completion /etc/bash_completion.d
```

Now clone this repository and install it using poetry. The goal is to create a new virtual environment, which will be used for development:

```sh
git clone https://github.com/ModarTensai/python_package
cd python_package && poetry install
```

If you pass `--no-dev` to `poetry install`, the `dev-dependencies` in [pyproject.toml](./pyproject.toml) will not be installed.

To run anything in this new virtual environment use:

```sh
poetry run python -V
# poetry shell  # use this to spawn inside the environment
```

For example, to add this virtual environment to jupyter:

```sh
poetry run pip install ipykernel
poetry run python -m ipykernel install --user --name python_package
```

If you want to remove it later from jupyter:

```sh
jupyter kernelspec uninstall python_package 
```

To clear the cache and recreate the virtual environment again, you need to delete it first:

```sh
# get the directory of the environment and remove it
rm -rf .venv  # this if you enabled in-project virtual environment setting
# rm -rf $(readlink -f $(dirname $(poetry run which python))/..)
poetry cache:clear --all .
poetry install
```

## License

[MIT](./LICENSE)

## Author

[Modar M. Alfadly](https://modar.me)

## Contributors

I would gladly accept any pull request to this repository.