from functools import wraps
from flask import request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def authentication_middleware(view_function):
    """
    Middleware that handles all authentication

    :param view_function: The view function to wrap
    :return: The wrapped view function
    """
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        """
        Decorator to authenticate requests

        :param view_function: The view function to wrap
        :return: The wrapped view function
        """
        if ('api-key' in request.headers and
            request.headers['api-key'] == API_KEY):

            return view_function(*args, **kwargs)

        return jsonify({"message": "Authentication failure"}), 401
    return decorated_function
