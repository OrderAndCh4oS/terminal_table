
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='terminal_table',
    version='0.3.0',
    description='Print headers and rows of data in terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sarcoma/terminal_table',
    author='sarcoma',
    author_email='sean@orderandchaoscreative.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
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
