''' programming languages supported '''

from .clike import CLikeReader
from .java import JavaReader
from .javascript import JavaScriptReader
from .python import PythonReader
from .objc import ObjCReader
from .ttcn import TTCNReader
from .swift import SwiftReader
from .ruby import RubyReader
from .csharp import CSharpReader
from .php import PHPReader
from .scala import ScalaReader
from .gdscript import GDScriptReader
from .go import GoReader
from .lua import LuaReader
from .rust import RustReader
from .typescript import TypeScriptReader


def languages():
    return [
        CLikeReader
        JavaReader,
        CSharpReader,
        JavaScriptReader,
        PythonReader,
        ObjCReader,
        TTCNReader,
        RubyReader,
        PHPReader,
        SwiftReader,
        ScalaReader,
        GDScriptReader,
        GoReader,
        LuaReader,
        RustReader,
        TypeScriptReader
    ]


def get_reader_for(filename):
    for lan in languages():
        if lan.match_filename(filename):
            return lan
