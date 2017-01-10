#!/usr/bin/python

import io
import yaml
import os
import sys

TMPFILE="/tmp/defaul_repos.yaml"

MOS92_UPDATES_REPOS = [
    {
        "name": "mos9.2-updates",
        "priority": 1050,
        "section": "main restricted",
        "suite": "mos9.0-updates",
        "type": "deb",
        'uri': "http://mirror.fuel-infra.org/mos-repos/ubuntu/9.2/",
    },
    {
        "name": "mos9.2-security",
        "priority": 1050,
        "section": "main restricted",
        "suite": "mos9.0-security",
        "type": "deb",
        'uri': "http://mirror.fuel-infra.org/mos-repos/ubuntu/9.2/",
    },
    {
        "name": "mos9.2-holdback",
        "priority": 1100,
        "section": "main restricted",
        "suite": "mos9.0-holdback",
        "type": "deb",
        'uri': "http://mirror.fuel-infra.org/mos-repos/ubuntu/9.2/",
    },
]

def repo_exists(repos,name):
    for repo in repos:
        if 'name' in repo:
            if repo['name']==name:
                return True
    return False

def run_or_die(cmd):
    if os.system(cmd)!=0:
        sys.exit(cmd + "has been failed with")

def main():
    for release in [2,3]:
        run_or_die("fuel2 release repos list {} -f yaml > {}".format(release, TMPFILE))

        with io.open(TMPFILE, "r") as ifile:
            data=yaml.load(ifile)
        
        for repo in MOS92_UPDATES_REPOS:
            if not repo_exists(data, repo["name"]):
                data.append(repo)

        with io.open(TMPFILE, "w") as ofile:
            yaml.dump(data,ofile, default_flow_style=False)

        run_or_die("fuel2 release repos update -f {} {}".format(TMPFILE, release))

if __name__ == '__main__':
    main()
