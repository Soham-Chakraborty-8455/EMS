# app/services/email_service.py

# from flask_mail import Message
# from flask import render_template
# from .. import mail
# from flask import current_app

def send_registration_email(recipient_email, participant, event):
    """
    Sends a registration email to the participant.

    :param recipient_email: Email address of the participant
    :param participant: Participants object containing participant details
    :param event: EventDetails object containing event details
    """
    # try:
    #     msg = Message(
    #         subject=f"Registration Confirmation for {event.eventname}",
    #         recipients=[recipient_email]
    #     )
    #     msg.body = render_template('emails/registration_confirmation.txt', participant=participant, event=event)
    #     msg.html = render_template('emails/registration_confirmation.html', participant=participant, event=event)
    #     mail.send(msg)
    #     print(f"Registration email sent to {recipient_email}")
    # except Exception as e:
    #     print(f"Failed to send email to {recipient_email}: {e}")
