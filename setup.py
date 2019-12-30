from setuptools import setup, find_packages

setup(
    name='data_file_validator',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'pymongo'
    ],
)
