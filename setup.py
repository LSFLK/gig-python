import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gig-python",
    version="0.0.1",
    author="ldf",
    author_email="umayangag@gmail.com",
    description="Interface For GIG Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LSFLK/gig-python",
    project_urls={
        "Bug Tracker": "https://github.com/LSFLK/gig-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'attrs==21.2.0',
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
    setup_requires=['pytest-runner==5.3.1'],
    tests_require=['pytest==6.2.4'],
    test_suite='tests',
)
