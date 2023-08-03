import setuptools

setuptools.setup(
    name="install-requirements",
    version="1.0",
    install_requires=[
        line.strip() for line in open("requirements.txt") if not line.startswith("#")
    ],
)
