#!/usr/bin/python

import sys
from fuelclient.objects.release import Release


ID = 3
NAME = 'Mitaka on Ubuntu+UCA 14.04'


class ReleasePatched(Release):
    def get_self(self):
        url = self.instance_api_path.format(self.id)
        return self.connection.get_request(url)

    def update_self(self, data):
        url = self.instance_api_path.format(self.id)
        self.connection.put_request(url, data)


def main():
    release = ReleasePatched(ID)
    data = release.get_self()

    if not data['name'] == NAME:
        sys.exit("Release with id 3 has unexpected name. "
                 "Expected name " + NAME)

    data['state'] = 'unavailable'

    release.update_self(data)


if __name__ == '__main__':
    main()
