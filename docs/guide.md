---
myst:
  substitutions:
    HPC: "*Hypermodern Python Cookiecutter*"
---

# User Guide

This is the user guide
for the [Hypermodern Python Cookiecutter],
a Python template based on the [Hypermodern Python] article series.



## Introduction

### About this project


(features)=

### Features

Here is a detailed list of features for this Python template:

```{eval-rst}
.. include:: ../README.md
   :parser: myst_parser.sphinx_

```

### Version policy

The {{ HPC }} uses [Calendar Versioning] with a `YYYY.MM.DD` versioning scheme.

The current stable release is [2022.6.3].

(installation)=

## Installation

### System requirements

You need a recent Windows, Linux, Unix, or Mac system with [git] installed.

:::{note}
When working with this template on Windows,
configure your text editor or IDE
to use only [UNIX-style line endings] (line feeds).

Nonetheless, configuring your editor for line feeds is recommended
to avoid complaints from the [pre-commit] hook for Prettier.
:::

### Getting Python (Windows)

If you're on Windows,
download the recommended installer for the latest stable release of Python
from the official [Python website].
Before clicking **Install now**,
enable the option to add Python to your `PATH` environment variable.

Verify your installation by checking the output of the following commands in a new terminal window:

```
python -VV
py -VV
```

Both of these commands should display the latest Python version, 3.10.

For local testing with multiple Python versions,
repeat these steps for the latest bugfix releases of Python 3.7+,
with the following changes:

- Do _not_ enable the option to add Python to the `PATH` environment variable.
- `py -VV` and `python -VV` should still display the version of the latest stable release.
- `py -X.Y -VV` (e.g. `py -3.7 -VV`) should display the exact version you just installed.

Note that binary installers are not provided for security releases.

### Getting Python (Mac, Linux, Unix)

If you're on a Mac, Linux, or Unix system,
use [pyenv] for installing and managing Python versions.
Please refer to the documentation of this project
for detailed installation and usage instructions.
(The following instructions assume that
your system already has [bash] and [curl] installed.)

Install [pyenv] like this:

```console
$ curl https://pyenv.run | bash
```

Add the following lines to your `~/.bashrc`:

```sh
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Install the Python build dependencies for your platform,
using one of the commands listed in the [official instructions][pyenv wiki].

Install the latest point release of every supported Python version.
This project template supports Python 3.7, 3.8, 3.9, and 3.10.

```console
$ pyenv install 3.7.12
$ pyenv install 3.8.12
$ pyenv install 3.9.10
$ pyenv install 3.10.2
```

After creating your project (see [below](creating-a-project)),
you can make these Python versions accessible in the project directory,
using the following command:

```console
$ pyenv local 3.10.2 3.9.10 3.8.12 3.7.12
```

The first version listed is the one used when you type plain `python`.
Every version can be used by invoking `python<major.minor>`.
For example, use `python3.7` to invoke Python 3.7.

### Requirements

:::{note}
It is recommended to use [pipx] to install Python tools
which are not specific to a single project.
Please refer to the official documentation
for detailed installation and usage instructions.
If you decide to skip `pipx` installation,
use [pip install] with the `--user` option instead.
:::

You need four tools to use this template:


Install [Nox] and [nox-poetry] using pipx:

```console
$ pipx install nox
$ pipx inject nox nox-poetry
```

Remember to upgrade these tools regularly:

```console
$ pipx upgrade cookiecutter
$ pipx upgrade --include-injected nox
$ poetry self update
```

## Project creation

(creating-a-project)=

### Creating a project

Create a project from this template
by pointing Cookiecutter to its [GitHub repository][hypermodern python cookiecutter].
Use the `--checkout` option with the [current stable release][2022.6.3]:

```console
$ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python --checkout="2022.6.3"
```

Cookiecutter downloads the template,
and asks you a series of questions about project variables,
for example, how you wish your project to be named.
When you have answered these questions,
your project is generated in the current directory,
using a subdirectory with the same name as your project.

Here is a complete list of the project variables defined by this template:

:::{list-table} Project variables
:header-rows: 1
:widths: auto

- - Variable
  - Description
  - Example
- - `project_name`
  - Project name on PyPI and GitHub
  - `hypermodern-python`
- - `package_name`
  - Import name of the package
  - `hypermodern_python`
- - `friendly_name`
  - Friendly project name
  - `Hypermodern Python`
- - `author`
  - Primary author
  - Katherine Johnson
- - `email`
  - E-mail address of the author
  - katherine@example.com
- - `github_user`
  - GitHub username of the author
  - `katherine`
- - `version`
  - Initial project version
  - `0.0.0`
- - `copyright_year`
  - The project copyright year
  - `2022`
- - `license`
  - The project license
  - `MIT`
- - `development_status`
  - Development status of the project
  - `Development Status :: 3 - Alpha`

:::

:::{note}
The initial project version should be the latest release on [PyPI],
or `0.0.0` for an unreleased package.
See [The Release workflow] for details.
:::
