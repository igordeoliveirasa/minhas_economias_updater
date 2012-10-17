__author__ = 'igor.sa'

import os
from stat import S_ISREG, ST_CTIME, ST_MODE

def get_last_created_file(dir_path, extension=".*"):
    dirlist = os.listdir(dir_path)
    max_ctime = 0;
    last_downloaded_fp = ""

    for fp in dirlist:

        if extension != ".*":

            if os.path.splitext(fp)[1] != extension:
                continue

        info = os.stat(os.path.join(dir_path, fp))
        ctime = info[ST_CTIME]
        if max_ctime < ctime:
            max_ctime = ctime
            last_downloaded_fp = fp

    return os.path.join(dir_path, last_downloaded_fp)
