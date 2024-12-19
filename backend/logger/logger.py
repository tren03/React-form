import logging

logging.basicConfig(
    format="%(levelname)s:%(message)s",
    filename="backend_logs.log",
    encoding="utf-8",
    level=logging.DEBUG,
)
custom_logger = logging.getLogger()
