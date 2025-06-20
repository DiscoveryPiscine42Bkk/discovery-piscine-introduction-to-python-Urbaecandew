# aff_first_param.py

import sys

def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        print(sys.argv[1])

if __name__ == "__main__":
    main()
