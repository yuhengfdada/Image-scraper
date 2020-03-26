# import HTMLSession from requests_html
from requests_html import HTMLSession
headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
# create an HTML Session object
session = HTMLSession()
 
# Use the object above to connect to needed webpage
resp = session.get('http://github.com',headers=headers)
print(resp.html.links)
# Run JavaScript code on webpage

resp.html.render()
print(resp.html.html)
session.close()
