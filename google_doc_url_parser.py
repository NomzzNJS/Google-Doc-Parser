import requests
from bs4 import BeautifulSoup



url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"

response = requests.get(url)
data = response.text
#this below code is giving me a whole html code instead of just table text, therefore need to do something else
# if response.status_code == 200:
#     document_text = response.text
#     print(document_text)
# else:
#     print(f"Failed to retrieve the document, satus code:{response.status_code}")


parse = BeautifulSoup(data, "html.parser")

#print(parse.prettify())

table = parse.find("table")
#print(tables)

headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

row = []
for tr in table.find_all('tr'):
    cells = tr.find_all('td')
    if not cells:
        continue
    for cell in cells:
        row.append(cell.text.strip())

print('headers:', headers)
print('row:', row)