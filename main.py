import sys

sys.path.append("./lib")
from lib.app import Application

if __name__ == '__main__':
    app = Application(sys.argv[1])
    app.start()