# Working with a public workbook in Google Sheets
# See the private sheets repo for more examples
# Go to the workbook in Google sheets
# Share, Get link, Anyone with the link
# Paste the link in the url string below and
# remove the "edit?isp=sharing" at the end of the link

import pandas

url="https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/"
url=url+"gviz/tq?tqx=out:csv&sheet="
urlSheet1=url + "2013"
urlSheet2=url + "2014"
data1=pandas.read_csv(urlSheet2)
print(data1)