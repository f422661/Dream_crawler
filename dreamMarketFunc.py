import re
import requests
from bs4 import BeautifulSoup


def crawlInnerPage(doc):

  soup = BeautifulSoup(doc, "html.parser")
  node = soup.find("div",class_ ="title")
  node_div = soup.find("div",class_="tabularDetails").find_all("div")
  post_title = node.text

  ## initial
  vendor = 0
  ratings = 0
  ratings_n = 0
  ships_to = 0
  ships_from = 0
  escrow = 0

  for item in node_div:

    if item.find("span").text == "Vendor":
      vendor = item.find("span").find("a").text.strip()
      item.find("span").find("a").find_next_siblings("a")[0].find_all("span")[1].text
      ratings = item.find("span").find("a").find_next_siblings("a")[0].find_all("span")[1].text.replace("\xa0","")
      ratings_n = item.find("span").find("a").find_next_siblings("a")[0].find_all("span")[0].text
      ratings_n = ratings_n.replace("(","").replace(")","")

    # elif item.find("span").text == "Price":
    #   print(item)


    elif item.find("span").text == "Ships to":
      ships_to = item.find("span").text.strip()
    elif item.find("span").text == "Ships from":
      ships_from = item.find("span").text.strip()
    elif item.find("span").text == "Escrow":
      escrow = item.find("span").text.strip()
          
  description = soup.find("div",class_ ="preformattedNotes").find("pre").text

  return [post_title,vendor,ratings,ratings_n,ships_to,ships_from,escrow,description]



