import os
from setuptools import setup, find_packages


def read(fname):
    """Reads a file's contents as a string.
    Args:
        fname: Filename.
    Returns:
        File's contents.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = "0.1"
BASE_URL = "https://github.com/atine/dmc2gymnasium"
INSTALL_REQUIRES = ["gymnasium>=0.26.3"]

setup(
    name="dmc2gymnasium",
    version=VERSION,
    description="Gymnasium integration for the DeepMind Control (DMC) suite",
    long_description=read("README.md"),
    author="Jen-Yen Chang",
    author_email="chou@mi.t.u-tokyo.ac.jp",
    license="MIT",
    url=BASE_URL,
    packages=find_packages(),
    zip_safe=True,
    install_requires=INSTALL_REQUIRES,
)
