#! python3
# mcb.py - saves and loads pieces of text to the clipboard.
# Usage: python mcb.py save <keyword> - save clipboard indexing by keyword
#        python mcb.py <keyword> - loads keyword indexed text to clipboard
#        python mcb.py list - list all keywords to clipboard

import shelve, pyperclip, sys

print(argv)

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    #save clipboard content
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        #list keywords and load content
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbShelf[sys.argv[1])

mcbShelf.close()

