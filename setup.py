import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsql-django",
    version="0.0.1",
    author="JSQL Sp. z o.o.",
    author_email="office@jsql.it",
    description="JSQL backend plugin for Django app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.jsql.it",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
)