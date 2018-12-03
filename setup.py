# from cx_Freeze import setup, Executable

# # Dependencies are automatically detected, but it might need
# # fine tuning.
# buildOptions = dict(packages = [], excludes = [])

# base = 'Console'

# executables = [
#     Executable('setup_cxfreeze.py', base=base, targetName = 'gnucash_importer/run_app.py')
# ]

# setup(name='gnucash_importer',
#       version = '1.0',
#       description = '',
#       options = dict(build_exe = buildOptions),
#       executables = executables)


import setuptools
import sys
from cx_Freeze import setup, Executable

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('gnucash_importer/version.py') as f:
    exec(f.read())

buildOptions = dict(packages = [], excludes = [])
base = 'Console'
    
setuptools.setup(
    name = "gnucash_importer",
    version = __version__,
    # version_command='git describe',
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
    # package_data = {'test/fixtures': ['test/fixtures/*']},
    # data_files=[('my_data', ['data/data_file'])],  # Optional
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'parser=parser:main',
    #     ],
    # },
    # options = {"build_exe": buildOptions},
    executables = [Executable("gnucash_importer/run_app.py", base = base)]
)
