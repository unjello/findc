import re
from subprocess import check_output

_command_candidate_patterns = ['/usr/bin/gcc','/usr/bin/g++', '/usr/bin/clang', '/usr/bin/clang++']
_find_apple_llvm_version='^Apple LLVM version ([0-9\.]+)'

def _detect_apple_llvm(command, out=None):
  if not command:
    return None

  if command not in _command_candidate_patterns:
    if out:
      out.trace("%s is not valid command candidate" % command)
    return None

  output = check_output([command, "--version"])
  match = re.search(_find_apple_llvm_version, output)
  if not match:
    if out:
      out.trace("%s is not Apple LLVM compiler" % command)
    return None

  out.info("Found Apple LLVM compiler version %s in %s" % (match.group(1), command))
  meta = {
    "tool": "applellvm",
    "path": command,
    "version": match.group(1),
    "raw_version_output": output
  }
  return meta

def run(command, out=None):
  result = []
  for f in [_detect_apple_llvm]:
    ret = f(command, out)
    if ret:
      result.append(ret)
  return result