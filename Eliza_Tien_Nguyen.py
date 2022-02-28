# # -*- coding: utf-8 -*-
""" Eliza homework. Chatbot created by Tien Nguyen """
__author__= "Tien Nguyen"

print ("Eliza!")

import re
import random

print("Hi, my name is Elize. What's your name?")

user_name = input()

print("Nice to meet you, " +  user_name)

happy_comments = ["Oh Nice!", "Awsome" , "Good to hear that"]
random_happy_comment = random.choice(happy_comments)

sad_comments = ["Sorry to hear that. What happened?", "What's wrong?", "Tell me about it!"]
random_sad_comment = random.choice(sad_comments)

def answerlist(a):
  if re.findall(r'(good|happy|ok|joyful|excited)',a,re.I):
    print(random_happy_comment)
    print("How can I help you today?")
  elif re.findall(r'(bad|sad|tired|sick)',a,re.I):
    print(random_sad_comment)
  elif re.findall(r'(dad)',a,re.I):
    print("Are you close with your dad?")
  elif re.findall(r'(mom)',a,re.I):
    print("Do you talk to you mom frequently?")
  elif re.findall(r'(sister)',a,re.I):
    print("what do you like about your sister?")
  elif re.findall(r'(brother)',a,re.I):
    print("What annoys you most about your sister?")
  elif re.findall(r'(friend)',a,re.I):
    print("How long have you known each other?")
  elif re.findall(r'\b(\w+ed)\b',a,re.I):
    ed_word = re.findall(r'\b(\w+ed)\b',a,re.I)
    word=''.join(ed_word)
    sub_text = re.sub(r'.{2}$','', word)
    print("When did it", sub_text, "?")
  else:
    print("Tell me more...")

print("How are you today?")
while True:
  a1= input()
  if re.findall(r'(bye)',a1,re.I):
    print("Goodbye!")
    break
  else:
    answerlist(a1)
