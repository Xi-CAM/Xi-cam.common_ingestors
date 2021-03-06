from setuptools import setup, find_namespace_packages
from codecs import open
from os import path


__version__ = "0.1.0"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="xicam.common_ingestors",
    version=__version__,
    description="",
    long_description=long_description,
    url="",
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    keywords="Xi-cam, ingestors",
    packages=find_namespace_packages(exclude=["docs", "tests*"]),
    include_package_data=True,
    author="Ron Pandolfi",
    install_requires=["fabio"],
    author_email="ronpandolfi@lbl.gov",
    entry_points={
        "databroker.ingestors": [
            "image/jpeg = xicam.common_ingestors.generic:ingest_jpeg",
            "image/tiff = xicam.common_ingestors.generic:ingest_tiff",
        ],
    },
)
