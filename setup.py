import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("HISTORY.md", "r") as fh:
    history = fh.read()

setuptools.setup(
    name="espressomaker-rmoralesdelgado",
    version="0.1a2",
    author="Raul Morales Delgado",
    author_email="rmoralesdelgado@gmail.com",
    description="Allows to temporarily modify the power management settings on a MacOS to run processes uninterruptedly.",
    long_description=long_description + history,
    long_description_content_type="text/markdown",
    url="https://github.com/rmoralesdelgado/espressomaker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.5',
)
