import os
import os.path
import time
import requests
import shutil


def is_dir_empty(dir_path):
    return not bool(os.listdir(dir_path))


def _merge(filedir, output):
    print('Start merge path : %s ' % filedir)
    filelist = os.listdir(filedir)
    with open(output, 'w', encoding='utf-8') as f:
        for filename in filelist:
            filepath = filedir + '/' + filename
            for line in open(filepath, encoding='utf-8'):
                f.writelines(line)
            f.write('\n')


def _download(url, outdir):
    print('Start download file from url %s ' % url)
    filename = outdir + '/' + os.path.basename(i)
    res = requests.get(url)
    with open(filename, 'wb') as f:
        print('encoding : %s' % res.encoding)
        f.write(res.content)


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
        'https://raw.githubusercontent.com/nickspaargaren/no-google/master/pihole-google.txt',
        'https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/all.txt',
        'https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/skyrules.txt',
        'https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/ok.txt'
    ]
    rule_dir = os.getcwd()+'/rules'
    # 判断文件夹是否为空
    if os.path.exists(rule_dir):
        print('rules dir exist, delete : %s' % rule_dir)
        shutil.rmtree(rule_dir)
    os.mkdir(rule_dir)
    print('rules dir empty, create : %s' % rule_dir)
    # 下载
    for i in list:
        print('URI: %s' % i)
        _download(i, rule_dir)
        print('URI download done: %s' % i)

    # 合并
    _merge(rule_dir, 'merge.txt')
    # 结束
    end = time.process_time()
    print('Running time : %s Seconds' % (end-start))
