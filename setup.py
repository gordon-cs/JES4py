import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jes4py",
    version="0.0.3",
    author="Jonathan Senning",
    author_email="jonathan.senning@gordon.edu",
    description="A python package implementing part of JES's media functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gordon-cs/JES-emulator",
    packages=['jes4py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0.0',install_requires=[
    'wave',
    'wxPython',
    'simpleaudio'
    ]
)