import logging

# Create a logger
custom_logger = logging.getLogger()

# Set up the log format
log_format = "%(levelname)s:%(message)s"

# Create a file handler to write logs to a file
file_handler = logging.FileHandler("backend_logs.log", encoding="utf-8")
file_handler.setFormatter(logging.Formatter(log_format))

# Create a stream handler to output logs to the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(log_format))
custom_logger.addHandler(file_handler)
custom_logger.addHandler(stream_handler)  # for console

custom_logger.setLevel(logging.DEBUG)
