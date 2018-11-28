import datetime
import os
import re
import subprocess
from subprocess import Popen

import pandas as pd

from configs import filename

test_line = 'Ping: 8.945 ms\nDownload: 39.57 Mbit/s\nUpload: 6.23 Mbit/s\n'


def main():
    def find_match(line, prefix):
        regex = '(%s: ([0-9]{1,}.[0-9]{1,}))' % prefix
        return re.findall(regex, str(line))[0][1]

    def write_results(time_of_test, ping, download, upload):
        prepare_new_file_if_not_exists()
        f = open(filename, 'a')
        f.write('\n%s,%s,%s,%s' % (time_of_test, ping, download, upload))
        f.close()

    def prepare_new_file_if_not_exists():
        if not os.path.isfile(filename):
            f = open(filename, 'w')
            f.write('time,ping,download,upload')
            f.close()

    results = Popen('speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()
    ping = find_match(results, 'Ping')
    download = find_match(results, 'Download')
    upload = find_match(results, 'Upload')
    time_of_test = datetime.datetime.now().isoformat()
    print('Date/Time: %s Ping: %s Download: %s Upload: %s' % (time_of_test, ping, download, upload))
    write_results(time_of_test=time_of_test, ping=ping, upload=upload, download=download)


if __name__ == '__main__':
    main()