# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:27:55 2016

@author: AbreuLastra_Work

This is the challenge for Thinkful - Data Science lesson
about visualizing Lending Clug Data.
It generates and saves a boxplot, histogram and QQ-plot
for the values in the 'Amount.Requested' and compares 
them with the variable 'Amount.Funded.By.Investors'
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# Droping missing observations
loansData.dropna(inplace=True)

#Make a bloxplot
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

loansData.boxplot(column='Amount.Requested')
plt.savefig("AR_boxplot.png")
plt.show()

#Make a histogram
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

loansData.hist(column='Amount.Requested')
plt.savefig("AR_Histogram.png")
plt.show()

# QQ-plot, to test normality
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("AR_QQplot.png")
plt.show()
