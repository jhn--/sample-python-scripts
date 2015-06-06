#! /usr/bin/env python

'''
Assume there is a REST API available at "http://www.linkedin.corp/api" for accessing employee information The employee information endpoint is "/employee/<id>" Each employee record you retrieve will be a JSON object with the following keys:

'name'  refers to a String that contains the employee's first and last name
'title' refers to a String that contains the employee's job title
'reports' refers to an Array of Strings containing the IDs of the employee's direct reports
'id' id of that employee 

Write a function that will take an employee ID and print out the hierarchy of employees under that employee.


 
-----------Begin Sample Output--------------
Flynn Mackie - Senior VP of Engineering
  Wesley Thomas - VP of Design
    Randall Cosmo - Director of Design
      Brenda Plager - Senior Designer
  Nina Chiswick - VP of Engineering
    Tommy Quinn - Director of Engineering
      Jake Farmer - Frontend Manager
        Liam Freeman - Junior Code Monkey
      Sheila Dunbar - Backend Manager
        Peter Young - Senior Code Cowboy
-----------End Sample Output--------------
'''

'''
def fetch_from_api(employee_id):
     example response 
    result = {'name': 'Joe Smith',
              'title': 'svp', 
              'reports': ['John Smith'],
              'id': 1234}
    
    result = {}
    #TODO: fetches from api
    return result
'''
result = {'name': 'Joe Smith', 'title': 'svp', 'reports': ['John Smith'], 'id': 1234}
'''
list_of_ids = []

for i in result.keys():
  if i == 'id':
    list_of_ids.append(result['id'])

print list_of_ids
'''

searchid = int(raw_input("Enter employee id: "))
'''
def id_exists(searchid, list_of_ids):
  for i in list_of_ids:
    if searchid == i:
      getinfo(result, searchid)
'''
def getinfo(result, searchid):
      if searchid == result['id']:
          print result['name'], "-", result['title']
      else:
        print "No such employee found."


#id_exists(searchid, list_of_ids)
getinfo(result, searchid)