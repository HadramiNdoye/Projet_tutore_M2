# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:01:29 2021

@author: EL Hadrami N'DOYE
"""

import pandas as pd
FILE_EXCEL = pd.ExcelFile("measures_enfants/measures_pmi.xlsx")
WORKSHEET = FILE_EXCEL.sheet_names
dataset_1 = pd.read_excel(FILE_EXCEL,WORKSHEET[0])
dataset_1.head(4)
dataset_1.shape