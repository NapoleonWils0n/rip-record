#!/usr/bin/env python3 

import shlex
import pipes
import os
import subprocess 
from datetime import datetime 

def ffmpeg(**kwargs):
    home = os.path.expanduser('~')
    desktop = '/Desktop/'
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ext = '.mkv'
    recordingfile = home + desktop + 'video-' + time + ext
    
    # get the values from the dictionary passed to the function
    values = list(kwargs.values())
    # url from kwargs which is the dictionary passed to the function
    url = kwargs['url']

    ffcmd = "ffmpeg -hide_banner -stats -v panic -i {0} -c:v copy -c:a copy {1}".format(url, recordingfile)

    if 'user-agent' or 'referer' or 'cookie' or 'x-forward' in kwargs:
        # dict minus first time which is the url
        options = values[1:]
        remove_bracket = str(options)[1:-1]
        options_join = ''.join(remove_bracket)
        ffcmd = "ffmpeg -hide_banner -stats -v panic {1} -i {0} -c:v copy -c:a copy {2}".format(url, options_join, recordingfile)
    
    if 'duration' in kwargs:
        tflag = kwargs['tflag']
        duration = kwargs['duration']
        # dict minus first time which is the url, and minus the last 2 items tflag and duration
        options = values[1:-2]
        remove_bracket = str(options)[1:-1]
        options_join = ''.join(remove_bracket)
        ffcmd = "ffmpeg -hide_banner -stats -v panic {1} -i {0} -c:v copy -c:a copy {2} {3} {4}".format(url, options_join, tflag, duration, recordingfile)
    

    ffsplit = shlex.split(ffcmd)
    print(ffsplit)

    #subpop = subprocess.Popen(ffcmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    #output = subpop.communicate()[0].decode()
