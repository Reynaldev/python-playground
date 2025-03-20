#!/usr/bin/env python

import sys
import subprocess

def change_content(filename: str):
    text = []

    with open(filename, "r") as f:
        for line in f.readlines():
            text.append("SIG" + line.strip())

    with open("new_" + filename, "w") as f:
        f.write("\n".join(text))

    return text

content = change_content(sys.argv[1])
print(content)
