import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="df4loop",
    version="0.1.0",
    author="Daiki Katsuragawa",
    author_email="daikikatsuragawa@gmail.com",
    description="df4loop supports general purpose processe that requires a combination of both pandas.DataFrame and loop.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daikikatsuragawa/df4loop",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas>=1.0.0"
    ],
    license="Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
