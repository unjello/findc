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
    out.write("findc %s" % "0.0.2", bold=True)    
    
    from toolchain.loader import get_plugins
    from find import find_match_in_path
    from toolchain.detect import detect_toolchains
    from toolchain.printer import print_toolchains
    
    files = detect_toolchains(out)
    plugins = get_plugins(out, folder="./find_compiler/toolchain/matcher", desc="compiler-matcher")

    meta = []
    for file in files:
      for plugin in plugins:
        m = plugins[plugin].run(file, out)
        if m:
          meta.extend(m)
    print_toolchains(meta, output)

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    main()
