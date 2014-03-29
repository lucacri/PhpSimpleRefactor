PHPSimpleRefactor for Sublime Text
===========

A simple way to integrate [PHP Refactoring Browser]'s method extraction in Sublime Text 3 

---

Requirements
===========
You need to have PHP installed and [PHP Refactoring Browser]'s refactor.phar file. 

Installation
=======
The package is available on [Package Control](https://sublime.wbond.net/).

Configuration
=======
Edit the file PHPSimpleRefactor.sublime-settings (Preferences > Package Settings > PHPSimpleRefactor > Settings – User) with the correct php_path and refactor_path.

Usage
=====
In a PHP file, select the lines that you'd like to extract to a new method, and use the shortcut ctrl+alt+r (or right click on the text and select "PHPSimpleRefactor: extract method"). The plugin will ask you for the method name to use, save the current view and apply the patch.


License
----

MIT

[PHP Refactoring Browser]:https://github.com/QafooLabs/php-refactoring-browser
