import click
import six
from output import Out

@click.command()
@click.option('-o', '--output', type=click.Choice(['plain', 'yaml', 'json']), default='plain', help='Output formatting')
@click.option('-v', '--verbose', count=True)
def main(output, verbose):
    """
    CLI for finding suitable C/C++ compiler on current platform
    """
    out = Out(output, verbose)
    out.write("findc %s" % "0.0.1-dev", bold=True)    
    

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    main()
