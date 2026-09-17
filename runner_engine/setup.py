from setuptools import setup, find_packages

setup(
    name='runner_engine',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'docker>=6.1.3',
    ],
    description='Sandboxed Python execution engine for PIP',
)
