import sys

# Constants:
START_ROOM = 'Time Headquarters'


# Intro Class:
class TitleIntro:
    def __init__(self):
        self.title = "  Temporal Odyssey: Guardians of the Continuum  "
        self.owner = "  By: Cameron Soller  "
        self.story_background = """
            In the epoch of 2341, an organization known as "The Keepers" has been entrusted with the formidable 
            responsibility of safeguarding the temporal continuum from malevolent forces. Following a pivotal 
            breakthrough in temporal technology subsequent to the 21st century, a revolutionary device emerged, 
            endowed with the unprecedented capability to navigate seamlessly through the dimensions of time and space. 
            At the forefront of this critical mission stands none other than yourself – the apex operative within 
            The Keepers, armed with the pinnacle of temporal advancement, the time-traveling device. 
            As the vanguard of this cutting-edge technology, you bear the pivotal role in upholding the sanctity of 
            the timeline and thwarting the nefarious threats that jeopardize the very fabric of existence.
        """

    def display_welcome_text(self):
        # Create a box around title
        title_box = f"+{'=' * (len(self.title) + 4)}+"

        # Print the box and content
        print(title_box)
        print(f"| {self.title}   |")
        print(title_box)

        # print owner
        print(f"  {self.owner}")
        print(f"{'_' * (len(self.title) + 6)}")

        # Print the story background
        print(self.story_background)


# Functions
def display_room_with_border(current_room):
    border_length = len(current_room) + 4  # Adjusting for borders
    print("_" * border_length)
    print(f"| {current_room} |")
    print("_" * border_length)


def move_through_portal(destination_room):
    display_room_with_border(destination_room)
    print(f"A PORTAL OPENS AND YOU ENTER THE PORTAL\nYou are now in the {destination_room}")


def press_enter_to_continue():
    # Enter to Continue Story Prompt
    user_input = input("Press ENTER to continue\n...or type 'E' to exit: ")
    if user_input == '':
        print()
        return True  # Continue the game
    elif user_input.upper() == 'E':
        print("Exiting the game.")
        sys.exit()  # Exit the entire program
    else:
        print("** Invalid input. Please try again. **")
        print()
        return press_enter_to_continue()  # Recursive call for re-entering input


def game_over():
    print("Game Over! Thanks for playing.")
    sys.exit()


# Game Play Class
class StartJourney:
    def __init__(self):
        self.rooms = {
            'Time Headquarters': {'Renaissance Library': 'North', 'Medieval Castle Dungeon': 'East',
                                  'Futuristic Laboratory': 'South', 'World War II Bunker': 'West'},
            'Renaissance Library': {'Time Headquarters': 'South', 'Ancient Pyramid Chamber': 'East'},
            'Ancient Pyramid Chamber': {'Renaissance Library': 'West'},
            'World War II Bunker': {'Time Headquarters': 'East', 'Space Age Observatory': 'South'},
            'Space Age Observatory': {'World War II Bunker': 'North'},
            'Futuristic Laboratory': {'Time Headquarters': 'North', 'Victorian Era Parlor': 'East'},
            'Victorian Era Parlor': {'Futuristic Laboratory': 'West'},
            'Medieval Castle Dungeon': {'Time Headquarters': 'West', 'Prehistoric Cave': 'North'},
            'Prehistoric Cave': {'Medieval Castle Dungeon': 'West'}
        }

        self.items = {
            'Time Headquarters': None,
            'Renaissance Library': 'Amulet of blood',
            'Ancient Pyramid Chamber': 'Mask of Tutankhamun',
            'World War II Bunker': 'Compass',
            'Space Age Observatory': 'Astronaut Gloves',
            'Futuristic Laboratory': 'Sonic Screwdriver',
            'Victorian Era Parlor': 'Tiara',
            'Medieval Castle Dungeon': 'Rusted Key',
            'Prehistoric Cave': None
        }

        self.descriptions = {
            'Time Headquarters': "The central hub for timekeepers. It's filled with advanced technology and monitors "
                                 "displaying temporal anomalies.",
            'Renaissance Library': 'A vast library containing knowledge from the Renaissance era. Books and scrolls '
                                   'line the shelves.',
            'Ancient Pyramid Chamber': 'A mysterious chamber within an ancient pyramid. Hieroglyphics cover the walls.',
            'World War II Bunker': 'A bunker from the World War II era, equipped with maps and wartime supplies.',
            'Space Age Observatory': 'An observatory near Mars. Telescopes and futuristic equipment fill the '
                                     'room.',
            'Futuristic Laboratory': 'A high-tech laboratory with advanced machinery and prototypes.',
            'Victorian Era Parlor': 'A luxurious parlor from the Victorian era, adorned with elegant furniture and '
                                    'decor.',
            'Medieval Castle Dungeon': 'A dark and damp dungeon within a medieval castle. Rusty chains hang from the '
                                       'walls.',
            'Prehistoric Cave': 'A cave from the prehistoric era. The air is thick, and primitive drawings mark the '
                                'walls.'
        }

        self.player_inventory = []

    def display_room_description(self, current_room):
        print(f"\n{current_room}:\n{self.descriptions[current_room]}")

        # Use get method to handle KeyError
        item_in_room = self.items.get(current_room, None)
        if item_in_room is not None:
            print(f"Item in this room: {item_in_room}\n")
        else:
            print("No item in this room.\n")

    def replace_items_with_prison_cube(self):
        items_to_replace = ['Amulet of blood', 'Mask of Tutankhamun', 'Compass',
                            'Astronaut Gloves', 'Sonic Screwdriver', 'Tiara', 'Rusted Key']

        if all(item in self.player_inventory for item in items_to_replace):
            print("\nCongratulations! You have collected all required items.")
            print("Your items have evolved into the 'Prison Cube'.")
            self.player_inventory = ['Prison Cube']

    def check_win_condition(self, current_room):
        if 'Prison Cube' in self.player_inventory and current_room == 'Prehistoric Cave':
            print("\nCongratulations! You have successfully collected all items and saved the timeline.")
            print("You win! Thanks for playing.")
            sys.exit()

    def search_room_for_item(self, current_room):
        # Use get method to handle KeyError
        item_in_room = self.items.get(current_room, None)

        if item_in_room is not None:
            user_input = input(f"Do you want to search for the '{item_in_room}' in this room? (Y/N): ").upper()

            if user_input == 'Y':
                print(f"You found the '{item_in_room}'! Adding it to your inventory.")
                self.player_inventory.append(item_in_room)
                del self.items[current_room]
                self.check_all_items_collected()
                self.replace_items_with_prison_cube()
                self.check_win_condition(current_room)
        else:
            print("No item to search in this room.")

    def check_all_items_collected(self):
        # When all items are collected the player's inventory changed to one ultimate item
        if all(item == 'Prison Cube' for item in self.player_inventory):
            print("\nCongratulations! You have found all items, and they have evolved into the 'Prison Cube'.")

    def check_prison_cube_on_entering_cave(self):
        # if the ultimate item is not in inventory when player enters Prehistoric Cave, Loose!
        if 'Prehistoric Cave' in self.rooms and 'Prison Cube' not in self.player_inventory:
            print("\nYou enter the Prehistoric Cave, but you do not have the 'Prison Cube'. Game Over!")
            game_over()

    def play_game(self):
        # Main Gameplay
        current_room = 'Time Headquarters'
        display_room_with_border(current_room)  # Room Header
        self.display_room_description(current_room)  # Room Description
        self.search_room_for_item(current_room)  # Check if item in current room

        while True:
            directions = ', '.join(self.rooms[current_room].values())
            next_move = input(  # Get and print current room directions
                f"Available directions: {directions}\nEnter the direction you want to go, or type 'E' to exit: ")

            if next_move.upper() == 'E':
                print("Exiting the game. Goodbye!")
                break

            possible_destinations = [room for room, direction in self.rooms[current_room].items() if
                                     direction.upper() == next_move.upper()]
            if possible_destinations:
                next_destination = possible_destinations[0]
                move_through_portal(next_destination)
                current_room = next_destination
                self.display_room_description(current_room)
                self.search_room_for_item(current_room)
                self.replace_items_with_prison_cube()

                # Check for win condition
                self.check_win_condition(current_room)

                # Check for Prehistoric Cave condition
                if current_room == 'Prehistoric Cave':
                    self.check_prison_cube_on_entering_cave()

            else:
                print("Invalid move. You cannot go in that direction from here.")
