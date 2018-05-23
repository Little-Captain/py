countrycap = {'U.S.': 'Washington D.C.',\
              'U.K.': 'London',\
              'India': 'New Delhi'}
n = input('Enter country: ')
if n in countrycap:
    print('The capital of', n, 'is', countrycap[n])
else:
    print('Sorry the country', n, 'does not exist in our dictionary')
countrycap['Australia'] = 'Sweden'
print('The dictionary after adding a country:')
for country, capital in countrycap.items():
    print('Capital of', country, 'is', capital)
m = input('Enter the country to delete:')
del countrycap[m]
print('The dictionary after deleting a country:')
for country, capital in countrycap.items():
    print('Capital of', country, 'is', capital)
