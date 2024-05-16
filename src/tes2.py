import argparse
import sys

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # Customize your error message here
        sys.stderr.write(f'Error: {message}\n')
        self.print_help()
        sys.exit(2)

def main():
    parser = CustomArgumentParser(description='Load semua data dalam folder.')
    parser.add_argument('integers', metavar='folder', type=str, nargs='+', help='string nama folder berisikan database')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == '__main__':
    main()