
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cloudnetpy',
    version='0.1.1',
    description='Python package for Cloudnet processing',
    long_description=readme,
    author='Simo Tukiainen',
    author_email='simo.tukiainen@fmi.fi',
    url='https://github.com/tukiains/cloudnetpy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'bin')),
    python_requires='>=3.6',
    install_requires=['scipy>=1.1', 'netCDF4>=1.4.1'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
    ],
)
