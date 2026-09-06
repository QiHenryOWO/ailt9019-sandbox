"""Plane Shooter - a tiny browser game.

Run this file and the game opens in your browser:

    python app.py

Uses only the Python standard library, so there is nothing to install.
Press Ctrl+C in the terminal to stop the server.
"""

import http.server
import os
import socketserver
import webbrowser

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    """Serves the game files from this folder."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        """Keep the terminal quiet so the score output is easy to read."""


def main():
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = "http://localhost:{}/".format(PORT)
            print("Plane Shooter is running at " + url)
            print("Press Ctrl+C to stop.")
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError:
        print("Port {} is already in use.".format(PORT))
        print("Another server may still be running - close it, then try again.")
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
