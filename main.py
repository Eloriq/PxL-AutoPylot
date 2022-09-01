import argparse
import json
import sys

from pxlautopylot.autopilot import Autopilot


def main():
    parser = argparse.ArgumentParser(
        description='PxL-AutoPylot : Automate your Windows inputs by monitoring your pixels.')
    parser.add_argument('file', help='a JSON configuration file')
    parser.add_argument('-r', '--run', action='store_true', help='run the given JSON configuration file')
    parser.add_argument('-c', '--check', action='store_true', help='check the given JSON configuration file')
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        try:
            j = json.load(f)
            a = Autopilot(**j)
            if args.check:
                print("Configuration file is JSON valid.")
            if args.run:
                a.launch()
            return 0
        except ValueError as err:
            print("Configuration file is not JSON valid.")
            print(err)
            return 1


if __name__ == '__main__':
    sys.exit(main())
