from setuptools import setup, find_packages

setup(
    name='dictator',
    version='0.1.1',
    packages=find_packages(),
    url='https://github.com/amka/dictator',
    license='MIT',
    author='andrey.maksimov',
    author_email='meamka@ya.ru',
    description='Dictator is a tiny library for Robots to work with Redis as a Dict.',
    install_requires=['redis'],
)
