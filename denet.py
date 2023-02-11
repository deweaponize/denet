import sys
import os

from pathlib import Path

ROOT_PATH = Path.cwd()


def make_package(suite: str, package: str):
    os.mkdir(os.path.join(ROOT_PATH, "suites", suite), package)

    for i in [f"{package}.py", f"{package}.run"]:
        with open(os.path.join(ROOT_PATH, "suites", suite, package, i)) as file:
            pass


def install(suite: str, package: str):
    pass


def build():
    pass


if __name__ == "__main__":
    if sys.argv[1] == 'make-package':
        make_package(
            suite=sys.argv[2],
            package=sys.argv[3]
        )
    elif sys.argv[1] == 'install':
        install(
            suite=sys.argv[2],
            package=sys.argv[3]
        )
    elif sys.argv[1] == 'build':
        build()
    else:
        print("not a valid command")
