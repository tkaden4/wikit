import argparse
import wikipedia
import subprocess
import os

def get_pager():
    # TODO verify that pager program actually exists
    return os.environ.get("PAGER", "/usr/bin/less");

def view(args):
    page = wikipedia.page(args.name)
    pager = get_pager()
    process = subprocess.Popen(pager, stdin=subprocess.PIPE)
    process.communicate(input=page.content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="view and search for wikipedia articles in your terminal")
    subparser = parser.add_subparsers(help="commands")
    # parser for the 'view' subcommand for viewing articles
    view_parser = subparser.add_parser("view", help="find and view wikipedia articles")
    view_parser.add_argument("name", help="name of the wikipedia page")
    view_parser.set_defaults(func=view)
    # parse arguments and dispatch to subcommand
    args = parser.parse_args()
    args.func(args)
