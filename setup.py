import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfuseki",
    version="1.0.1",
    author="Bin Yu",
    author_email="yubin_SkyWalker@yeah.net",
    description="An easy way to mix together OWL and Jena Fuseki.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yubinCloud/pyfuseki",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Artistic License",
        "Operating System :: OS Independent",
    ],
    install_requires=['httpx', 'rdflib', 'pydantic', 'SPARQLWrapper'],
    python_requires='>=3.6',
)