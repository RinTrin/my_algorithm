import os
import argparse
import subprocess

def makedir(path):
    if os.path.exists(path):
        print('WRONG NUMBER')
        print('TRY AGAIN')
    else:
        os.makedirs(path)

def make_args():
    parser = argparse.ArgumentParser(description='make atcoder files faster')    # 2. パーサを作る

    parser.add_argument('--org_path', default='/home/kento/tomita/my_algorithm/atco')
    parser.add_argument('-n', '--num', default=None)   # よく使う引数なら省略形があると使う時に便利

    args = parser.parse_args()
    return args

def main(args):
    dir_path = os.path.join(args.org_path, str(args.num))
    makedir(dir_path)

    for al in ['a', 'b','c','d','e']:
        file_path = os.path.join(dir_path, al+'.py')
        with open(file_path, 'w') as f:
            f.write('')


if __name__ == '__main__':
    args = make_args()
    main(args)
    # subprocess.run(["cd", str(os.path.join(args.org_path, str(args.num)))], shell=True)
    # res.stdout.decode("utf8")

