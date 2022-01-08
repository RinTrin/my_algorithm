import os
import argparse
import subprocess

def makedir(path):
    if os.path.exists(path):
        print('WRONG NUMBER')
        print('TRY AGAIN')
        raise IndexError
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

    file_paths = []

    input_strs =  "N = int(input()) \n"
    input_strs += "N, M = map(int, input().split()) \n"
    input_strs += "p_list = list(map(int, input().split())) \n"
    input_strs += "xy_matrix = [list(map(int, input().split())) for _ in range(N)] \n"

    for al in ['a', 'b','c','d','e']:
        file_path = os.path.join(dir_path, al+'.py')
        file_paths.append(file_path)
        with open(file_path, 'w') as f:
            f.write(input_strs)

    return file_paths

if __name__ == '__main__':
    args = make_args()
    fls = main(args)
    for fl in fls:
        subprocess.run(["code", fl], shell=False)
    # res.stdout.decode("utf8")

