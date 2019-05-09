#!/bin/python
"""Setup file for mtools."""

from setuptools import find_packages
from promebuilder import gen_metadata, setup
from promebuilder.utils import VERSIONFILE
from shutil import copyfile

# import version from mtools/version.py
with open('mtools/version.py') as f:
    exec(f.read())
with open(VERSIONFILE, "w") as fw:
    fw.write(__version__.split('-')[0])

# read README.rst for long_description content
copyfile('README.rst', 'README.md')


extras_requires = {
    "all": ['matplotlib==1.4.3', 'numpy==1.14.5', 'pymongo==3.6.1', 'psutil==5.4.2'],
    "mlaunch": ['pymongo==3.6.1', 'psutil==5.4.2'],
    "mlogfilter": [],
    "mloginfo": ['numpy==1.14.5'],
    "mlogvis": [],
    "mplotqueries": ['matplotlib==1.4.3', 'numpy==1.14.5'],
}


METADATA = gen_metadata(
    name="mtools",
    description=("Useful scripts to parse and visualize MongoDB log files, "
                 "launch test environments, and reproduce issues."),
    email="pytho_support@prometeia.com",
    url="https://github.com/prometeia/mtools",
    packages=sorted(set(find_packages()) - {'mtools/test'}),
    package_data={
        'mtools': ['data/log2code.pickle', 'data/index.html'],
    },
    entry_points={
        "console_scripts": [
            "mgenerate=mtools.mgenerate.mgenerate:main",
            "mlaunch=mtools.mlaunch.mlaunch:main",
            "mlogfilter=mtools.mlogfilter.mlogfilter:main",
            "mloginfo=mtools.mloginfo.mloginfo:main",
            "mlogvis=mtools.mlogvis.mlogvis:main",
            "mplotqueries=mtools.mplotqueries.mplotqueries:main"
        ],
    }
)

METADATA.update(dict(
    author='Thomas Rueckstiess',
    author_email='thomas@rueckstiess.net',
    license='Apache License 2.0 (Apache-2.0)',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Database',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='MongoDB logs testing',
    extras_require=extras_requires
))


if METADATA.get('conda_command_tests'):
    # Disabling for generic problem with mplotqueries
    METADATA['conda_command_tests'] = False


if __name__ == '__main__':
    setup(METADATA)