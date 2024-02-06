from setuptools import setup, find_packages

setup(
    name='assignment0',
    version='1.0',
    author='Rutika Pandhurang Shinde',
    author_email='shinder@ufl.edu',
    description='CIS 6930 Spring 2024 Assignment 0',
    url='https://github.com/sightunseen/cis6930sp24-assignment0',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',  
        'requests', 
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'assignment0 = assignment0.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
