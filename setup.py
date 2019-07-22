from setuptools import setup
from setuptools import find_packages

setup(
    name='flask final test project',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)