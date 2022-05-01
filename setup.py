import re

from setuptools import setup


version = ""
with open("nekos/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)


requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()


if not version:
    raise RuntimeError("version is not set")


setup(
    name="nekos.py",
    author="AlexFlipnote",
    url="https://github.com/Nekos-life/nekos.py",
    version=version,
    packages=["nekos"],
    license="GNU v3",
    description="A Python module that uses Nekos API",
    include_package_data=True,
    install_requires=requirements,
)
