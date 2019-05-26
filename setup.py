from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='pyIpeaData',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/danielsioli/IpeaData',
    author='Gustavo Coelho, Daniel Oliveira',
    author_email='danielsioli@gmail.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Pacote para obter dados do Ipea Data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='ipea',
    install_requires=['requests', 'pandas'],
    include_package_data=True,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
