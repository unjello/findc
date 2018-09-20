_print_format='{:25}{:15}{:10}'

def print_toolchains(meta, output):
  print(_print_format.format('PATH', 'TOOLCHAIN', 'VERSION'))
  for m in meta:
    print(_print_format.format(m[0]['path'], m[0]['tool'], m[0]['version']))
