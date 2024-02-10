from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="math2",
    version="0.1.0",
    author="hick",
    author_email="hick@example.com",
    description="A simple math package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henriqueos98/math2",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)