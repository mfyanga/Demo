#!/usr/bin/python
#-*- coding: UTF-8 -*-
import xml.sax

class MovieHandler(xml.sax.ContentHandler):
  def __init__(self):
    self.current_data = ""
    self.type = ""
    self.format = ""
    self.year = ""
    self.rating = ""
    self.stars = ""
    self.description = ""

  def     

if __name__ == "__main__":
  print ("新年好!")
  
  #1.创建一个xml.parser
  parser = xml.sax.make_parser()
  
  #2.turn off name space
  parser.setFeature(xml.sax.handler.feature_namespaces, 0)

  #3.重写ContexHandler
  handler = MovieHandler()
  
