#from PyQt4 import uic

from PyQt5 import uic

with open('istasyonui.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('istasyon.ui', fout)