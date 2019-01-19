## Usage

We recommend using [VS Code](https://code.visualstudio.com/), which we configured to work with this project using `vs.code-workspace` and `settings.json`. You can always use a different IDE but you need to make sure to activate the virtual environment you created inside `.venv` folder previously.

```sh
source .venv/bin/activate
```

### Documentation

Adding documentation is as simple as modifying `mkdocs.yml` and `docs` folder. They are self-explanatory but for a very quick guide, refer to [this tutorial](https://www.mkdocs.org/) on how to use mkdocs. We also used GitHub [Project Pages](https://help.github.com/articles/user-organization-and-project-pages/#project-pages-sites) (as opposed to GitHub [Organization and User Pages](https://help.github.com/articles/user-organization-and-project-pages/#user-and-organization-pages-sites)) as demonstrated in [this tutorial](https://www.mkdocs.org/user-guide/deploying-your-docs/). Finally, we setup a custom subdomain for the project page (consult [this manual](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)). Assuming you have already purchased a domain name and hosted your personal website on GitHub with the following records in the domain's DNS table:

<!-- table is generated using: https://www.tablesgenerator.com/markdown_tables -->
| Type  | Name | Value                             |
|-------|------|-----------------------------------|
| A     | @    | 185.199.108.153                   |
| A     | @    | 185.199.109.153                   |
| A     | @    | 185.199.110.153                   |
| A     | @    | 185.199.111.153                   |
| CNAME | www  | &lt;github-username&gt;.github.io |

Note: these IP addresses are from [this page](https://help.github.com/articles/setting-up-an-apex-domain/).

Now to link your project page to your domain as `python_package.example.com` add:

| Type  | Name           | Value                             |
|-------|----------------|-----------------------------------|
| CNAME | python_package | &lt;github-username&gt;.github.io |

Then, modify the `CNAME` file in `docs` to reflect these changes. 

Once you are satisfied with your modifications to `mkdocs.yml` and the documentation folder and wants to test out your website:

```sh
mkdocs serve
```

If everything is in place, **commit your changes first**, then:

```sh
mkdocs gh-deploy
```

### Command Line Interface (CLI)

We used [click](https://click.palletsprojects.com/en/7.x/) to implement a CLI for our example English dictionary package.

```sh
english
```

```
Usage: english [OPTIONS] COMMAND [ARGS]...

  English dictionary.

Options:
  -r, --run / -d, --debug  Whether to run without debugging.  [default: True]
  -v, --version            Show the version and exit.
  --help                   Show this message and exit.

Commands:
  antonyms     Get the different antonyms of a given word.
  meanings     Get the different meanings of a given word.
  suggestions  Get the different suggestions of a given word.
  synonyms     Get the different synonyms of a given word.
```

### Linting and testing

Fortunately linting is automatically done through the recommended VS Code extensions in `extensions.json`. As for unit testing and code coverage, both can be achieved through [pytest](https://pytest.org) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/), respectively. In theory, we could use [unittest](https://docs.python.org/3.7/library/unittest.html) and [pytest-mock](https://pypi.org/project/pytest-mock/) to test each and every unit in our package. However, we only implemented two unit tests using [click.testing](https://click.palletsprojects.com/en/7.x/testing/).

```sh
pytest tests  # run pytest only
py.test --cov=python_package tests  # run pytest and coverage
```