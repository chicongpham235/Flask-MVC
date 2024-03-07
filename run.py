from __init__ import app
import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-P", "--port", help="Port of backend Server", default=8000)
    args = parser.parse_args()
    port = args.port or 8000
    app.run(host="localhost", port=port, debug=True)