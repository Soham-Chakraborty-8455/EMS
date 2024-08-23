from ..certificates import certificate1, certificate2, certificate3

def create_certificate(template, data, event):
    if template == "1":
        certificate1.make_certificates1(data['name'], data['pronoun'], event.eventname, "Organizer", event.orgname, event.signature, event.logo)
    elif template == "2":
        certificate2.make_certificates2(data['name'], event.eventname, event.startdate, event.venue, "Organizer", event.orgname, event.signature, event.logo)
    elif template == "3":
        certificate3.make_certificates3(data['name'], event.eventname, event.startdate, event.orgname, "Organizer", event.orgname, event.signature, event.logo)
