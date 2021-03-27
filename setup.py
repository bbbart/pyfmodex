from setuptools import setup

clfs = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Microsoft :: Windows :: Windows XP",
    "Operating System :: Microsoft :: Windows :: Windows Vista",
    "Operating System :: Microsoft :: Windows :: Windows 7",
    "Operating System :: Microsoft :: Windows :: Windows 8",
    "Operating System :: Microsoft :: Windows :: Windows 8.1",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3",
]

setup(name="pyfmodex", version="0.7.0", author="Lukas Tyrychtr", author_email="lukastyrychtr@gmail.com", url="https://www.github.com/tyrylu/pyfmodex", packages=["pyfmodex", "pyfmodex.studio"], long_description=open("readme.md", "r").read(), long_description_content_type="text/markdown", description="Python bindings to the Fmod Ex library.", license="MIT", classifiers=clfs, install_requires=["py-flags"])