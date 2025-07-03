import argparse
import os
import humanize
parser = argparse.ArgumentParser()
parser.add_argument("path", help="Root directory to display")
parser.add_argument("--depth", type=int, default=-1, help="Max depth to traverse (-1 = unlimited)")
parser.add_argument("--show-hidden", action="store_true", help="Include hidden files")
parser.add_argument("--output", help="Save output to file")
parser.add_argument("--ztoa",action="store_true",)
args = parser.parse_args()

def main():
    print_tree(args.path,max_depth= args.depth)

def print_tree(path,prefix="",depth=0,max_depth=-1):
    if max_depth != -1 and depth > max_depth:
        return

    for i,entry in enumerate(sorted(os.listdir(path),reverse=True if args.ztoa else False)):
        if not args.show_hidden and entry[0] == '.':
            continue
        
        full_path = os.path.join(path,entry)
        connector = "└── " if i == len(os.listdir(path)) - 1 else "├── "

        if os.path.isdir(full_path):
            print(prefix+connector+f"📁 {entry}/")
            print_tree(full_path,prefix + ("    " if len(os.listdir(path))-1 == i else "|   "),depth+1,max_depth)
        else:
            try:
                size = os.path.getsize(full_path)
            except:
                size = 0
            print(prefix+connector+f"📄 {entry} ({humanize.naturalsize(size,binary=True)})/")
        

