import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pfsc-examp",
    version="0.22.7-pre",
    license="Apache 2.0",
    url="https://github.com/alpinemath/pfsc-examp",
    description="Example explorers for Proofscape",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)

