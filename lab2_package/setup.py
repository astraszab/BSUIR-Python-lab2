import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lab2_astraszab",
    version="0.0.1",
    author="Uladzislau Astraszab",
    author_email="u.astraszab@gmail.com",
    description="BSUIR Python lab2 package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astraszab/BSUIR-Python-lab2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
