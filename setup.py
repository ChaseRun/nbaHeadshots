import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbaHeadshots",
    version="0.0.1",
    author="Chase Austin",
    author_email="chase7867@gmail.com",
    description="A package for downloading NBA player headshots from stats.NBA.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChaseAustin/nbaHeadshots",
    packages=setuptools.find_packages(),
       classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
)