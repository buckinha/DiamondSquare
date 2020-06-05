from setuptools import find_packages, setup


def get_version() -> str:
    with open('VERSION', 'r') as f:
        version = f.readline().strip()
    return version


def get_requirements() -> list:
    with open("requirements.txt", 'r') as f:
        requirements = [l.strip() for l in f]
    return requirements


setup(
    author="Hailey K Buckingham",
    author_email="hailey.k.buckingham@gmail.com",
    url='https://github.com/buckinha/DiamondSquare',
    name='hkb_diamondsquare',
    version=get_version(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=get_requirements(),
    license='The MIT License (MIT)',
    long_description="Python library for running the Diamond Square terrain generation algorithm"

)

