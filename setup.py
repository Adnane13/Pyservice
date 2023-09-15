import setuptools

setuptools.setup(
    name="pyservice",
    version="0.0.01",
    author="Adnane",
    author_email="adnaneabdellaoui@gmail.com",
    license='The Unlicense',
    description="A simple python script for a linux server ( almalinux )",
    url="https://github.com/Adnane13/Pyservice.git",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': ['pyserv=mainp:start'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved ? :: The Unlicense"
    ],
)
