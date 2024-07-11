import setuptools

VERSION = "1.0.2" 

NAME = "py-plugin-feeds"

def parse_requirements(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith('#')]
setuptools.setup(
    name=NAME,
    version=VERSION,
    description="Plugin Decentralized Oracle Price Feed Python Package",
    url="https://github.com/GoPlugin/py-plugin-feeds",
    project_urls={
        "Source Code": "https://github.com/GoPlugin/py-plugin-feeds",
    },
    author="Logeswaran",
    author_email="meta2web3@gmail.com",
    license="Apache License 2.0",
    classifiers=[
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=parse_requirements("requirements.txt"),
    packages=["py_plugin_feeds"],
    package_data={'': ['*.txt', '*.md', 'tests/*.py','abi/*','mapping/*'],},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)