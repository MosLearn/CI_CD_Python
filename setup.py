import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mon_package",
    version="0.0.1",
    author="Mos",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir_in={"": "src"},
    package_dir_out={"": "tu"},
    packages_in=setuptools.find_packages(where="src"),
    packages_out=setuptools.find_packages(where="tu"),
    python_requires=">=3.7",
)

# https://othrif.github.io/python/basics/packaging.html
