from setuptools import setup
from codecs import open

from ia_plugin import __version__


setup(
    name='ia_plugin',
    version=__version__,
    author='Jacob M. Johnson',
    author_email='jake@archive.org',
    url='https://github.com/jjjake/internetarchive-plugin',
    license='AGPL 3',
    description='An example ia-wrapper plugin.',
    py_modules=['ia_plugin'],
    install_requires=[
        'internetarchive',
        'docopt',
    ],
    entry_points = {
        'internetarchive.cli.plugins': [
            'ia_plugin = ia_plugin',
        ],
        'console_scripts': [
            'ia-plugin = ia_plugin:main',
        ],
    },
)
