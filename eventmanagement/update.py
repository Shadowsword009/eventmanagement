events ={}
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

            # Check for time conflict
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
