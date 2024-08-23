# Event Management System (EMS)

![EMS Banner](./docs/banner.png)

## Overview

The Event Management System (EMS) is a web application designed to streamline the process of managing events. It offers features such as generating banners, ID cards for volunteers, certificates, and handling participant registrations. Built using Python and Flask, EMS provides an easy-to-use interface for event organizers to manage their events efficiently.

## Features

- **Event Creation**: Organizers can create events by entering details such as the event name, venue, date, time, organizer's name, speaker's name, and uploading volunteer names via a CSV file.
- **Generate Banners**: Automatically create event banners with event details using Pillow for image processing.
- **Volunteer ID Cards**: Generate and send ID cards to volunteers, delivered directly to the organizer's email.
- **Send Certificates**: Send personalized certificates to participants after authentication using the organizer's email and phone number.
- **Participant Registration**: Participants can register for events by providing their name, phone number, and email.
- **Email Notifications**: Utilize Flask-Mail to send emails for confirmations, ID cards, and certificates.

## Technology Stack

- **Backend**: Python, Flask
- **Database**: SQLite (development), PostgreSQL (production)
- **Image Processing**: Pillow
- **Email**: Flask-Mail
- **Forms**: Flask-WTF
- **Database ORM**: SQLAlchemy

## Usage

### Event Creation

1. **Go to the Homepage**
    - Start by navigating to the homepage of the application.

2. **Click on the "+New Event" Button**
    - Find the "+New Event" button on the homepage and click it to create a new event.

3. **Fill in the Event Details**
    - Enter the following information in the provided form:
        - **Event Name**: The name of the event.
        - **Venue**: The location where the event will be held.
        - **Date & Time**: When the event is scheduled.
        - **Organizer Name**: The name of the person or team organizing the event.
        - **Speaker Name**: The name of the main speaker or guest.
        - **Volunteers**: Upload a CSV file containing the names of volunteers.

4. **Click "Add Event"**
    - After filling in all the details, click the "Add Event" button to save the event.
    - The newly created event will now appear in a table on the homepage.

### Generating Banners

- **Click the "View Banner" Button**
    - Next to each event in the table, you'll find a "View Banner" button. Click it to automatically generate a visual banner for the event.
    - The banner will include all the event details and can be customized for printing or online sharing.

### Volunteer ID Cards

- **Click the "Generate ID Card" Button**
    - For each event, there is an option to generate ID cards for volunteers.
    - Click the "Generate ID Card" button, and the system will create personalized ID cards for each volunteer listed in the CSV file.
    - The ID cards will be sent directly to the organizer's email address.

### Sending Certificates

- **Click the "Send Certificate" Button**
    - To send certificates to participants, click the "Send Certificate" button.
    - You will be prompted to authenticate using the organizer's email and phone number.
    - Once authenticated, the system will send personalized certificates to the participants.

### Participant Registration

- **Register for an Event**
    - Participants interested in attending the event can register by clicking the "Register for Event" button next to the event listing.
    - A registration form will appear, prompting participants to enter their details:
        - **Name**: Participant's full name.
        - **Phone Number**: A contact number for follow-up.
        - **Email**: An email address to receive notifications and confirmation.
    - After filling out the form, participants can submit their registration, and they will receive a confirmation email with further details about the event.
