# Koromali/app_core/syntax_highlighters.py
"""
This module serves as a central import point for all built-in syntax
highlighters. This prevents code duplication and makes it easier to manage
and extend language support.
"""
from .highlighters.python_syntax_highlighter import PythonSyntaxHighlighter
from .highlighters.json_syntax_highlighter import JsonSyntaxHighlighter
from .highlighters.html_syntax_highlighter import HtmlSyntaxHighlighter
from .highlighters.css_syntax_highlighter import CssSyntaxHighlighter
from .highlighters.cpp_syntax_highlighter import CppSyntaxHighlighter
from .highlighters.csharp_syntax_highlighter import CSharpSyntaxHighlighter
from .highlighters.javascript_syntax_highlighter import JavaScriptSyntaxHighlighter
from .highlighters.rust_syntax_highlighter import RustSyntaxHighlighter

__all__ = [
    "PythonSyntaxHighlighter",
    "JsonSyntaxHighlighter",
    "HtmlSyntaxHighlighter",
    "CssSyntaxHighlighter",
    "CppSyntaxHighlighter",
    "CSharpSyntaxHighlighter",
    "JavaScriptSyntaxHighlighter",
    "RustSyntaxHighlighter"
]