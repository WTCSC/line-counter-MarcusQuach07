from setuptools import setup, find_packages

setup(
    name='line_count',
    version='0.1',
    py_modules=['line_count'],
    entry_points={
        'console_scripts': [
            'line_count=line_count:main',
        ],
    },
)