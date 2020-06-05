from distutils.core import setup


def get_version() -> str:
    with open('VERSION', 'r') as f:
        version = f.readline().strip()
    return version

setup(
    author="Hailey K Buckingham",
    author_email="hailey.k.buckingham@gmail.com",
    url='https://github.com/buckinha/DiamondSquare',
    name='hkb_diamondsquare',
    version=get_version(),
    packages=['src/hkb_diamondsquare',],
    license='The MIT License (MIT)',
    long_description=open('README.md').read(),
)

