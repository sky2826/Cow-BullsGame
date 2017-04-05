#!/usr/bin/python3


import bs4 as bs
import string
import html.parser
import urllib
import random
import math



#//////////////////////////////////////////////////////setting up playing variable////////////////////////////////////////////////////////////#

random_word="boob"
attempt=0
choice=10
def set_play_variable():
 global random_word
 try:
   alphabet_list=list(string.ascii_lowercase[:]) 
   url='https://www.morewords.com/unique-letters/4' #url to find 4 letter word with unique alphabets
   random_alphabet=random.choice(alphabet_list)
   url=url+random_alphabet+'/'
   sauce=urllib.request.urlopen(url).read()
   soup=bs.BeautifulSoup(sauce,'html.parser')
   p_set=soup.div.find_all('p')
   a_set=p_set[2].find_all('a')
   random_word=a_set[math.floor(random.random()*len(a_set))].text
 except:
   print("no internet or something went wrong try again with internet connection")
   exit()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def res():
  restart=input("press 1 to restart else exit  : ")
  if(restart=='1'):
   guess()
  else:
   exit()


def won():
 print("right guess in {0:d} attempts".format(attempt-1))
 res()

def lost():
 print("you loss, rigth word is {0:s}".format(random_word))
 res()

def helper():
 print("all the characters in words should be unique and it should be 4 letter word")
 play()


def play():
 global random_word
 global choice
 global attempt
 if(choice):
  print("No. of guesses left :{0:d}".format(choice))
  guess_word=input("Guess the word : ")
  if(len(set(guess_word))!=4):
   helper()
  else:
   choice-=1
   attempt+=1
   if(guess_word==random_word):
    won()
   else:
    common_set=set(guess_word)&set(random_word)
    count=0
    for i in common_set:
      if(guess_word.find(i)==random_word.find(i)):
       count+=1
    print("No. of Bulls : {0:d}".format(count))
    print("No. of cows : {0:d}".format(len(common_set)-count))
    play()
 else:
  lost()
     
   

def guess():
 global choice
 global attempt
 choice=10
 attempt=0
 set_play_variable()
 print("Rules:\n")
 print("1)You have 10 options to guess the right word\n")
 print("2)The word will be of 4 alphabets\n")
 print("3)All alphabets are unique\n")
 print("4)No. of bulls represent right alphabet guessed with right position\n")
 print("5)No. of cows represent right alphabet guessed with wrong position\n")
 start=input("Enter 1 to start or anyother key to exit : ")
 if(start=="1"):
  play()
 else:
  exit()


if __name__=='__main__':
 guess()
