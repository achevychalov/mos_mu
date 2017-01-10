#!/usr/bin/python

import sys
from fuelclient.objects.release import Release

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


def repo_exists(repos, name):
    for repo in repos:
        if 'name' in repo:
            if repo['name'] == name:
                return True
    return False


def run_or_die(cmd):
    if os.system(cmd) != 0:
        sys.exit(cmd + "has been failed with")


def main():
    for id in [2, 3]:
        r = Release(id)
        meta = r.get_attributes_metadata()
        data = meta['editable']['repo_setup']['repos']['value']

        for repo in MOS92_UPDATES_REPOS:
            if not repo_exists(data, repo["name"]):
                data.append(repo)

        r.update_attributes_metadata(meta)


if __name__ == '__main__':
    main()
