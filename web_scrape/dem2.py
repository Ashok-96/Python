import requests as request
from bs4 import BeautifulSoup

url="https://www.google.com/search?q=web+scraping+google+search+result+website&rlz=1C1CHBF_enIN1031IN1031&sxsrf=AJOqlzVWBRoDDZsJSAPIMjT1q7m2VHHqMw%3A1678695824911&ei=kN0OZPWlN6G43LUPwPOO4AU&oq=web+scraping+google+search+re+website&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgoIIRCgARDDBBAKMgoIIRCgARDDBBAKOgoIABBHENYEELADOgcIABANEIAEOgYIABAeEA06CAgAEAUQHhANOggIABAIEB4QDToFCAAQhgM6CAghEKABEMMEOgQIIRAKSgQIQRgAULMHWJtaYI9yaAVwAXgAgAHAAYgBjBaSAQQwLjE5mAEAoAEByAEIwAEB&sclient=gws-wiz-serp"
response=request.get(url)
frag=BeautifulSoup(response.text,'html.parser')
print(frag.find_all('div'))