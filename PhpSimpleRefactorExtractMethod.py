import sublime, sublime_plugin
import subprocess
import tempfile
import os
import sys

from PhpSimpleRefactor.PhpSimpleRefactorCommand import PhpSimpleRefactorBaseCommand

class PhpSimpleRefactorExtractMethodCommand(PhpSimpleRefactorBaseCommand):
	function_name = ''

	def process(self):
		sublime.active_window().show_input_panel('Function name', '', self.obtain_function_name, None, None)

	def obtain_function_name(self, functionName):
		self.function_name = functionName;
		self.on_filled_info()

	def get_command(self):
		settings = sublime.load_settings('PHPSimpleRefactor.sublime-settings')
		self.php_path = settings.get('php_path')
		self.refactor_path = settings.get('refactor_path')
		rows = ''.join([str(self.rowBegin), "-", str(self.rowEnd)])
		cmd = ''.join([self.php_path, ' "', self.refactor_path,'" ',  'extract-method', ' "', self.file_name, '" ', rows, ' ', self.function_name])
		print(cmd)
		return subprocess.Popen(cmd, shell=True, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
