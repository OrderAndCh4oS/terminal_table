# Always prefer setuptools over distutils

from setuptools import setup, find_packages

VERSION = "1.0.5"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='terminal_table',
    version=VERSION,
    description='Print headers and rows of data in terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sarcoma/terminal_table',
    author='sarcoma',
    author_email='sean@orderandchaoscreative.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='table print development display terminal command-line-tools',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>=3.5, <4',
    install_requires=['ansi_colours'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Order & Chaos Creative': 'https://orderandchaoscreative.com',
        'Bug Reports': 'https://github.com/sarcoma/terminal_table/issues',
        'Source': 'https://github.com/sarcoma/terminal_table',
    },
)
