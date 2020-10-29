import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="margo-loader", 
    version="0.0.1",
    author="Jake Kara",
    author_email="jake@jakekara.com",
    description="Import Jupyter notebooks using Margo notebook margin notebook syntax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakekara/nbdmod",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      'margo-parser==0.0.1',
      'nbformat==5.0.7'
    ],
    dependency_links=[
        'git+ssh://git@github.com/jakekara/nbdl.git#egg=margo-parser-0.0.1',
    ],
    python_requires='>=3.6',
)
