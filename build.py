import os
import json
from pathlib import Path
import re

CWD = Path.cwd()
BUILD_FILE = "build.json"


def parse(file_path: str) -> list:
    with open(file_path, 'r') as file:
        items = re.findall(r'<(.*?)>', str(file.read()))
    return items


def dir_structure_to_json(root_dir):
    result = dict()
    _suite = []
    _package = set()
    for suite in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, suite)):
            _suite.append(suite)
    result["suites"] = _suite

    for suite in _suite:
        result[suite] = dict()
        for i in os.listdir(os.path.join(root_dir, suite)):
            if os.path.isdir(os.path.join(root_dir, suite, i)):
                _package.add(i)
        result[suite]["package"] = list(_package)
        try:
            with open(os.path.join(root_dir, suite, "readme.md"), "r") as file:
                doc = file.read()
        except:
            doc = '''# documentation not found'''

        for package in _package:
            try:
                with open(os.path.join(root_dir, suite, package, 'readme.md', 'r')) as file:
                    package_doc = file.read()
            except:
                package_doc = '''# documentation not found'''

            run_script = os.listdir(os.path.join(CWD, "suites", suite, package))
            run_script = [i for i in run_script if "." not in i]
            result[suite][package] = {"commands": [i for i in os.listdir(os.path.join(root_dir, suite, package)) if "." not in i]}

            for commands in run_script:
                with open(os.path.join(CWD, "suites", suite, package, commands, f"{commands}.run")) as file:
                    exec_command = file.read()

                result[suite][package][commands] = {
                    "exec_command": str(exec_command),
                    "inputs": parse(os.path.join(CWD, "suites", suite, package, commands, f"{commands}.run"))
                }

            result[suite][package]["doc"] = doc

        result[suite]["doc"] = doc

    return json.dumps(result, indent=2)


if __name__ == "__main__":
    with open(os.path.join(CWD, "api", BUILD_FILE), "w") as build_file:
        build_file.write(dir_structure_to_json(
            root_dir="suites"
        ))
