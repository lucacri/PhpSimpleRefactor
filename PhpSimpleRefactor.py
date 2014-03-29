import sublime, sublime_plugin
import subprocess

class PhpSimpleRefactorCommand(sublime_plugin.TextCommand):
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
			sublime.active_window().show_input_panel('Function name', '', self.on_filled_info, None, None)	
		

	def on_filled_info(self, functionName):
		view = sublime.Window.active_view(sublime.active_window())
		# save if dirty
		if view.is_dirty():
			view.run_command('save')
			sublime.status_message('File saved')

		settings = sublime.load_settings('PHPSimpleRefactor.sublime-settings')
		self.php_path = settings.get('php_path')
		self.refactor_path = settings.get('refactor_path')
		rows = ''.join([str(self.rowBegin), "-", str(self.rowEnd)])
		cmd = ''.join([self.php_path, ' ', self.refactor_path,' ',  'extract-method', ' ', self.file_name, ' ', rows, ' ', functionName, ' | patch -p1'])
		p = subprocess.Popen(cmd, shell=True, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output, error = p.communicate()
		if error:
			sublime.error_message(error.decode('utf-8'))
		else:
			sublime.status_message('Refactor completed')
