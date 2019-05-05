import argparse, os
from comms.dispatcher import Dispatcher

from comms import commands

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="An argparse example")

    # Arguments prefixed with - are optional
    parser.add_argument(commands.action, help='The action to take (e.g. init, add, etc.)')
    parser.add_argument(commands.node_name_short,commands.node_name_long, help='The node name being specified.', default=None)
    parser.add_argument(commands.archive_name_short,commands.archive_name_long, help='The node name being specified.', default=None)
    parser.add_argument(commands.node_type_short,commands.node_type_long, help='The node type being specified.', default=None)
    parser.add_argument(commands.message_short,commands.message_long, help='The node type being specified.', default="")

    args = parser.parse_args()

    Dispatcher.dispatch(os.getcwd()+"\\",args)
