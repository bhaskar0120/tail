def __exit (args):
    """Exit the program."""
    if len(args) > 0 and args[0].isnumeric():
        exit(int(args[0]))
    else:
        exit(0)
