events={}
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