import argparse
from deposit_api.deposit import Deposit
from deposit_api import __version__


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('deposit_api')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    parser.add_argument('--new-session', action='store_true', dest="new")
    parser.add_argument('--email', action='store', default='w3_pdb05@localhost', dest="email")
    return parser

def main(args=None):
    """
    Main entry point for your project.

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    if args.new:
        d = Deposit(email=args.email)
        d.new()


if __name__ == '__main__':
    main()