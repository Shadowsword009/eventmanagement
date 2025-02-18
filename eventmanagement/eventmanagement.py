events = {}

def view_events():
    if not events:
        print("No events scheduled.")
    else:
        print("\nScheduled Events:")
        for date, event_list in sorted(events.items()):
            print(f"Date: {date}")
            for event in event_list:
                print(f"    Event: {event['name']}, Time: {event['start_time']} - {event['end_time']}")

def create_event():
    date = input("Enter the date of the event (YYYY-MM-DD): ")
    start_time = input("Enter the start time of the event (HH:MM, 24-hour format): ")
    end_time = input("Enter the end time of the event (HH:MM, 24-hour format): ")
    if date in events:
        for event in events[date]:
            if (start_time < event['end_time'] and end_time > event['start_time']):
                print(f"Time conflict with event: {event['name']} ({event['start_time']} - {event['end_time']}).")
                return
    name = input("Enter the name of the event: ")
    new_event = {'name': name, 'start_time': start_time, 'end_time': end_time}
    if date not in events:
        events[date] = []
    events[date].append(new_event)
    print("Event created successfully.")

def update_event():
    if not events:
        print("No events scheduled.")
        return
    print("\nScheduled Events:")
    event_list = []
    idx = 1
    for date, event_details in sorted(events.items()):
        for event in event_details:
            print(f"{idx}. Date: {date}, Event: {event['name']}, Time: {event['start_time']} - {event['end_time']}")
            event_list.append((date, event))
            idx += 1
    try:
        event_choice = int(input("\nEnter the number of the event to update: "))
        if event_choice < 1 or event_choice > len(event_list):
            print("Invalid choice.")
        else:
            chosen_event = event_list[event_choice - 1]
            date_to_update, event_to_update = chosen_event
            new_name = input("Enter the new name of the event: ")
            new_start_time = input("Enter the new start time (HH:MM, 24-hour format): ")
            new_end_time = input("Enter the new end time (HH:MM, 24-hour format): ")
            for event in events[date_to_update]:
                if (new_start_time < event['end_time'] and new_end_time > event['start_time']) and event != event_to_update:
                    print("Time conflict with another event.")
                    return
            event_to_update['name'] = new_name
            event_to_update['start_time'] = new_start_time
            event_to_update['end_time'] = new_end_time
            print("Event updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
def cancel_event():
    if not events:
        print("No events scheduled.")
        return
    print("\nScheduled Events:")
    event_list = []
    idx = 1
    for date, event_details in sorted(events.items()):
        for event in event_details:
            print(f"{idx}. Date: {date}, Event: {event['name']}, Time: {event['start_time']} - {event['end_time']}")
            event_list.append((date, event))
            idx += 1
    try:
        event_choice = int(input("\nEnter the number of the event to cancel: "))
        if event_choice < 1 or event_choice > len(event_list):
            print("Invalid choice.")
        else:
            chosen_event = event_list[event_choice - 1]
            date_to_remove, event_to_remove = chosen_event
            events[date_to_remove].remove(event_to_remove)
            print("Event canceled successfully.")
            if not events[date_to_remove]:
                del events[date_to_remove]
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    switch = {
        '1': view_events,
        '2': create_event,
        '3': update_event,
        '4': cancel_event,
    }
    while True:
        print("\nEvent Management System")
        print("1. View all events")
        print("2. Create an event")
        print("3. Update an event")
        print("4. Cancel an event")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '5':
            print("Exiting the system. Goodbye!")
            break
        action = switch.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
