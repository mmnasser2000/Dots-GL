'''
This page uses data from the OpenPowerlifting project, https://www.openpowerlifting.org.
You may download a copy of the data at https://data.openpowerlifting.org.
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('openpowerlifting-2022-03-14/openpowerlifting-2022-03-14-f3d5c9e1.csv')
df = df[df['Equipment'].str.contains('Raw')]
df = df[df['Federation'].str.contains('USAPL')]
df = df[df['Event'].str.contains('SBD')]
df = df[['Name', 'Sex', 'BodyweightKg', 'TotalKg', 'Dots', 'Goodlift', 'State']]

liftersCarolinas = df[df['State'].str.contains('NC', na=False)].append(df[df['State'].str.contains('SC', na=False)])
liftersTX = df[df['State'].str.contains('TX', na=False)]


liftersCarolinasDots = set(liftersCarolinas.loc[liftersCarolinas['Dots'] > 500]['Name'])
liftersCarolinasGL = set(liftersCarolinas.loc[liftersCarolinas['Goodlift'] > 100]['Name'])
allCarolinaLifters = set(liftersCarolinas['Name'])

liftersTXDots = set(liftersTX.loc[liftersTX['Dots'] > 500]['Name'])
liftersTXGL = set(liftersTX.loc[liftersTX['Goodlift'] > 100]['Name'])
allTexasLifters = set(liftersTX['Name'])


carolinaDotsRatio = len(liftersCarolinasDots) / len(allCarolinaLifters)
carolinaGLRatio = len(liftersCarolinasGL) / len(allCarolinaLifters)

texasDotsRatio = len(liftersTXDots) / len(allTexasLifters)
texasGLRatio = len(liftersTXGL) / len(allTexasLifters)


rows = ["% of carolina lifters w/ > 500 dots", "% of texas lifters w/ > 500 dots", "% of carolina lifters w/ > 100 GL", "% of texas lifters w/ > 100 GL"]
values = [carolinaDotsRatio*100, texasDotsRatio*100, carolinaDotsRatio*100, texasDotsRatio*100]

f = plt.figure(1)
plt.bar(['Carolinas', 'Texas'], values[:2])
plt.title("% of Lifters W/ > 500 Dots")


s = plt.figure(2)
plt.bar(['Carolinas', 'Texas'], values[2:])
plt.title("% of Lifters W/ > 100 GL")
plt.show()
