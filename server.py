"""
server.py — a small Python web server for Mathew Yves L. Nipay's portfolio.

Uses only Python's standard library (http.server), so there is nothing to
install. It serves the files in this folder (index.html, css/style.css)
exactly the way a real web server would.

HOW TO RUN
----------
1. Make sure Python 3 is installed:  python3 --version
2. From this folder, run:            python3 server.py
3. Open a browser to:                http://localhost:8000

Press Ctrl+C in the terminal to stop the server.
"""

import http.server
import os
import socketserver

PORT = 8000

# Always serve from the folder this script lives in, no matter where the
# command was run from.
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))


class PortfolioRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Serves files from SITE_ROOT and treats "/" as a request for index.html."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_ROOT, **kwargs)

    def log_message(self, format, *args):
        # Slightly friendlier console output than the default.
        print(f"[server] {self.address_string()} - {format % args}")


def main():
    with socketserver.TCPServer(("", PORT), PortfolioRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"Portfolio server running at {url}")
        print(f"Serving files from: {SITE_ROOT}")
        print("Open that address in your browser. Press Ctrl+C to stop.")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server...")


if __name__ == "__main__":
    main()

