from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QTextCharFormat, QSyntaxHighlighter, QColor, QRegExp
from PySide2.QtCore import QRegExp

class PythonSyntaxHighlighterPlugin(PluginInterface):
    def run(self, editor):
        editor.highlighter = PythonHighlighter(editor.text_edit.document())
        QMessageBox.information(editor, "Plugin Loaded", "Python Syntax Highlighter plugin loaded successfully.")
