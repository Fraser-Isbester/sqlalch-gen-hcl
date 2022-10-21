import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlalchemy2atlas",
    version="0.0.1",
    author="Fraser Isbester",
    description="Converts SQLALchemy Base Classes to AtlasGo HCL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    py_modules=["sqlalchemy2atlas"],
    package_dir={"": "quicksample/src"},
    install_requires=[
        "docker>=6.0",
        "psycopg2==2.9",
    ],
)
