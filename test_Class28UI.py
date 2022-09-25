
from LoginPage import  *
def test_Login_UI():
  result  =Login_Page()
  assert result == True

def test_invlid_login_ui():
  result  = Invalid_Login_Page()
  assert result == "Epic sadface: Username and password do not match any user in this service"


# JIRA,Github ,Jenkins
# Ticketing tool => JIRA
# waterfall => Once upon a time
# Agile methodology => Ceremonies => Sprint Planing , Daily scrum, sprint review, Sprint Retro ,
# Sprint backlog refinement
# PO(Product owner) ,Scrum master , Developers, testers
# Sprint Planing => we will plan work for next two weeks (sprint duration will be two weeks)
# Daily scrum => we will discuss what we have done yesterday , what we are working today , any blocker
# Sprint review => we will showcase the work what we have done in 2 weeks to PO and stack holders and every one
# Sprint retro => We will discuss what went well in the sprint , what didn't well , any ideas
# Action items => what things to do make it things gud and assign the responsible person


# Git hub => Version control
# its a repository to store the code

# Jenkins => server => we will have jobs => Dev ops => by using those job we will run the test cases




