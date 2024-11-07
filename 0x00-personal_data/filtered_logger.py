#!/usr/bin/env python3
"""
Module for filtering log messages.
"""

import logging
import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): String to replace the field values with.
        message (str): The log message to be obfuscated.
        separator (str): The character separating fields in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = '|'.join(
        [f'{field}=[^{separator}]*' for field in fields]
    )
    return re.sub(
        pattern,
        lambda m: f'{m.group(0).split("=")[0]}={redaction}',
        message
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)


PII_FIELDS = ('email', 'phone_number', 'ssn', 'credit_card', 'dob')


def get_logger() -> logging.Logger:
    """
    Creates and returns a logging.Logger object with specific configurations.

    Returns:
        logging.Logger: Configured logger with a RedactingFormatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create stream handler
    handler = logging.StreamHandler()

    # Set formatter for the handler
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(handler)

    return logger
