import os
from flask import Flask
from app import create_app

app = create_app()

if __name__ == '__main__':
    """
    This is the entry point for the application.
    """
    if os.environ.get('PORT') is None:
        port = 5000
    else:
        port = os.environ.get('PORT')

    app.run(host='0.0.0.0', port=port)