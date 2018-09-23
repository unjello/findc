import re
from subprocess import check_output, STDOUT

_command_candidate_patterns = ['/usr/bin/gcc','/usr/bin/g++', '/usr/bin/clang', '/usr/bin/clang++']
_find_apple_llvm_version='Apple LLVM version ([0-9\.]+)'
_find_apple_llvm_options='\s+--?([A-Za-z0-9#\-\+]+)((([\s,]*)|=)<([^>]+)>)?\s*([^\n]+)'


def _detect_apple_llvm_options(command):
  output = check_output([command, "--help"], stderr=STDOUT)
  match = re.findall(_find_apple_llvm_options, output)
  options = []
  for m in match:
    options.append({
      "name": m[0],
      "paremeter": m[4],
      "description": m[5]
    })
  return options

def _detect_apple_llvm_version(command, out=None):
  output = check_output([command, "--version"], stderr=STDOUT)
  match = re.search(_find_apple_llvm_version, output)
  if not match:
    if out:
      out.trace("%s is not Apple LLVM compiler" % command)
    return None
  return match.group(1)

def _detect_apple_llvm(command, out=None):
  if not command:
    return None

  if command not in _command_candidate_patterns:
    if out:
      out.trace("%s is not valid command candidate" % command)
    return None

  
  version = _detect_apple_llvm_version(command, out)
  if not version:
    return None

  options = _detect_apple_llvm_options(command)

  out.info("%s: found Apple LLVM compiler version %s" % (command, version))
  meta = {
    "tool": "applellvm",
    "path": command,
    "version": version,
    "options": options
  }
  return meta

def run(command, out=None):
  result = []
  for f in [_detect_apple_llvm]:
    ret = f(command, out)
    if ret:
      result.append(ret)
  return result