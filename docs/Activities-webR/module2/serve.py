#!/usr/bin/env python3
"""
serve.py — local server for module2_practical.html
────────────────────────────────────────────────────
Required for Firefox (Chrome / Edge work without this).

Firefox needs the page served over http:// with two security headers
so that WebAssembly shared memory (SharedArrayBuffer) is allowed:
  Cross-Origin-Opener-Policy:   same-origin
  Cross-Origin-Embedder-Policy: require-corp

Usage
─────
  Double-click this file,  OR
  python serve.py          OR
  python3 serve.py

Then open:  http://localhost:8000/module2_design_activities.html

Press Ctrl+C in this window to stop the server.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

FILE = "module2_design_activities.html"
PORTS_TO_TRY = [8000, 8001, 8080, 8888, 9000]


class COIHandler(http.server.SimpleHTTPRequestHandler):
    """Serve files with Cross-Origin Isolation headers."""

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # suppress per-request noise


def find_free_port(candidates):
    """Return the first port in candidates that is not already in use."""
    import socket
    for port in candidates:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port   # bind succeeded → port is free
            except OSError:
                continue
    return None


def main():
    # Always serve from the folder containing this script,
    # regardless of where the user ran it from.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    port = find_free_port(PORTS_TO_TRY)

    if port is None:
        print(f"\n  Could not find a free port.")
        print(f"  Tried: {PORTS_TO_TRY}")
        print(f"  Close other applications and try again.\n")
        input("Press Enter to exit...")
        sys.exit(1)

    url = f"http://localhost:{port}/{FILE}"

    try:
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("", port), COIHandler) as httpd:
            print(f"\n  Module 2 Practical — server running")
            print(f"  ────────────────────────────────────")
            print(f"  Open this in Firefox (or any browser):")
            print(f"\n      {url}\n")
            print(f"  Serving files from:  {script_dir}")
            print(f"  Press Ctrl+C to stop.\n")

            try:
                webbrowser.open(url)
            except Exception:
                pass

            httpd.serve_forever()

    except OSError as e:
        print(f"\n  Error starting server on port {port}: {e}\n")
        input("Press Enter to exit...")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n  Server stopped.\n")


if __name__ == "__main__":
    main()
