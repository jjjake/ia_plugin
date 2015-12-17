#!/usr/bin/env python
"""An example 'ia' plugin.

Usage: ia plugin [--help] [--field FIELD] <identifier>

Options:
  -h, --help                Show this help message and exit.
  -f, --field FIELD         Return specific metadata field [default: metadata].

Examples:
    $ ia plugin --field metadata.title nasa
    NASA Images
"""
from docopt import docopt

__title__ = 'ia_plugin'
__version__ = '0.0.1'
__url__ = 'https://github.com/jjjake/ia_plugin'
__author__ = 'Jacob M. Johnson'
__license__ = 'AGPL 3'
__copyright__ = 'Copyright 2015 Internet Archive'
__all__ = ['ia_plugin']


def main(argv=None, session=None):
    args = docopt(__doc__, argv=argv)

    item = session.get_item(args['<identifier>'])
    fields = args['--field'].split('.')
    md = item.item_metadata
    for f in fields:
        md = md.get(f)
    print(md)

if __name__ == '__main__':
    main()
