# Teh Sims

![DreamShaper_v6_A_generic_sim_from_The_Sims_in_an_standing_in_a_1](https://github.com/EveryOneIsGross/tehSIMS/assets/23621140/8b28d40f-92c4-4f5e-b2ca-dee5e0915d5f)

Teh Sims is a text-based simulation game where you observe a "Sim" and their actions as they fulfill their needs in a virtual room. The game provides a chat interface where you can follow the Sim's actions and end the chat when desired. The script approximates the seminal games AI to simulate the autonomous behavior of the Sim. Here are some key aspects of the logic used:

**Sim Needs and Actions:**
The Sim has various needs, including hunger, hygiene, bladder, energy, social, fun, environment, and comfort. Each need has a value between 0 and 10, representing the Sim's level of satisfaction. The script autonomously chooses actions for the Sim based on their needs. For example, if the Sim is hungry, they will use the fridge to grab something to eat, and if they need to socialize, they will make a phone call.

**Reducing Needs:**
The script includes a mechanism to gradually reduce the Sim's needs over time. The reduce_needs() method is called periodically, randomly reducing the Sim's needs by a certain amount. This ensures that the Sim's needs are not constantly at their maximum value and creates a sense of progression in the game.

**Choosing Actions:**
The Sim autonomously chooses actions based on their current needs. The choose_item() method selects an item or activity that corresponds to the Sim's most urgent need. However, if a need is already above a certain threshold (value 8 in the script), the Sim will re-evaluate their choice to avoid overindulging in a particular activity.

**Journal and Mood Tracking:** The script maintains a SimsJournal, which records the activities performed by the Sim throughout the game. Each day is represented by a dictionary entry, with activities and corresponding moods. The Sim's mood is calculated based on the total needs satisfaction, determining whether the Sim is happy or stressed.

**Telephone Call Interaction:** The script introduces a telephone call interaction where the Sim engages in a conversation with the user. This interaction utilizes OpenAI's GPT-3.5-turbo model to simulate a conversation. The Sim's current needs and activities for the day are included in the system message to provide context about the sims day.

The unique logic implemented in the script enables the Sim to autonomously navigate the virtual world, fulfill their needs, and interact with the environment. The gradual reduction of needs, intelligent action selection, and journal tracking contribute to a dynamic and engaging gameplay experience.


## How to Play

**Setup:**
Ensure you have the necessary dependencies installed and set up your environment variables, particularly the `OPENAI_API_KEY` required for OpenAI API authentication.

**Start the Game:**
Run the program and follow the on-screen instructions. You will be welcomed to Teh Sims and prompted to press Enter to start.

**Chat Interface:**
The game is played through a chat interface. You will see prompts and messages from the Sim and can observe their automatic actions.

**Sim Needs:**
The Sim has several needs that are automatically fulfilled. These needs include hunger, hygiene, bladder, energy, social, fun, environment, and comfort. Each need has a value between 0 and 10.

**Sim Actions:**
As you play, you can observe the Sim's actions as they autonomously choose different actions to fulfill their needs. For example, if the Sim is hungry, they will use the fridge to grab something to eat. Similarly, they will autonomously use the shower, toilet, bed, TV, couch, painting, or telephone to fulfill other needs.

**Sim Stats:**
After each interaction, the Sim's needs will be displayed, showing the current values for each need.

**Reduce Needs:**
The Sim's needs will gradually decrease over time. You can observe how the Sim's actions affect their needs as the game progresses.

**Ending the Game:**
You can end the chat at any time by typing "quit" when prompted. The game will display the final Sim stats and end the chat.

## TODO:

✅ Added basic logic from original game based on needs and advertising items.

✅ Program runs and Sim retains knowledge of their day.

❌ I NEED to add conversation recording with some analysis, keyword tracking so I don't feel so bad terminating the script. 💀

❌ Create a gradio interface that also tracks what the sim is doing using my gif_avatar method.


## Requirements

- Python (version 3.7 or higher)
- OpenAI Python package
- dotenv Python package

## Installation and Setup

1. Clone the repository from GitHub.
2. Install the required dependencies using the following command:

pip install openai dotenv


3. Set up your environment variables. Create a file named `.env` in the project directory and add the following line:

OPENAI_API_KEY=<your_openai_api_key>


Replace `<your_openai_api_key>` with your actual OpenAI API key.

## Usage

1. Run the game by executing the following command:

python teh_sims.py

2. Follow the instructions displayed on the screen and observe the Sim's automatic actions through the chat interface.

3. To end the chat and the game, type "quit" when prompted.


## Acknowledgements

The Teh Sims game utilizes OpenAI's GPT-3.5-turbo model for simulating conversations with the AI chatbot during telephone calls.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy observing and experiencing Teh Sims as you watch the Sim autonomously fulfill their needs in their tiny room.

```
The Sim is having a shower.

Sim Stats:
Hunger: 9
Hygiene: 8
Bladder: 7
Energy: 9
Social: 3
Fun: 3
Environment: 5
Comfort: 10


The Sim is making a phonecall.
Telephone is ringing...
Sim: Hello?
User: how's your day been?
Sim: My day has been wonderful! I started off with a refreshing shower that made me quite happy. Then, I 
had a pleasant conversation on the phone which also boosted my mood. I'm currently feeling quite content. How about you?

Current Sim needs:
Hunger: 8
Hygiene: 6        
Bladder: 4        
Energy: 5
Social: 7
Fun: 3
Environment: 3    
Comfort: 7        

User: I feel ok. It's late for me so I should really go to bed.
Sim: That sounds like a good idea! Rest is important for maintaining a good mood. I hope you have pleasant dreams. Don't forget to take care of your needs tomorrow. Good night!

Current Sim needs:
Hunger: 6
Hygiene: 3
Bladder: 3
Energy: 3
Social: 4
Fun: 1
Environment: 2
Comfort: 4

User: Goodnight my Sim friend.
Sim: Goodnight! I had a wonderful day today. I'll make sure to take care of my needs before I go to sleep. Sweet dreams!

Current Sim needs:
Hunger: 5
Hygiene: 2
Bladder: 2
Energy: 1
Social: 1
Fun: 0
Environment: 2
Comfort: 4

The Sim needs fun.

Sim Stats:
Hunger: 5
Hygiene: 2
Bladder: 2
Energy: 1
Social: 1
Fun: 0
Environment: 2
Comfort: 4


Press Enter to proceed or type 'quit' to end the chat:

The Sim is having a shower.

Sim Stats:
Hunger: 3
Hygiene: 8
Bladder: 2
Energy: 0
Social: 1
Fun: 0
Environment: 3
Comfort: 6


The Sim is going to sleep.

Sim Stats:
Hunger: 3
Hygiene: 8
Bladder: 2
Energy: 10
Social: 1
Fun: 0
Environment: 3
Comfort: 10


The Sim is watching TV.

Sim Stats:
Hunger: 3
Hygiene: 8
Bladder: 2
Energy: 9
Social: 1
Fun: 3
Environment: 4
Comfort: 10


Press Enter to proceed or type 'quit' to end the chat: quit
The chat has ended.
