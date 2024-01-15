import os
import os.path
import time
import requests
import shutil

_my_allow = 'my-allow.txt'
_merge_txt = 'merge.txt'
_base_dir = os.getcwd()
_rule_dir = _base_dir + '/rules'


def is_dir_empty(dir_path):
    return not bool(os.listdir(dir_path))


def _merge(filedir):
    print('Start merge path : %s ' % filedir)
    filelist = os.listdir(filedir)
    with open(_base_dir + '/' + _merge_txt, 'w', encoding='utf-8') as f:
        for filename in filelist:
            filepath = filedir + '/' + filename
            for line in open(filepath, encoding='utf-8'):
                f.writelines(line)
            f.write('\n')


def _merge_allow(file1, file2):
    f1 = open(file1, 'a+', encoding='utf-8')
    with open(file2, 'r', encoding='utf-8') as f2:
        f1.write('\n')
        for i in f2:
            f1.write(i)


def _download(url, outdir):
    print('Start download file from url %s ' % url)
    filename = outdir + '/' + os.path.basename(i)
    res = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(res.content)


def _clean_dir(rule_dir):
    # 判断文件夹是否为空
    if os.path.exists(rule_dir):
        print('rules dir exist, delete : %s' % rule_dir)
        shutil.rmtree(rule_dir)


if __name__ == '__main__':
    # 开始
    start = time.process_time()
    list = [
        'https://easylist-downloads.adblockplus.org/easylist.txt',
        'https://easylist-downloads.adblockplus.org/easylistchina.txt',
        'https://easylist-downloads.adblockplus.org/easyprivacy.txt',
        'https://github.com/badmojr/1Hosts/releases/download/latest/1hosts-Xtra_adblock.txt',
        'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt',
        'https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt',
        'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt',
        'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
        'https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/all.txt',
        'https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/skyrules.txt',
        'https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/ok.txt'
    ]
    rule_dir = os.getcwd()+'/rules'
    # 清理文件
    _clean_dir(_rule_dir)
    os.mkdir(_rule_dir)
    print('rules dir empty, create : %s' % _rule_dir)
    # 下载
    for i in list:
        print('URI: %s' % i)
        _download(i, _rule_dir)
        print('URI download done: %s' % i)

    # 合并
    _merge(_rule_dir)
    _merge_allow(_base_dir + '/' + _merge_txt, _base_dir + '/' + _my_allow)
    # 清理文件
    _clean_dir(rule_dir)
    # 结束
    end = time.process_time()
    print('Running time : %s Seconds' % (end-start))
