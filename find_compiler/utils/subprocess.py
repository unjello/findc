from subprocess import check_output, STDOUT

def get_output(command_line):
  return check_output(command_line, stderr=STDOUT).decode('ascii')