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

df = df[:-1]

df.plot(x='Unnamed: 2', y='High °F', marker ='.')
plt.xticks(range(0, 12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.xlabel('Month')
plt.ylabel('High Temperature (°F)')
plt.title('Average High Temperatures in Palo Alto, CA')


plt.show()

