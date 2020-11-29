from setuptools import setup

__version__ = '0.0.1'
__url__ = 'https://github.com/layerqa/fastcupy'
__description__ = 'Unofficial fascup api wrapper for python3'
__author__ = 'layerqa'
__author_email__ = 'https://t.me/layerqa'
__license__ = 'GNU GENERAL PUBLIC LICENSE'

def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

def get_description():
    with open('README.md') as f:
        return f.read()

setup(
    name='fastcupy',
    version=__version__,
    url=__url__,
    description=__description__,
    long_description=get_description(),
    long_description_content_type='text/markdown',
    author=__author__,
    author_email=__author_email__,
    install_requires=get_requirements(),
    license=__license__,
    packages=['fastcupy'],
    python_requires=">=3.8"
)