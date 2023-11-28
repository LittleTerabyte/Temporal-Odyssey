import my_modules
import re

# Initiate start room
current_room = my_modules.START_ROOM
# Display Title and Story Background
intro = my_modules.TitleIntro()  # Create an instance of the TitleIntro class
intro.display_welcome_text()  # Call the method to display welcome text

# Press ENTER to continue
if my_modules.press_enter_to_continue():
    print()
else:
    print("Game is exiting...")

while True:
    hero_name = input("Enter your name.\n(Or the name of our hero.)")  # Gets hero's name from user
    # Check to see if input is characters only.
    if re.match("^[a-zA-Z]+$", hero_name):
        break
    else:
        print("\nInvalid input. Please enter characters only, without numbers or special characters.")
        print()

print()
print("""
            ! RING RING RING !
            You roll over to check your phone and see your boss calling.""")
print()
boss_message = f"""
            "{hero_name} there has been an emergency at the agency! I need you here as soon as possible, the fate of the
            world is in your hands! Do you still have your mobile teleporter?"
"""
answer_phone = input(str("To answer phone, press 'P'"))
if answer_phone.upper() == 'P':  # Some fun text if an invalid response is inputted by user
    print(boss_message)
else:
    print("""
            As much as you dont want to...
            **IT IS YOUR BOSS, YOU MUST ANSWER IT**
            You reach over and accept the call.
            """)
    print(f"{boss_message}")

boss_instructions = f"""
            "Thank goodness! Get to the {my_modules.START_ROOM.lower()} and I will explain the situation."
            \n"""
answer_teleporter_question = input(str("Press 'Y' for Yes.\nPress 'N' for No."))
if answer_teleporter_question.upper() == 'Y':  # More fun text if invalid response
    print(boss_instructions)
else:
    print("""
            You begin to say that you left your teleporter at the agency headquarters but then you see it laying on 
            the counter next to your phone...
            "Yes sir, I have it here."
            """)
    print(f"{boss_instructions}")

print(f"""
            You hang up the phone and get into your black robe uniform.
            Using your teleporter you open a portal to the {current_room.lower()}""")
print()

if my_modules.press_enter_to_continue():  # Press Enter to continue
    print()
else:
    print("Game is exiting...")

# Move through a portal and display the new room header (Starting Room)
print(f"A PORTAL OPENS AND YOU ENTER THE PORTAL\nYou are now in the {current_room})")
my_modules.display_room_with_border(current_room)

# Message from player's boss
print(f"""
            "{hero_name} A grave concern has arisen regarding the stability of the temporal continuum. Numerous minute 
            temporal rifts have manifested across time. While the current repercussions on the timeline remain within 
            manageable bounds, intelligence reports have identified the source of these anomalies. The instigator is 
            none other than the Chronos Saboteur, a former operative of The Keepers, who has deviated from their ranks. 
            It is strongly suspected that the saboteur is traversing the vast expanse of time and space with the 
            intention of manipulating pivotal events. Should these endeavors persist unchecked, the ensuing damage to 
            the timeline poses a severe threat, placing the entirety of existence in jeopardy."

            "Your designated mission entails the retrieval of specific artifacts possessing the capability to construct 
            a temporal prison, thereby restraining Chronos and mitigating this imminent peril. Regrettably, these vital 
            artifacts have been dispersed across different temporal epochs. Recognizing the inevitability of our 
            resorting to this countermeasure, Chronos preemptively purloined them from archival repositories. 
            Fortunately, our tracking mechanisms remain operational, and a comprehensive list of the artifacts will be
            furnished to facilitate your pursuit."
        
        
            -The list of locations have been imported into your teleporter. 
            
            "Good luck, {hero_name}. We are counting on you!"
""")
if my_modules.press_enter_to_continue():  # Press Enter to continue
    print()
else:
    print("Game is exiting...")
# Start the journey // Call Main gameplay class
play_instance = my_modules.StartJourney()
play_instance.play_game()
