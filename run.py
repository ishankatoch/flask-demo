import os
import click
from app import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6000)
