import os
from PIL import Image, ImageDraw, ImageFont
import uuid

def pick(name):
  filename=name
  ironman = Image.open(filename, 'r')
  filename1='tomskij_politehnicheskij_universitet.jpg'
  bg = Image.open(filename1, 'r')
  text_img = Image.new('RGBA', (600,320), (500, 100, 10, 10))
  text_img.paste(bg, (0,0))
  text_img.paste(ironman, (0,0), mask=ironman)
  newName = str(uuid.uuid4())
  text_img.save(newName+".png", format="png")
  return newName+".png"