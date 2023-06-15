import argparse
import os


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


parser = argparse.ArgumentParser()
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-s", "--sum", action="store_true", help="first arg", required=False)
group1.add_argument("-d", "--dir", action="store_true", help="first arg", required=False)
parser.add_argument("-l", "--long", action="store_true", help="first arg", required=False)
parser.add_argument("x", type=str, help="first arg")
parser.add_argument("y", nargs="?", default=None)
args = parser.parse_args()

if args.sum:
    print(int(args.x) + int(args.y))
elif args.dir:
    if args.long:
        for dir in os.listdir(args.x):
            item_path = os.path.join(args.x, dir)
            print(dir, get_dir_size(item_path))
            # print(dir, os.path.getsize(dir))
    else:
        print(*os.listdir(args.x))

