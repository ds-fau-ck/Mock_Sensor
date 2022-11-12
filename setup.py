from setuptools import setup
AUTHOR_USER_NAME = "Kulakirti Chakma"
SRC_REPO = "Sensor"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    author_email="kirticse.chakma869@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)