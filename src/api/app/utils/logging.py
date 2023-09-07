"""
Custom logger for our application. 
Will output logs in the following format: 
    {
        "message": "The message we want to send",
        "error": "The error message we want to log"
    }

Usage:
    from utils.logging import CustomLogger
    logger = CustomLogger(__name__)
    logger.info("This is an info message")
    logger.error("This is an error message", "This is the error message we want to log")
"""
import logging
import json

class CustomLogger:
    """
    Custom logger class that logs messages in a structured format.

    :param name: The name of the logger.
    """
    def __init__(self, name):
        """
        The constructor for the CustomLogger class.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def _structured_message(self, message, method, error="null"):
        """
        Format the message in a structured format.

        :param message: The message that we want to send.
        :param error: The error message we want to log.
        :return: The formatted message.
        """
        return json.dumps({"message": message, "method": method, "error": str(error)})

    def info(self, message, method):
        """
        Log an info message.

        :param message: The message that we want to send.
        """
        self.logger.info(self._structured_message(message, method))

    def error(self, message, method, error="An error occurred"):
        """
        Log an error message.

        :param message: The message that we want to send.
        :param error: The error message we want to log.
        """
        self.logger.error(self._structured_message(message, method, error))
