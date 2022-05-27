# codding: utf-8
"""
Template for creating a logger.
"""
import logging
import logging.handlers


def make_logger(log_file=None, name=None):
    """
    Create a Logger (console, and optionally file).

    :param log_file: optional - full path of the log  file.
    :param name: optional - name of the logger.
    :return: a Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")

    if log_file is not None:
        file_handler = logging.FileHandler(log_file, mode="w")  # mode = "a" in order to append to an existing log_file
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

def write_header(logger, verbosity):
    logger.info("#################################################")
    logger.info("START")
    logger.debug("Verbosity set to {}".format(verbosity))
    logger.info("#################################################")

def write_main_content(logger, verbosity):
    logger.info("Interesting stuff written here.")

def write_error(logger, verbosity):
    logger.error("Something wrong happened...")

def write_footer(logger):
    logger.info("#################################################")
    logger.info("END")
    logger.info("#################################################")


if __name__ == "__main__":

    log_file = "/tmp/dummy_logs.log"
    verbosity = 1

    logger = make_logger(log_file)
    write_header(logger, verbosity)
    write_main_content(logger, verbosity)
    write_error(logger, verbosity)
    write_footer(logger)