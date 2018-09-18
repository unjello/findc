import click

_verbosity_levels = {
  'info': 0,
  'debug': 1,
  'trace': 2
}



class Out:
  def __init__(self, outputFormat, verbosity):
    self.outputFormat = outputFormat
    self.verbosity = verbosity

  def _is(self, level):
    return self.verbosity >= _verbosity_levels[level]
  
  def _plain(self):
    return self.outputFormat == 'plain'

  def _can(self, level):
    return self._plain() and self._is(level)

  def write(self, data, fg=None, bg=None, bold=None, dim=None, underline=None):
    if self._plain():
      click.secho(data, fg=fg, bg=bg, bold=bold, dim=dim, underline=underline)

  def info(self, data, fg=None, bg=None, bold=None, dim=None, underline=None):
    if self._can('info'):
      click.secho("info ", fg="bright_green", nl=False)
      click.secho(data, fg=fg, bg=bg, bold=bold, dim=dim, underline=underline)

  def debug(self, data, fg=None, bg=None, bold=None, dim=None, underline=None):
    if self._can('debug'):
      click.secho("debg ", fg="green", nl=False)
      click.secho(data, fg=fg, bg=bg, bold=bold, underline=underline)

  def trace(self, data, fg=None, bg=None, bold=None, dim=None, underline=None):
    if self._can('trace'):
      click.secho("trac ", fg="green", dim=True, nl=False)
      click.secho(data, fg=fg, bg=bg, bold=bold, dim=dim, underline=underline)