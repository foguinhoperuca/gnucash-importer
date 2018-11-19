import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "gnucash-importer",
    version = "0.1.0",
    author = "Jefferson Campos",
    author_email = "jefferson@jeffersoncampos.eti.br",
    description = "Parse data source (ofx, qif, csv, etc.) and import to Gnucash file.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/foguinhoperuca/gnucash-importer",
    packages = setuptools.find_packages(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    # data_files=[('my_data', ['data/data_file'])],  # Optional
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'parser=parser:main',
    #     ],
    # },
)
