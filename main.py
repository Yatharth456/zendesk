import requests
import json, os

# Set the credentials.

base_url = "https://abc9618.zendesk.com"
request_endpoint = "/api/v2/tickets/"
user = "goswami2001yatharth@gmail.com" + "/token"
password = "NTRkHML4RoPX6icjEWol8uM4AlH8mcUFe3Uvxy5p"
headers = {"content-type": "application/json"}



# 1> For getting data of Tickets.
def GetAllTickets():
    try:
        response = requests.get(base_url+request_endpoint, auth=(user, password))

        if response.status_code != 200:
            print("Response Code: ",  response.status_code)
            exit()
        else:
            data = response.json()
            ticket_list = data['tickets']
            # print(ticket_list)

        for ticket in ticket_list:
            print(f"Ticket ID: {ticket['id']}")
            print(f"Subject: {ticket['raw_subject']}")
            print(f"Description: {ticket['description']}")
            print(f"Priority: {ticket['priority']}")
            print(f"Due Date: {ticket['due_at']}")
            print()
            return ({
                "Ticket ID": {ticket['id']},
                "Subject": {ticket['raw_subject']},
                "Description": {ticket['description']},
                "Priority": {ticket['priority']},
                "Due Date": {ticket['due_at']},
            })
    except:
        return ("Something went wrong.")



#2> Creating new ticket.
def CreateTicket():
    
    subject = "Python API Test Ticket One"
    body = "Demonstrating creating a ticket with the Zendesk API using Python"
    type = "question"
    priority = "normal"
    
    # Package the data into a dictionary
    data = {"ticket": {"subject": subject, "type": type, "priority": priority, "comment": {"body": body}}}

    # Encode the data to create a JSON payload
    payload = json.dumps(data)
    try:
        # Send the HTTP post request
        response = requests.post(base_url+request_endpoint, data=payload, auth=(user, password), headers=headers)

        # Check for HTTP codes other than 201 (Created)
        if response.status_code != 201:
            print(f"Response Code: {response.status_code}. There was a problem with the request. Exiting.")
            return (f"Response Code: {response.status_code}. There was a problem with the request. Exiting.")
        else:
            print("Ticket created successfully.")
            return ("Ticket created successfully.")
    except:
        return ("Something went wrong.")



#3> For delete Ticket by ID.
def GetTicketByID(ticket_id):
    try:
        response = requests.get(f"{base_url+request_endpoint+str(ticket_id)}", auth=(user, password))
        if response.status_code != 200:
            print("Response Code: ",  response.status_code)
            return ("Response Code: ",  response.status_code)
        else:
            data = response.json()
            print(data['ticket'])
            return (data['ticket'])
    except:
        return ("Ticket ID not exist, please enter a valid Ticket ID.")



#4> For delete Ticket by ID.
def DeleteTicket(ticket_id):
    try:
        response = requests.delete(f"{base_url+request_endpoint+str(ticket_id)}", auth=(user, password))
        if response.status_code != 204:
            print("Response Code: ",  response.status_code)
            return ("Response Code: ",  response.status_code)
        else:
            print('Ticket deleted.')
            return ('Ticket deleted.')
    except:
        return ("Response Code", response.status_code)



#5> For updating ticket.
def UpdateTicketByID(ticket_id):
   
    data = {"ticket": {"status": "solved", "comment": {"public":False,"body":"This ticket has been resolved."}}}
    # data = {"ticket": {"status": "open"}}
    payload = json.dumps(data)
    try:
        response = requests.put(f"{base_url+request_endpoint+str(ticket_id)}.json", data=payload, auth=(user, password), headers=headers)
        if response.status_code != 200:
            print("Response Code: ",  response.status_code)
            return ("Response Code: ",  response.status_code)
        else:
            print("Updated successfully.")
            return ("Updated successfully.")
    except:
        return ("Something went wrong, Please try afer some time.")



#6> For getting all status of Tickets.
def GetAllStatus():
    try:
        response = requests.get(base_url+request_endpoint, auth=(user, password), headers=headers)

        if response.status_code != 200:
            print("Response Code: ",  response.status_code)
            exit()
        else:
            data = response.json()
            ticket_list = data['tickets']

        for ticket in ticket_list:
            print(f"Ticket ID: {ticket['id']}")
            print(f"requester: {ticket['requester_id']}")
            print(f"status: {ticket['status']}\n")
    except:
        return ("ConnectionError, Please try afer some time.")



#7> For count all tickets.
def CountAllTickets():
    try:
        response = requests.request("GET", base_url+request_endpoint, auth=(user, password), headers=headers)
        # print(response.text)
        data = response.json()
        ticket_list = data['count']
        print("Total tickets available in your dashboard is: ", ticket_list)
        return ("Total tickets available in your dashboard is: ", ticket_list)
    except:
        return ("ConnectionError, Please try afer some time.")



#8> For Restoring deleted ticket by ID.
def RestoreDeletedTicket(ticket_id):
    try:
        requests.request("PUT", f"{base_url}/api/v2/deleted_tickets/{ticket_id}/restore", auth=(user, password), headers=headers)
        print("Ticket restored.")
        return ("Ticket restored.")
    except Exception as e:
        return ("ConnectionError, Please try afer some time.")



#9> For getting email ccs by ID.
def GetEmailCCs(ticket_id):
    try:
        response = requests.request("GET", f"{base_url+request_endpoint+str(ticket_id)}/email_ccs", auth=(user, password), headers=headers)
        print(response.text)
        return (response.text)
    except Exception as e:
        return ("ConnectionError, Please try afer some time.")



#10> For getting tickets problems.
def TicketProblems():
    try:
        response = requests.request("GET", base_url+"/api/v2/problems", auth=(user, password), headers=headers)
        print(response.text)
        return (response.text)
    except:
        return ("ConnectionError, Please try afer some time.")



#11> For mark ticket as spam by ID.
def mark_as_spam(ticket_id):
    try:
        response = requests.request("GET", f"{base_url+request_endpoint+str(ticket_id)}/mark_as_spam", auth=(user, password), headers=headers)
        print(response.text)
        return (response.text)
    except:
        return ("ConnectionError, Please try afer some time.")



#12> For see the all deleted ticket.
def DeletedTickets():
    try:
        response = requests.request("GET", f"{base_url}/api/v2/deleted_tickets?sort_by=&sort_order=", auth=(user, password), headers=headers)
        print(response.text)
        data = response.json()
        print(data['deleted_tickets'])
        print(data['count'])
        return ({
            'deleted_tikents': data['deleted_tickets'],
            'Count': data['count']
            })
    except:
        return ("ConnectionError, Please try afer some time.")



#13> For getting followers on ticket by ID.
def GetFollowers(ticket_id):
    try:
        response = requests.request("PUT", f"{base_url+request_endpoint+str(ticket_id)}/followers", auth=(user, password), headers=headers)
        print(response.text)
        return (response.text)
    except Exception as e:
        return ("ConnectionError, Please try afer some time.")
    

