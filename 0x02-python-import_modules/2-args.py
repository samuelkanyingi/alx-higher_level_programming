#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    if not args:
        print("0 arguments.")
    else:
        print(f"argument{'s' if len(args) > 1 else ''}: {len(args)}")
        for i, arg in enumerate(args, start=1):
            print(f"{i} : {arg}")
