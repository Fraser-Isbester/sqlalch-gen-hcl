import setuptools
from os import environ

with open("README.md", "r") as fh:
    long_description = fh.read()

# Update this as part of your release cycle
version = "v0.0.0-dev0"

if environ.get("CI") and environ.get("VERSION_TAG"):
    version = environ["VERSION_TAG"]

setuptools.setup(
    name="sqlalchemy2atlas",
    version=version,
    author="Fraser Isbester",
    description="Converts SQLALchemy Base Classes to AtlasGo HCL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fraser-Isbester/sqlalchemy2atlas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    py_modules=["sqlalchemy2atlas"],
    install_requires=[
        "docker>=6.0",
        "psycopg2>=2.9",
        "SQLAlchemy>=1.4",
    ],
    entry_points={
        "console_scripts": [
            "sqlalchemy2atlas=sqlalchemy2atlas.sqlalchemy2atlas:main",
        ]
    },
)
