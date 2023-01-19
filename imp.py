from links import *
import os

import subprocess
from urllib.request import *
from hachoir.parser import createParser
from datetime import datetime

def multirec(client, message, channel, url, title, lang)
    f1 = 'ffmpeg -y -i'
    f2 = f'{url} -ss {s} -to {s2}'
    f3 = '-map 0:v:0 -map 0:a -metadata:s:a title=f'tn' -c copy'
    output = f'{title} {channel} [{lang}] [H264]_Tony.mkv'
    merge = f1.split() + [url] + f2.split() + f3.split() + [output]

subprocess.run(merge)

return output 
