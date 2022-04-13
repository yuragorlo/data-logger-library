from setuptools import setup, find_packages

setup(
    author='New Age Sol.',
    author_email='dev@newagesol.com',
    name='logger',
    version='1.0',
    description='HRZN iGaming platform data team logger.',
    url='https://github.com/yuragorlo/data-logger-library.git',

    classifiers=[],

    install_requires=['uvicorn==0.11.8'],

    packages=find_packages(),
    package_dir={'logger': 'logger'}
)