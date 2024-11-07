#!/usr/bin/env python3
"""
Module to filter log messages and connect to a MySQL database.
"""

import logging
import os
import mysql.connector
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
    """Formatter for redacting log fields."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)


# PII fields to redact
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_db():
    """
    Returns a MySQL database connection.
    """
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    if not db_name:
        raise ValueError("Database name is required.")

    return mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )


def get_logger() -> logging.Logger:
    """
    Configures and returns a logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def main():
    """
    Logs user data from the database with filtered PII.
    """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    for row in cursor:
        log_message = (
            f"name={row[0]}; email={row[1]}; phone={row[2]}; "
            f"ssn={row[3]}; password={row[4]}; ip={row[5]}; "
            f"last_login={row[6]}; user_agent={row[7]}"
        )
        logger.info(log_message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
