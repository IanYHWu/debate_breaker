import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="debate_breaker_HerrHruby", # Replace with your own username
    version="1.0.0",
    author="Ian Wu",
    author_email="theplasmid2@gmail.com",
    description="A Python program to predict the break at a BP debating tournament",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HerrHruby/debate_breaker.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)