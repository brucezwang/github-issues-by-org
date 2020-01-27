'''
Pulls all issues for a certain github repository that have been raised by
members of specified organization
'''

import os
import sys

from github import Github
from dotenv import load_dotenv

if  not os.path.exists('.env'):
	print("no file named .env found", file=sys.stderr)
	sys.exit(1)
elif len(sys.argv) != 3:
	print("Usage: ./pull_issues.sh <repository name> <organization name>\nExample: ./pull_issues.sh DataDog/Gello DataDog")
	sys.exit(0)

gh = None
load_dotenv(verbose=True)

if 'GITHUB_USERNAME' in os.environ and 'GITHUB_PASSWORD' in os.environ:
	gh = Github(os.getenv("GITHUB_USERNAME"), os.getenv("GITHUB_PASSWORD"))
elif 'GITHUB_ACCESS_TOKEN' in os.environ:
	gh = Github(os.getenv("GITHUB_ACCESS_TOKEN"))
else:
	print(".env file does not have enough information", file=sys.stderr)
	sys.exit(1)

repo_name = sys.argv[1]
repo_issues = gh.get_repo(repo_name).get_issues(state='open')

org_name = sys.argv[2]
org_members = gh.get_organization(org_name).get_members()

# Pagination making this really slow, can try to pull all at once and internally buffer later

members = set()
for member in org_members:
	members.add(member.login)

for issue in repo_issues:
	if issue.user.login in members:
		print(issue)