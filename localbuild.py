#! /usr/bin/env python3
""" Script for managing local builds and installations """

import os
import sys
import shlex
import argparse
import subprocess

import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_localbuild():
    filename = ".localbuild"
    with open(filename) as f:
        return yaml.load(f, Loader=Loader)


def run_command(string):
    if not string:
        print("Command empty, skipping...", file=sys.stderr)
        return
    print(string)
    os.system(string)
    print()


def update(localbuild):
    print("Updating...")
    command = localbuild.get("update")
    run_command(command)


def setup(localbuild):
    print("Setting up...")
    command = localbuild.get("setup")
    run_command(command)


def build(localbuild):
    print("Building...")
    command = localbuild.get("build")
    run_command(command)


def install(localbuild):
    print("Installing...")
    command = localbuild.get("install")
    run_command(command)


def uninstall(localbuild):
    print("Uninstalling...")
    command = localbuild.get("uninstall")
    run_command(command)


def clean(localbuild):
    print("Cleaning...")
    command = localbuild.get("build")
    run_command(command)


COMMANDS = {
    "update": update,
    "setup": setup,
    "build": build,
    "install": install,
    "uninstall": uninstall,
    "clean": clean,
}


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("commands", nargs="*", default=[])
    args = parser.parse_args()
    valid_commands = set(COMMANDS.keys())
    for c in args.commands:
        if c not in valid_commands:
            raise ValueError(f"Invalid command: {c}")
    if not args.commands:
        args.commands = ["update", "setup", "build", "install"]
    return args


def main():
    args = parse_arguments()

    localbuild = load_localbuild()

    for command in args.commands:
        func = COMMANDS[command]
        func(localbuild)


if __name__ == "__main__":
    main()
