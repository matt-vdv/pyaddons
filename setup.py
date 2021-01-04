import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyaddons", # Replace with your own username
    version="0.0.5",
    author="Matt H",
    author_email="matt.hu1@outlook.com",
    description="A collection of addons for the Python programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matt-hu/pyaddons",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)