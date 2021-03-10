import sys
sys.path.append('C:\Lijun\workspace\firstpython\venv\Lib\site-packages\pytesseract')
print(sys.path)

sys.path.append('C:\Lijun\workspace\firstpython\venv\Lib\site-packages\openpyxl')
print(sys.path)

sys.path.append('C:\Program Files\Tesseract-OCR')
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import pandas as pd
import numpy as np
import openpyxl

#Path
#/usr/local/lib/python3.9/site-packages/openpyxl/__init__.py



#path = 'C:\\Sean\\'
df = pytesseract.image_to_data(Image.open('C:\Sean\Page_1.png'),lang='eng', output_type='data.frame')
df_pandas = pd.DataFrame(data=df)
print(df_pandas)
df.to_excel("output.xlsx")

#troubleshootings:
#1. https://github.com/tesseract-ocr/tesseract/wiki Download tesseract and install it.
#2. add environment variable tesseract= 'C:/Program Files/Tesseract-OCR/tesseract.exe'
#3.open pytesseract.py from Lib\site-packages\pytesseract.
# Change the following code from tesseract_cmd = 'tesseract' to: tesseract_cmd = 'D:/Program Files/Tesseract-OCR/tesseract.exe'