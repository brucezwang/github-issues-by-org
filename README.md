# GitHub Issue Puller by Organization

Uses the GitHub API to show all open issues from a given repository raised by
members of a given organization.

## Setup:

Requires PyGithub and python-dotenv.

```bash
pyenv install 3.8.1
pyenv virtualenv 3.8.1 github-issues-by-org
pyenv activate github-issues-by-org
pipenv install
```

## Usage:

```bash
./pull_issues.sh <repository name> <organization name>
```

### Example:

```bash
./pull_issues.sh DataDog/Gello DataDog
```