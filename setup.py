from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

requirements = []

test_requirements = ["pytest==7.2.0"]

dev_requirements = ["black==22.10.0"] + test_requirements

extra_requirements = {
    "dev": dev_requirements,
}

setup(
    name="logger",
    version="1.0.5",
    description="Simple Logger inspired by the Logger base module of python",
    long_description=long_description,
    author="Malo Boucé",
    author_email="ma.sithis@gmail.com",
    url="https://github.com/Sithi5/logger",
    packages=["logger"],
    install_requires=requirements,
    extras_require=extra_requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
