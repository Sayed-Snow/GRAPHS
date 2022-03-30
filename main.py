from datetime import datetime
import json
import requests
import matplotlib.pyplot as plt

response = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com")

un_date = []
un_users = []
f_date = []
f_users = []
users = json.loads(response.text)
for i in users:
    un_date.append(i)
    un_users.append(users[i])

begin = str(input("Do you wish to filter the data?(yes or no)"))

if begin.lower() == 'yes':

    start = str(input('Enter Start date(dd-mm-yyyy): '))
    end = str(input('Enter End date(dd-mm-yyyy): '))
    for x in users:
        if start == x:
            j = x
        if end == x:
            p = x

    new_start = datetime.strptime(j, "%d-%m-%Y")
    new_end = datetime.strptime(p, "%d-%m-%Y")

    delta = new_end - new_start

    for i in range(len(un_date)):
        if start == un_date[i]:
            for j in range(delta.days + 1):
                f_date.append(un_date[i])
                f_users.append(un_users[i])
                i += 1

    plt.plot(f_date, f_users)
    plt.title(' Users Vs Year')
    plt.xlabel('Year')
    plt.ylabel('Users')
    plt.show()
if begin.lower() == 'no':
    plt.plot(un_date, un_users)
    plt.title(' Users Vs Year')
    plt.xlabel('Year')
    plt.ylabel('Users')
    plt.show()
