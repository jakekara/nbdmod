import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbmod", 
    version="0.0.1",
    author="Jake Kara",
    author_email="jake@jakekara.com",
    description="Prototype for notebook module system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakekara/nbmod",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
