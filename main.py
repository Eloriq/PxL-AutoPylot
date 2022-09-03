import argparse
import errno
import json
import sys

from pxlautopylot.autopilot import Autopilot
from pxlautopylot.sandbox import Sandbox


def check(file):
    with open(file, 'r') as f:
        try:
            j = json.load(f)
            a = Autopilot(**j)
            print("Configuration file is JSON valid.")
            return 0
        except ValueError as ve:
            print("Configuration file is not JSON valid.")
            return 1
        except TypeError as te:
            print(te)
        except IOError as ioe:
            if ioe.errno == errno.ENOENT:
                print('Configuration file not found')
            elif ioe.errno == errno.EACCES:
                print('Permission denied on configuration file')


def run(file):
    with open(file, 'r') as f:
        try:
            j = json.load(f)
            a = Autopilot(**j)
            a.launch()
            return 0
        except (IOError, ValueError, TypeError) as e:
            print("Could not run configuration. Please check your file.")
            return 1


def sandbox(n):
    sandbox_o = Sandbox(n)
    sandbox_o.run()


def autopilot_parser():
    parser = argparse.ArgumentParser(
        description='PxL-AutoPylot : Automate your Windows inputs by monitoring your pixels.')
    subparsers = parser.add_subparsers(help='commands', dest='command')
    run_parser = subparsers.add_parser("run", help="run your config file")
    sandbox_parser = subparsers.add_parser('sandbox', help='get information about your pixels')
    # RUN
    run_parser.add_argument('-c', '--check', action='store_true', help='check the given JSON configuration file')
    run_parser.add_argument('file', help='a JSON configuration file')
    # SANDBOX
    sandbox_parser.add_argument("n", type=int, default=0, help='number of pixels to describe')
    return parser


def main():
    args = autopilot_parser().parse_args()
    command = args.command
    if command == 'run':
        if args.check:
            return check(args.file)
        else:
            return run(args.file)
    if command == 'sandbox':
        sandbox(args.n)


if __name__ == '__main__':
    sys.exit(main())
