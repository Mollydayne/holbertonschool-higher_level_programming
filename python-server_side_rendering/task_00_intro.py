import os

def generate_invitations(template, attendees):
    """
    Generating invites with a template and a list of attendees
    template: (str) Text with placeholders {name}, {event_title}, etc.
    attendees: (list) dict with list of people invited
    """

    # chekin to see if its the type of data we want
    if not isinstance(template, str):
        print("Template is not a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Attendees is not a list of dictionaries")
        return

    # Checkin if entry is not empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Loop to handle each invited people

    for index, attendee in enumerate(attendees, start=1):
        try:
            # Replacing placeholders
            invitation = template.replace("{name}", attendee.get("name", "N/A"))
            invitation = invitation.replace("{event_title}", attendee.get("event_title", "N/A"))
            invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A"))
            invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))

            # Generating a file for each invited people
            output_filename = f"output_{index}.txt"

            # Chekin if file already exists
            if os.path.exists(output_filename):
                print(f"The file '{output_filename}' already exists, it will not be overwritten.")
                continue

            # Writting in the previously created file
            with open(output_filename, "w", encoding="utf-8") as file:
                file.write(invitation)

            print(f"Invitation successfully written to '{output_filename}'.")

        except Exception as e:
            print(f"Error: An error occurred while generating '{output_filename}': {e}")

