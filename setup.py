from setuptools import setup, find_packages

setup(
    name="solar-browser",
    version="0.0.1",
    packages=find_packages(where="src"),
    install_requires=[
        'PyQt5',
        'PyQtWebEngine'
    ],
    package_dir={'': 'src'}
) 