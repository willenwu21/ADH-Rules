# -*- coding: utf-8 -*-
import os
import os.path
import time
import requests
import shutil

_base_dir = os.getcwd()
_rule_dir = _base_dir + '/rules'
_my_allow_f = 'my-allow.txt'
_merge_txt_f = 'merge.txt'
_download_list = [
    'https://easylist.to/easylist/easylist.txt',
    'https://raw.githubusercontent.com/easylist/easylistchina/master/easylistchina.txt',
    'https://easylist.to/easylist/easyprivacy.txt',
    'https://secure.fanboy.co.nz/fanboy-cookiemonster.txt',
    'https://github.com/badmojr/1Hosts/releases/download/latest/1hosts-Lite_adblock.txt',
    'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt',
    'https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt',
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/multi.txt',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    'https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt'
]


def _merge(rule_dir):
    print('Start merge path : %s ' % rule_dir)
    filelist = os.listdir(rule_dir)
    with open(_base_dir + '/' + _merge_txt_f, 'w', encoding='utf-8') as f:
        for filename in filelist:
            filepath = rule_dir + '/' + filename
            for line in open(filepath, encoding='utf-8'):
                f.writelines(line)
            f.write('\n')


def _merge_allow(file1, file2):
    f1 = open(file1, 'a+', encoding='utf-8')
    with open(file2, 'r', encoding='utf-8') as f2:
        f1.write('\n')
        for i in f2:
            f1.write(i)


def _check_rule_dir(rule_dir):
    if not os.path.exists(rule_dir):
        os.mkdir(rule_dir)
        print('rules dir empty, create : %s' % rule_dir)


def _download(file_list, rule_dir):
    _check_rule_dir(rule_dir)
    for i in file_list:
        print('Start download file from url %s ' % i)
        filename = _rule_dir + '/' + os.path.basename(i)
        res = requests.get(i)
        with open(filename, 'wb') as f:
            f.write(res.content)


def _clean_rule_dir(rule_dir):
    if os.path.exists(rule_dir):
        print('rules dir exist, delete : %s' % rule_dir)
        shutil.rmtree(rule_dir)


if __name__ == '__main__':
    # Start
    start = time.process_time()
    _download(_download_list, _rule_dir)
    # merge download rules
    _merge(_rule_dir)
    # merge my-allow
    _merge_allow(_base_dir + '/' + _merge_txt_f, _base_dir + '/' + _my_allow_f)
    # clean rules dir
    _clean_rule_dir(_rule_dir)
    # end
    end = time.process_time()
    print('Running time : %s Seconds' % (end-start))
