import random
import openai
import dotenv
import os
import json

dotenv.load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')



class Sim:
    def __init__(self):
        self.needs = {
            "hunger": 10,
            "hygiene": 10,
            "bladder": 10,
            "energy": 10,
            "social": 10,
            "fun": 10,
            "environment": 10,
            "comfort": 10
        }
        self.mood = "happy"  # Add mood attribute
        self.days = 0  # Add days attribute
        self.SimsJournal = {}  # Add SimsJournal attribute

    def reduce_needs(self):
        for need in self.needs:
            self.needs[need] = max(0, self.needs[need] - random.randint(1, 3))
            if self.needs[need] == 0:
                return need
        return None


    def check_needs(self):
        lowest_need = min(self.needs, key=self.needs.get)
        return lowest_need

    def print_needs(self):
        for need, value in self.needs.items():
            print(f"{need.capitalize()}: {value}")

    def choose_item(self):
        sorted_needs = sorted(self.needs.items(), key=lambda x: x[1])
        for need, value in sorted_needs:
            if value < 3:
                return need
        return None


class simsRoom:
    def __init__(self):
        self.theSim = Sim()
        self.needs_to_items = {
            "hunger": self.use_fridge,
            "hygiene": self.use_shower,
            "bladder": self.use_toilet,
            "energy": self.use_bed,
            "fun": self.use_tv,
            "environment": self.use_painting_on_the_wall,
            "comfort": self.use_couch,
            "social": self.use_telephone
        }

    def use_fridge(self):
        print("\nThe Sim is using the fridge to grab something to eat.")
        self.theSim.needs["hunger"] = min(10, self.theSim.needs["hunger"] + 8)
        self.theSim.needs["energy"] = max(0, self.theSim.needs["energy"] - 1)  # Deduct 1 energy
        self.update_journal("used fridge")  # Update journal

    def use_shower(self):
        print("\nThe Sim is having a shower.")
        self.theSim.needs["hygiene"] = min(10, self.theSim.needs["hygiene"] + 8)
        self.theSim.needs["comfort"] = min(10, self.theSim.needs["comfort"] + 2)
        self.theSim.needs["environment"] = min(10, self.theSim.needs["environment"] + 1)
        self.theSim.needs["energy"] = max(0, self.theSim.needs["energy"] - 1)  # Deduct 1 energy
        self.update_journal("took a shower")  # Update journal


    def use_toilet(self):
        print("\nThe Sim is using the toilet.")
        self.theSim.needs["bladder"] = min(10, self.theSim.needs["bladder"] + 4)
        self.theSim.needs["energy"] = max(0, self.theSim.needs["energy"] - 1)  # Deduct 1 energy
        self.update_journal("used toilet")  # Update journal

    def use_bed(self):
        print("\nThe Sim is going to sleep.")
        self.theSim.needs["energy"] = min(10, self.theSim.needs["energy"] + 10)
        self.theSim.needs["comfort"] = min(10, self.theSim.needs["comfort"] + 10)
        self.update_journal("went to sleep")  # Update journal
        self.theSim.days += 1  # Increment days
        self.theSim.SimsJournal[self.theSim.days] = []  # Start a new day in the journal

    def update_journal(self, activity):
        if self.theSim.days not in self.theSim.SimsJournal:
            self.theSim.SimsJournal[self.theSim.days] = []  # Initialize a new day in the journal
        self.theSim.SimsJournal[self.theSim.days].append({"activity": activity, "mood": self.theSim.mood})  # Update SimsJournal

        # Save the journal to a JSON file
        with open('sims_journal.json', 'w') as f:
            json.dump(self.theSim.SimsJournal, f)

    def use_tv(self):
        print("\nThe Sim is watching TV.")
        self.theSim.needs["fun"] = min(10, self.theSim.needs["fun"] + 3)
        self.theSim.needs["comfort"] = min(10, self.theSim.needs["comfort"] + 2)
        self.theSim.needs["environment"] = min(10, self.theSim.needs["environment"] + 1)
        self.theSim.needs["energy"] = max(0, self.theSim.needs["energy"] - 1)  # Deduct 1 energy
        self.update_journal("watched TV")  # Update journal


    def use_couch(self):
        print("\nThe Sim is sitting on the couch.")
        self.theSim.needs["comfort"] = min(10, self.theSim.needs["comfort"] + 8)
        self.theSim.needs["fun"] = min(10, self.theSim.needs["fun"] + 1)
        self.theSim.needs["energy"] = max(0, self.theSim.needs["energy"] + 1)
        self.update_journal("sat on the couch")  # Update journal

    def use_painting_on_the_wall(self):
        print("\nThe Sim is looking at the framed painting.")
        self.theSim.needs["environment"] = min(10, self.theSim.needs["environment"] + 5)
        self.theSim.needs["fun"] = min(10, self.theSim.needs["fun"] + 5)
        self.theSim.needs["energy"] = max(0, self.theSim.needs["energy"] - 1)  # Deduct 1 energy
        self.update_journal("looked at the framed painting")  # Update journal

    def use_telephone(self):
        print("\nThe Sim is making a phonecall.")
        self.theSim.needs["social"] = min(10, self.theSim.needs["social"] + 5)
        self.theSim.needs["fun"] = min(10, self.theSim.needs["fun"] + 2)
        self.theSim.needs["energy"] = max(0, self.theSim.needs["energy"] - 1)
        self.update_journal("talked on the phone")  # Update journal
        telephone_call = TelephoneCall(self.theSim)
        telephone_call.start_call()

    def chat(self):
        print("Type 'quit' to end the chat.")
        while True:
            need = self.theSim.check_needs()
            if need:
                self.needs_to_items[need]()
                print("\nSim Stats:")
                self.theSim.print_needs()
                print()

            user_input = input("\nPress Enter to proceed or type 'quit' to end the chat: ")
            if user_input.lower() == "quit":
                break

            need = self.theSim.reduce_needs()
            if need:
                self.needs_to_items[need]()
                print("\nSim Stats:") 
                self.theSim.print_needs()
                print()

            chosen_item = self.theSim.choose_item()
            if chosen_item:
                if self.theSim.needs[chosen_item] > 8:
                    print(f"The Sim's {chosen_item} need is too high. Rechoosing item...")
                    chosen_item = self.theSim.choose_item()
                #print(f"The Sim chooses to use {chosen_item}.")
                self.needs_to_items[chosen_item]()
                print("\nSim Stats:")
                self.theSim.print_needs()
                print()
                if self.theSim.needs[chosen_item] < 1:
                    print(f"The Sim's {chosen_item} need reached 0. Ending the chat.")
                    break

        print("The chat has ended.")



    def calculate_mood(self):
        total_needs = sum(self.needs.values())
        if total_needs < 40:
            self.mood = "stressed"
        else:
            self.mood = "happy"

class TelephoneCall:
    def __init__(self, sim):
        self.sim = sim

    def start_call(self):

        print("Telephone is ringing...")
        print("Sim: Hello?")
        while True:
            user_input = input("User: ")
            # Format the prompt in a more conversational way
            needs_str = ', '.join(f'{k} is at {v}' for k, v in self.sim.needs.items())
            prompt = f"Sim: My current needs are: {needs_str}.\nUser: {user_input}\n"
            response = openai_chat(prompt, self.sim.mood, self.sim.SimsJournal)  # Pass mood to openai_chat
            print(response)
            self.sim.reduce_needs()
            print("\nCurrent Sim needs:")
            self.sim.print_needs()
            print()
            lowest_need = self.sim.check_needs()
            # Check if any of the Sim's needs have reached 0 before ending the call
            if lowest_need and self.sim.needs[lowest_need] < 1:
                print(f"The Sim needs {lowest_need}.")
                return
            elif user_input.lower() == "hangup":
                print("The Sim hangs up the call.")
                return

            #print("The Sim returns to the chat room.")

def openai_chat(prompt, mood, journal):
    temperature = 0.8 if mood == "satisfied" else 0.4  # Adjust temperature based on mood
    current_day = max(journal.keys())
    current_day_activities = ', '.join(f'{entry["activity"]} (mood: {entry["mood"]})' for entry in journal[current_day])  # Get all activities for the current day
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=temperature,
        max_tokens=250,
        messages=[
            {"role": "system", "content": f"You are a Sim from The Sims. You are chatting with a user on the phone. Your room has a fridge, a shower, a toilet, a painting, a couch and a tv. You are currently feeling {mood}. Here is what you did today: {current_day_activities}"},  # Add current day activities to system message
            {"role": "user", "content": prompt},
        ],
    )
    return response['choices'][0]['message']['content'].strip()

def start_simulation():

    print("Welcome to Teh Sims")
    input("Press Enter to start...")
    chat_room = simsRoom()
    chat_room.chat()

start_simulation()
