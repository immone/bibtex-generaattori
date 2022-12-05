"""Run app."""
from init import app
import routes  # pylint: disable=unused-import

class App:
    def main():
        app.run()

if __name__ == '__main__':
    app = App()
    app.main()
