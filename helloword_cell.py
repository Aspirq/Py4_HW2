# coding: utf-8
get_ipython().run_line_magic('save', '-f helloword_cell.py 1-5')
from helloword import HelloWord

a = HelloWord()
print(a.hw_string)
