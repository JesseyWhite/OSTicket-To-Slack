import requests
from bs4 import BeautifulSoup
import json

# def comment_ticket(message, ticket_id):
# TODO


# def reply_ticket(message, ticket_id):
# TODO


# def close_ticket(message, ticket_id):
# TODO


def find_tickets(soup):
    tickets_list = []
    for new in soup.tbody.find_all('tr'):
        ticket = {}
        ticket['id'] = new.contents[1].contents[0]['value']
        ticket['link'] = payload['DOMAIN'] + 'support/scp/tickets.php?id=' + ticket['id']
        ticket['TicketNo'] = new.contents[3].text.strip()
        ticket['LastUpdate'] = new.contents[4].text.strip()
        # Have to strip twice because the number of reply is in this string. makes it look bad, removed 2
        # characters just in case it is a long string of replies
        ticket['Subject'] = new.contents[5].contents[1].text.strip()
        ticket['From'] = new.contents[6].text.strip()
        ticket['Priority'] = new.contents[7].text.strip()
        if new.contents[8].text.strip() == '':
            ticket['Assigned'] = 'Unclaimed'
        else:
            ticket['Assigned'] = new.contents[8].text.strip()
        tickets_list.append(ticket)
    return tickets_list


'''
Loading Sensitive files from .gitignore and making them into a dict
'''

with open(".gitignore/package.json") as mylittlefile:
    payload = json.load(mylittlefile)

# This URL will be the URL that your login form points to with the "action" tag.
PRE_LOGIN_URL = payload["LOGIN_URL"]

# This URL is the page you actually want to pull down with requests.
REQUEST_URL = payload["POST_LOGIN_URL"]

# dict that contains login information
credentials = {
    'userid': payload["userid"],
    'passwd': payload["passwd"],
    '__CSRFToken__': payload["__CSRFToken__"],
    'do': payload["do"],
    'submit': payload["submit"]
}

# Creating a live session
with requests.Session() as current:

    # Go to the login page to get the __CSRFToken__.
    # The token is unique to every session.
    live = current.get(PRE_LOGIN_URL)

    # Convert the login page into something Beautiful Soup can read.
    soup = BeautifulSoup(live.content, 'html.parser')

    # Find the Token and then record the value of the token into the payload dict
    credentials["__CSRFToken__"] = soup.input['value']

    # Deliver the payload AKA Log into the website
    current.post(PRE_LOGIN_URL, data=credentials, headers={"Referer": "https://www.se.edu/"})

    '''
    You should now be inside the website.
    '''

    # Getting Page inside of OS TICKET
    page = current.get(REQUEST_URL)

    # making it readable
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup)

    list_of_tickets = find_tickets(soup)

    for x in list_of_tickets:
        print(x)

# End of File
quit(0)
