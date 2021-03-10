#Command Line:
#  $ pip3 install camelot-py[cv] tabula-py
#camelot-py[cv] was install by pip3 install camelot-py[cv] from cms
# tabula-py was installed from Pycharm interpreter
# Camelot pip package: https://pypi.org/project/camelot-py/
# Git Source Code: https://github.com/camelot-dev/camelot/issues/193
# Download Ghostscript from here https://www.ghostscript.com/download/gsdnld.html and install it per instructions

from camelot import *

# PDF file to extract tables from
#test.pdf is a text-based pdf file
file = "C:\\Sean\\test.pdf"

# extract all the tables in the PDF file
cols = ['62,105,185,252']
cols *= 128 # <-- workaround: just make sure to have enough of the same col set for all tables that will be discovered. e.g. ['62,105,185,252', '62,105,185,252', .....]
tables = read_pdf(file,flavor='stream', columns=cols)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# Export Option 1: export individually as CSV
tables[0].to_csv("Page_1_camelot.csv")

# Export Option 2: export individually as Excel (.xlsx extension)
tables[0].to_excel("Page_1_camelot.xlsx")
