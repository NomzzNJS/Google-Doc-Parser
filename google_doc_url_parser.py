import requests

url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"

response = requests.get(url)

#this below code is giving me a whole html code instead of just table text, therefore need to do something else
if response.status_code == 200:
    document_text = response.text
    print(document_text)
else:
    print(f"Failed to retrieve the document, satus code:{response.status_code}")

