import sublime, sublime_plugin
import subprocess
import tempfile
import os
import abc

class PhpSimpleRefactorBaseCommand(sublime_plugin.TextCommand):
	__metaclass__ = abc.ABCMeta

	def run(self, edit):
		(rowBegin,col) = self.view.rowcol(self.view.sel()[0].begin())
		(rowEnd,col) = self.view.rowcol(self.view.sel()[0].end())

		self.rowBegin = rowBegin + 1
		self.rowEnd = rowEnd + 1
		view = sublime.Window.active_view(sublime.active_window())
		if(view.file_name() is None):
			sublime.status_message('File not saved yet, please save first')
		else:
			self.file_name = view.file_name();
			self.process()

	@abc.abstractmethod
	def process(self):
		return

	def get_command(self):
		return

	def on_filled_info(self):
		view = sublime.Window.active_view(sublime.active_window())
		# save if dirty
		if view.is_dirty():
			view.run_command('save')
			sublime.status_message('File saved')

		p = self.get_command()
		output, error = p.communicate()
		if error:
			sublime.error_message(error.decode('utf-8'))
		else:
			fp = tempfile.NamedTemporaryFile(delete=False)
			fp.write(output)
			fp.close()
			cmd = ''.join(['patch -p1 "',self.file_name,'" "',fp.name,'"'])
			pr = subprocess.Popen(cmd, shell=True, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			output, error = pr.communicate()
			os.remove(fp.name)
			if error:
				sublime.error_message(error.decode('utf-8'))
			else:
				sublime.status_message('Refactor completed')
