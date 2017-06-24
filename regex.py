#!/usr/bin/env python3 

import re

#=================================================#
# split url
#=================================================#

def splitUrl(urldata):
    ''' split url
    
    split url on slash or ampersand
    '''
    localproxy = re.compile(r'^http://127.0.0.1[:0-9]?')
    rtmp = re.compile(r'^(rtmp|rtmpe)://')
    amp = re.compile(r'(?=[&][a-zA-Z_]+=+[-a-zA-Z0-9.]?)')
    if '|' in urldata:
        print("match |")
        udSplit = urldata.split(r'|')
        udSplitA = udSplit[0] # url before |
        udSplitB = udSplit[1] # url after |
        if not master(udSplitA):
            print("no")
            urlDict = {'url': udSplitA}
            print(urlDict)
        c= master(udSplitB)
        d = splitEquals(c)
        return d
    elif rtmp.match(urldata):
        print("rtmp")
        return urldata
    elif localproxy.match(urldata):
        print("localproxy")
        return urldata
    else:
        print("full url")
        urldata = {'url': urldata}
        return urldata

# split string on = and store in dict
def splitEquals(*args):
    return dict([v.split('=', 1) for v in args if '=' in v])

urlparams = ''

def match_func(pattern, urlparams):
    def match_rule(params):
        match = re.findall(pattern, params)
        if match:
            return match
        else:
            return params
    return match_rule
    
# regex dictionary
patterns = {
           'user-agent': 'u?User-a?Agent=[a-zA-Z0-9/.()\s,:;%+_-]+',
           'referer': 'r?Referer=[a-zA-Z0-9/.()\s,:;%+_-]+',
           'x-forward': 'X-Forwarded-For=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',
           'cookie': '[cC]ookie=[a-zA-Z0-9/&%_*~;=_\s]+'
           }

rules = [match_func(pattern, urlparams) for (pattern) in patterns.values()]

def master(urlparams):
    for match_func in rules:
        if match_func(urlparams):
             return match_func(urlparams)

# record function
def record(link, *args):
    arg2 = args[0:]
    strtuple = ' '.join(arg2)
    print(strtuple)
            
    print("ffmpeg -hide_banner -stats -v panic", strtuple, "-i", link, "-c:v copy -c:a copy $tflag $duration $recordingfile")
