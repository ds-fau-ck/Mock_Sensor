from setuptools import find_packages,setup

setup(
    name="Sensor",
    version="0.0.1",
    author="kulkirti Chakma",
    author_email="kirticse.chakma869@gmail.com",
    package=find_packages(),
    install_requires=["numpy","matplotlib","mysql"],
)