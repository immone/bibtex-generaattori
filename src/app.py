"""Run app."""
from init import app
import routes  # pylint: disable=unused-import

class App: # pylint: disable=too-few-public-methods
    """Main class of the app"""
    def __init__(self) -> None:
        pass

    def main(self):
        """Start the app"""
        app.run()

if __name__ == '__main__':
    app = App()
    app.main()
