import sublime, sublime_plugin
import subprocess
import tempfile
import os

from PhpSimpleRefactor.PhpSimpleRefactorCommand import PhpSimpleRefactorBaseCommand

class PhpSimpleRefactorRenameLocalVariableCommand(PhpSimpleRefactorBaseCommand):
	old_name = '';
	new_name = '';

	def process(self):
		sublime.active_window().show_input_panel('Variable name', '', self.obtain_old_name, None, None)

	def obtain_old_name(self, name):
		self.old_name = name;
		sublime.active_window().show_input_panel('New name', '', self.obtain_new_name, None, None)

	def obtain_new_name(self, name):
		self.new_name = name;
		self.on_filled_info()

	def get_command(self):
		settings = sublime.load_settings('PHPSimpleRefactor.sublime-settings')
		self.php_path = settings.get('php_path')
		self.refactor_path = settings.get('refactor_path')
		rows = str(self.rowBegin)
		cmd = ''.join([self.php_path, ' "', self.refactor_path,'" ',  'rename-local-variable', ' "', self.file_name, '" ', rows, ' ', self.old_name, ' ', self.new_name])
		return subprocess.Popen(cmd, shell=True, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)