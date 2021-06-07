from setuptools import find_packages, setup

setup(
    name='gig-python',
    packages=find_packages(),
    version='0.1.0',
    description='Interface to GIG server',
    author='LDF',
    license='MIT',
    install_requires=[
        'attrs == 21.2.0',
        'certifi==2021.5.30',
        'chardet==4.0.0',
        'idna==2.10',
        'iniconfig==1.1.1',
        'packaging==20.9',
        'pluggy==0.13.1',
        'py==1.10.0',
        'pyparsing==2.4.7',
        'requests==2.25.1',
        'toml==0.10.2',
        'urllib3==1.26.5'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.4'],
    test_suite='tests',
)
