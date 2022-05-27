# codding: utf-8
"""
Template for argument parsing.
"""


def main(positional_parameter_1, positional_parameter_2, debug, verbosity, log_file):
    print("Arguments are:")
    print("positional_parameter_1: {}".format(positional_parameter_1))
    print("positional_parameter_2: {}".format(positional_parameter_2))
    print("debug: {}".format(debug))
    print("verbosity: {}".format(verbosity))
    print("log_file: {}".format(log_file))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Dummy game.")
    # positional
    parser.add_argument("positional_parameter_1",
                        help="positional_parameter_1.")
    parser.add_argument("positional_parameter_2",
                        help="positional_parameter_2.")
    # optional
    parser.add_argument("-d", "--debug",
                        action="store_true",
                        help="output debug logs.")
    parser.add_argument("-v", "--verbosity",
                        type=int,
                        choices=[0, 1, 2],
                        default=0,
                        help="increase the output verbosity.")
    parser.add_argument("--log_file",
                        default=None,
                        help="file where the report of the game is dumped.")

    args = parser.parse_args()
    positional_parameter_1 = args.positional_parameter_1
    positional_parameter_2 = args.positional_parameter_2
    debug = args.debug
    verbosity = args.verbosity
    log_file = args.log_file

    main(positional_parameter_1, positional_parameter_2, debug, verbosity, log_file)