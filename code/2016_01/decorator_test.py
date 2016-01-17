#!/usr/bin/env python3

def mk_func():

    def _f():
        print("Hello")

    return _f


def main():
    abc = mk_func()
    abc()


if __name__ == "__main__":
    main()
