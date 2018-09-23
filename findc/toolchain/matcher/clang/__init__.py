import re
from subprocess import check_output, STDOUT

_command_candidate_patterns = ['clang(\.exe)?$','clang-[A-Za-z0-9]+(\.exe)?$', 'clang++(\.exe)?$', 'clang++-[A-Za-z0-9]+(\.exe)?$']
_not_apple_llvm='Apple LLVM version ([0-9\.]+)'

def run(command, out=None):
  return None