import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jes4py",
    version="0.1.1",
    author="Jonathan Senning",
    author_email="jonathan.senning@gordon.edu",
    description="Python 3.x package providing a subset of JES's media functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gordon-cs/JES4py",
    packages=['jes4py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0.0',install_requires=[
        'wave',
        'wxPython',
        'simpleaudio'
    ],
    package_data={
        'jes4py': ['images/Left.png','images/Right.png'],
    },

)
