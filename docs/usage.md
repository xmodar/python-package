## Usage

We recommend using [VS Code](https://code.visualstudio.com/), which we configured to work with this project using [vs.code-workspace](./vs.code-workspace) and [settings.json](./.vscode/settings.json). You can always use a different IDE but you need to make sure to activate the virtual environment you created inside `.venv` folder previously.

```sh
source .venv/bin/activate
```

### Documentation

Adding documentation is as simple as modifying [mkdocs.yml](./mkdocs.yml) and [docs](./docs) folder. They are self-explanatory but for a very quick guide, refer to [this tutorial](https://www.mkdocs.org/) on how to use mkdocs. We also used GitHub [Project Pages](https://help.github.com/articles/user-organization-and-project-pages/#project-pages-sites) (as opposed to GitHub [Organization and User Pages](https://help.github.com/articles/user-organization-and-project-pages/#user-and-organization-pages-sites)) as demonstrated in [this tutorial](https://www.mkdocs.org/user-guide/deploying-your-docs/). Finally, we setup a custom subdomain for the project page (consult [this manual](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)). Assuming you have already purchased a domain name and hosted your personal website on GitHub with the following records in the domain's DNS table:

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

Then, modify [CNAME](./docs/CNAME) to reflect these changes. 

Once you are satisfied with your modifications to [mkdocs.yml](./mkdocs.yml) and the [documentation folder](./docs) and wants to test out your website:

```sh
mkdocs serve
```

If everything is in place, **commit your changes first**, then:

```sh
mkdocs gh-deploy
```
