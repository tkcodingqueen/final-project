# import requests
# import bs4 
# import pandas as pd
# import matplotlib.pyplot as plt

# session = requests.Session()
# response = session.get('https://www.currentresults.com/Weather/California/Places/palo-alto-temperatures-by-month-average.php', headers={'User-Agent': 'Mozilla/5.0'})

# print(response.status_code)

# tables = pd.read_html(response.text)
# print(tables)

# table = tables[0]
# df = table [["High °F", "Unnamed: 2"]]
# print(df.info())
# df.plot(x = "Unnamed: 2", y = "High °F" )

# plt.show()

import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

session = requests.Session()
response = session.get('https://www.currentresults.com/Weather/California/Places/palo-alto-temperatures-by-month-average.php', headers={'User-Agent': 'Mozilla/5.0'})

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
df = pd.read_html(str(table))[0][['High °F', 'Unnamed: 2']]
print(df.info())

df.plot(x='Unnamed: 2', y='High °F')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.xlabel('Month')
plt.ylabel('High Temperature (°F)')
plt.title('Average High Temperatures in Palo Alto, CA')
plt.show()