import click
import six
from output import Out
from toolchain.detect import detect_toolchains

@click.command()
@click.option('-o', '--output', type=click.Choice(['plain', 'yaml', 'json']), default='plain', help='Output formatting')
@click.option('-v', '--verbose', count=True)
def main(output, verbose):
    """
    CLI for finding suitable C/C++ compiler on current platform
    """
    out = Out(output, verbose)
    out.write("findc %s" % "0.0.1-dev", bold=True)    
    
    from toolchain.loader import get_plugins
    from find import find_match_in_path
    from toolchain.detect import detect_toolchains
    
    files = detect_toolchains(out)
    plugins = get_plugins(out, folder="./findc/toolchain/matcher", desc="compiler-matcher")

    for file in files:
      for plugin in plugins:
        plugins[plugin].run(file, out)

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    main()
