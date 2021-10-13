
from setuptools import setup, find_packages


setup(
    name='mixpeek',
    version='1.1',
    license='MIT',
    author="Ethan Steininger",
    author_email='info@mixpeek.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mixpeek/mixpeek-python',
    keywords='file search',
    install_requires=['requests','boto3']
)
