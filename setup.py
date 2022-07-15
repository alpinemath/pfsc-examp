import setuptools

with open("README.md", "r") as fh:
    long_description = ''.join(fh.readlines()[1:])

setuptools.setup(
    name="pfsc-examp",
    version="0.22.7",
    license="Apache 2.0",
    url="https://github.com/alpinemath/pfsc-examp",
    description="Example explorers for Proofscape",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'lark067==0.6.7',
        'alpinemath-sympy>=0.10.3',
        'displaylang>=0.22.7',
        'pfsc-util>=0.22.7',
        'Jinja2>=3.0.3,<4',
        'MarkupSafe>=2.0.1,<3',
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)

