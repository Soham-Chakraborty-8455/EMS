from ..tickets import ticket1, ticket2, ticket3

def create_ticket(template, participant, event):
    if template == "1":
        ticket1.make_tickets1(participant.name, event.eventname, event.startdate, event.orgname, event.venue, participant.email, participant.phone, event.starttime)
    elif template == "2":
        ticket2.make_tickets2(participant.name, event.eventname, event.startdate, event.orgname, event.venue, participant.email, participant.phone, event.starttime)
    elif template == "3":
        ticket3.make_tickets3(participant.name, event.eventname, event.startdate, event.orgname, event.venue, participant.email, participant.phone, event.starttime)
