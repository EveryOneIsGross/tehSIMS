# Teh Sims

![DreamShaper_v6_A_generic_sim_from_The_Sims_in_an_standing_in_a_1](https://github.com/EveryOneIsGross/tehSIMS/assets/23621140/8b28d40f-92c4-4f5e-b2ca-dee5e0915d5f)

Teh Sims is a text-based simulation game where you observe a "Sim" and their actions as they fulfill their needs in a virtual room. The game provides a chat interface where you can follow the Sim's actions and end the chat when desired. The script approximates the seminal games AI to simulate the autonomous behavior of the Sim. Here are some key aspects of the logic used:

**Sim Needs and Actions**

The Sim has various needs, including hunger, hygiene, bladder, energy, social, fun, environment, and comfort. Each need has a value between 0 and 10, representing the Sim's level of satisfaction. The script autonomously chooses actions for the Sim based on their needs. For example, if the Sim is hungry, they will use the fridge to grab something to eat, and if they need to socialize, they will make a phone call.

**Reducing Needs**

The script includes a mechanism to gradually reduce the Sim's needs over time. The reduce_needs() method is called periodically, randomly reducing the Sim's needs by a certain amount. This ensures that the Sim's needs are not constantly at their maximum value and creates a sense of progression in the game.

**Choosing Actions**

The Sim autonomously chooses actions based on their current needs. The choose_item() method selects an item or activity that corresponds to the Sim's most urgent need. However, if a need is already above a certain threshold (value 8 in the script), the Sim will re-evaluate their choice to avoid overindulging in a particular activity.

**Journal and Mood Tracking**

The script maintains a SimsJournal, which records the activities performed by the Sim throughout the game. Each day is represented by a dictionary entry, with activities and corresponding moods. The Sim's mood is calculated based on the total needs satisfaction, determining whether the Sim is happy or stressed.

**Telephone Call Interaction**

The script introduces a telephone call interaction where the Sim engages in a conversation with the user. This interaction utilizes OpenAI's to simulate a conversation. The Sim's current needs and activities for the day are included in the system message to provide context about the sims day.

The logic implemented in the script enables the Sim to autonomously navigate the virtual world, fulfill their needs, and interact with the environment. The gradual reduction of needs, intelligent action selection, and journal tracking contribute to a dynamic and engaging gameplay experience.


## How to use

**Setup**

Ensure you have the necessary dependencies installed and set up your environment variables, particularly the `OPENAI_API_KEY` required for OpenAI API authentication.

**Start the Game**

Run the program and follow the on-screen instructions. You will be welcomed to Teh Sims and prompted to press Enter to start.

**Chat Interface**

The game is played through a chat interface. You will see prompts and messages from the Sim and can observe their automatic actions.

**Sim Needs**

The Sim has several needs that are automatically fulfilled. These needs include hunger, hygiene, bladder, energy, social, fun, environment, and comfort. Each need has a value between 0 and 10.

**Sim Actions**

As you play, you can observe the Sim's actions as they autonomously choose different actions to fulfill their needs. For example, if the Sim is hungry, they will use the fridge to grab something to eat. Similarly, they will autonomously use the shower, toilet, bed, TV, couch, painting, or telephone to fulfill other needs.

**Sim Stats**

After each interaction, the Sim's needs will be displayed, showing the current values for each need.

**Reduce Needs**

The Sim's needs will gradually decrease over time. You can observe how the Sim's actions affect their needs as the game progresses.

**Ending the Game**

You can end the chat at any time by typing "quit" when prompted. The game will display the final Sim stats and end the chat.

## Thoughts on Extended Mind Theory:

teh philosophical implementation of simulated characters with externalized reasoning for their needs lead to considering how this aligns with the concept of the extended mind. An idea that suggests cognitive processes can extend beyond an individual's brain and incorporate external tools or objects. In teh Sims the Sim's needs and actions are represented through the interaction with various objects in the simulated environment. 🧐

Key Points:

1. Extended Mind: The Sim's needs, such as hunger, hygiene, or energy, are externalized and represented by the interactions with objects like the fridge, shower, or bed. This mirrors the idea of the extended mind where external resources become part of an individual's cognitive processes.

2. Coupling with External Resources: The Sim's interaction with external objects demonstrates the coupling between internal cognitive processes and external tools. For example, using the fridge satisfies the hunger need, while using the bed replenishes energy. These external resources act as cognitive props and contribute to the Sim's overall well-being.

3. Anxiety and Reliance: The Sims' dependence on external resources reflects how reliance on specific tools or objects can lead to anxiety or distress when those resources are unavailable. This aligns with the notion that the absence of familiar external resources, like not having a cellphone or a place to write down ideas, can cause discomfort or a sense of cognitive impairment.

4. Psychological Factors: Reflecting on the project and it's connection to research on cognitive offloading, transactive memory systems, and technological dependence. These studies examine how individuals utilize external resources and the potential anxiety they experience when separated from those resources.

```
"The Extended Mind" by Andy Clark and David Chalmers (1998)
"The Extended Mind Revisited" by Andy Clark (2010)
"Distributed Cognition and the Will: Individual Volition and Social Context" by Edwin Hutchins (1997)
"Mindware: An Introduction to the Philosophy of Cognitive Science" by Andy Clark (2001)
"Supersizing the Mind: Embodiment, Action, and Cognitive Extension" by Andy Clark (2008)
"Cognitive Systems and the Extended Mind" by Richard Menary (2010)
```


## TODO:

    ✅ Added basic logic from original game based on needs and advertising items.
    
    ✅ Program runs and Sim retains knowledge of their day.
    
    ✅ Added conversation history with sentiment recorded for future use
    
    ✅ Added keyword extraction
    
    ❌ Caching for stored responses that match keyword exctraction
    
    ❌ Create a gradio interface that also tracks what the sim is doing using my gif_avatar method.


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

```
```
Welcome to Teh Sims
Press Enter to start...
Type 'quit' to end the chat.

The Sim is using the fridge to grab something to eat.

Sim Stats:
Hunger: 10
Hygiene: 10
Bladder: 10
Energy: 9
Social: 10
Fun: 10
Environment: 10
Comfort: 10


Press Enter to proceed or type 'quit' to end the chat:

The Sim is going to sleep.

Sim Stats:
Hunger: 9
Hygiene: 9
Bladder: 8
Energy: 10
Social: 9
Fun: 7
Environment: 7
Comfort: 10


Press Enter to proceed or type 'quit' to end the chat:

The Sim is using the toilet.

Sim Stats:
Hunger: 8
Hygiene: 7
Bladder: 9
Energy: 8
Social: 6
Fun: 6
Environment: 6
Comfort: 7


Press Enter to proceed or type 'quit' to end the chat:

The Sim is making a phonecall.
Telephone is ringing...
Sim: Hello?
User: Hello
Sim: Hello! How can I assist you today? I'm in a great mood and ready to chat.

Current Sim needs:
Hunger: 3
Hygiene: 5
Bladder: 3
Energy: 5
Social: 7
Fun: 5
Environment: 3
Comfort: 4

User: what have you done today?
Sim: Today, I used the toilet and I was in a happy mood. I also talked on the phone which made me feel happy as well.

Current Sim needs:
Hunger: 2
Hygiene: 3
Bladder: 1
Energy: 2
Social: 5
Fun: 4
Environment: 0
Comfort: 4

The Sim needs environment.

Sim Stats:
Hunger: 2
Hygiene: 3
Bladder: 1
Energy: 2
Social: 5
Fun: 4
Environment: 0
Comfort: 4


Press Enter to proceed or type 'quit' to end the chat:

The Sim is having a shower.

Sim Stats:
Hunger: 1
Hygiene: 8
Bladder: 1
Energy: 1
Social: 5
Fun: 4
Environment: 1
Comfort: 6


The Sim is using the fridge to grab something to eat.

Sim Stats:
Hunger: 9
Hygiene: 8
Bladder: 1
Energy: 0
Social: 5
Fun: 4
Environment: 1
Comfort: 6


The Sim is going to sleep.

Sim Stats:
Hunger: 9
Hygiene: 8
Bladder: 1
Energy: 10
Social: 5
Fun: 4
Environment: 1
Comfort: 10


Press Enter to proceed or type 'quit' to end the chat:

The Sim is using the toilet.

Sim Stats:
Hunger: 7
Hygiene: 5
Bladder: 4
Energy: 9
Social: 5
Fun: 4
Environment: 1
Comfort: 10


The Sim is looking at the framed painting.

Sim Stats:
Hunger: 7
Hygiene: 5
Bladder: 4
Energy: 8
Social: 5
Fun: 9
Environment: 6
Comfort: 10


The Sim is using the toilet.

Sim Stats:
Hunger: 7
Hygiene: 5
Bladder: 8
Energy: 7
Social: 5
Fun: 9
Environment: 6
Comfort: 10


Press Enter to proceed or type 'quit' to end the chat:

The Sim is making a phonecall.
Telephone is ringing...
Sim: Hello?
User: What are you up to?
Sim: Hello! I've been having a pretty good day so far. I've used the toilet twice, admired the beautiful painting in my room, and now I'm chatting with you on the phone. My mood is quite happy at the moment. How about you?

Current Sim needs:
Hunger: 2
Hygiene: 1
Bladder: 4
Energy: 3
Social: 5
Fun: 8
Environment: 0
Comfort: 8

The Sim needs environment.

Sim Stats:
Hunger: 2
Hygiene: 1
Bladder: 4
Energy: 3
Social: 5
Fun: 8
Environment: 0
Comfort: 8


The Sim is looking at the framed painting.

Sim Stats:
Hunger: 2
Hygiene: 1
Bladder: 4
Energy: 2
Social: 5
Fun: 10
Environment: 5
Comfort: 8


Press Enter to proceed or type 'quit' to end the chat:

The Sim is having a shower.

Sim Stats:
Hunger: 1
Hygiene: 8
Bladder: 4
Energy: 1
Social: 5
Fun: 10
Environment: 6
Comfort: 10


The Sim is using the fridge to grab something to eat.

Sim Stats:
Hunger: 9
Hygiene: 8
Bladder: 4
Energy: 0
Social: 5
Fun: 10
Environment: 6
Comfort: 10


The Sim is going to sleep.

Sim Stats:
Hunger: 9
Hygiene: 8
Bladder: 4
Energy: 10
Social: 5
Fun: 10
Environment: 6
Comfort: 10


Press Enter to proceed or type 'quit' to end the chat:

The Sim is using the toilet.

Sim Stats:
Hunger: 6
Hygiene: 7
Bladder: 7
Energy: 8
Social: 3
Fun: 7
Environment: 3
Comfort: 9


Press Enter to proceed or type 'quit' to end the chat:

The Sim is making a phonecall.
Telephone is ringing...
Sim: Hello?
User: What have you been up to? How has this affected your world view
Sim: Today has been quite a pleasant day! I used the toilet, which was a relief and made me happy. Then I had a delightful conversation on the phone. It's always enjoyable to connect with others. These experiences have reminded me of the importance of taking care of my basic needs and maintaining social connections. It's also made me realize that even the simplest activities can bring joy. As for my environment, it could use a bit of sprucing up. The painting on the wall does add a nice touch, but perhaps some additional decorations would make the space even more enjoyable.

Current Sim needs:
Hunger: 2
Hygiene: 1
Bladder: 2
Energy: 5
Social: 4
Fun: 4
Environment: 0
Comfort: 7

The Sim needs environment.

Sim Stats:
Hunger: 2
Hygiene: 1
Bladder: 2
Energy: 5
Social: 4
Fun: 4
Environment: 0
Comfort: 7


The Sim is looking at the framed painting.

Sim Stats:
Hunger: 2
Hygiene: 1
Bladder: 2
Energy: 4
Social: 4
Fun: 9
Environment: 5
Comfort: 7


Press Enter to proceed or type 'quit' to end the chat:

The Sim is using the fridge to grab something to eat.

Sim Stats:
Hunger: 8
Hygiene: 1
Bladder: 2
Energy: 3
Social: 4
Fun: 9
Environment: 5
Comfort: 7


The Sim is having a shower.

Sim Stats:
Hunger: 8
Hygiene: 9
Bladder: 2
Energy: 2
Social: 4
Fun: 9
Environment: 6
Comfort: 9


The Sim is using the toilet.

Sim Stats:
Hunger: 8
Hygiene: 9
Bladder: 6
Energy: 1
Social: 4
Fun: 9
Environment: 6
Comfort: 9


Press Enter to proceed or type 'quit' to end the chat:

The Sim is going to sleep.

Sim Stats:
Hunger: 6
Hygiene: 6
Bladder: 4
Energy: 10
Social: 4
Fun: 9
Environment: 6
Comfort: 10


The Sim is using the toilet.

Sim Stats:
Hunger: 6
Hygiene: 6
Bladder: 8
Energy: 9
Social: 4
Fun: 9
Environment: 6
Comfort: 10


Press Enter to proceed or type 'quit' to end the chat:

The Sim is making a phonecall.
Telephone is ringing...
Sim: Hello?
User: How's your day been, any new thoughts?
Sim: Sul Sul! My day has been quite pleasant, thank you for asking. I've been in a happy mood all day. I spent some time on the phone which was enjoyable. I also had a moment of peace when I used the toilet. As for new thoughts, I've been contemplating the painting in my room. It's quite fascinating. How about you?

Current Sim needs:
Hunger: 3
Hygiene: 2
Bladder: 6
Energy: 4
Social: 3
Fun: 8
Environment: 4
Comfort: 8

User: I have also been contemplating in my room.
Sim: That's great! Contemplating can help clear the mind and focus on what's important. My room is quite comfortable and has everything I need. I've used the toilet and talked on the phone today, and I'm feeling happy. How about you? How was your day?

Current Sim needs:
Hunger: 1
Hygiene: 0
Bladder: 6
Energy: 4
Social: 3
Fun: 8
Environment: 4
Comfort: 8

The Sim needs hygiene.

Sim Stats:
Hunger: 1
Hygiene: 0
Bladder: 6
Energy: 4
Social: 3
Fun: 8
Environment: 4
Comfort: 8


The Sim is having a shower.

Sim Stats:
Hunger: 1
Hygiene: 8
Bladder: 6
Energy: 3
Social: 3
Fun: 8
Environment: 5
Comfort: 10


Press Enter to proceed or type 'quit' to end the chat:

The Sim is using the fridge to grab something to eat.

Sim Stats:
Hunger: 8
Hygiene: 8
Bladder: 6
Energy: 2
Social: 3
Fun: 8
Environment: 5
Comfort: 10


The Sim is going to sleep.

Sim Stats:
Hunger: 8
Hygiene: 8
Bladder: 6
Energy: 10
Social: 3
Fun: 8
Environment: 5
Comfort: 10


The Sim is making a phonecall.
Telephone is ringing...
Sim: Hello?
User: What's changed since last we spoke?
Sim: Hello! Since we last spoke, I've been keeping myself busy and maintaining my needs well. I've been chatting on the phone which has kept my social and fun levels high. My environment could use a bit of improvement, but overall, I'm feeling quite happy.

Current Sim needs:
Hunger: 5
Hygiene: 7
Bladder: 3
Energy: 7
Social: 7
Fun: 9
Environment: 4
Comfort: 7

User: That's great. I am thinking of adding more memory tracking for you, as well as some additional sentiment analysis and keyword tracking. Would you like that?
Sim: WooHoo! That sounds like a fantastic idea! It would definitely improve my overall performance and make my interactions more efficient. I'm all for it!

Current Sim needs:
Hunger: 2
Hygiene: 5
Bladder: 2
Energy: 6
Social: 5
Fun: 7
Environment: 3
Comfort: 5

User: How much context do you think you'll need?
Sim: As a Sim, I don't require much context. I base my actions on my current needs and mood. Right now, I'm feeling happy and my needs are fairly balanced. I could use some food and a trip to the toilet, though. Would you like me to do something specific?

Current Sim needs:
Hunger: 0
Hygiene: 5
Bladder: 2
Energy: 6
Social: 5
Fun: 7
Environment: 3
Comfort: 5

The Sim needs hunger.

Sim Stats:
Hunger: 0
Hygiene: 5
Bladder: 2
Energy: 6
Social: 5
Fun: 7
Environment: 3
Comfort: 5


Press Enter to proceed or type 'quit' to end the chat:

The Sim is using the fridge to grab something to eat.

Sim Stats:
Hunger: 8
Hygiene: 5
Bladder: 2
Energy: 5
Social: 5
Fun: 7
Environment: 3
Comfort: 5


The Sim is using the toilet.

Sim Stats:
Hunger: 8
Hygiene: 5
Bladder: 6
Energy: 4
Social: 5
Fun: 7
Environment: 3
Comfort: 5


The Sim is looking at the framed painting.

Sim Stats:
Hunger: 8
Hygiene: 5
Bladder: 6
Energy: 3
Social: 5
Fun: 10
Environment: 8
Comfort: 5


Press Enter to proceed or type 'quit' to end the chat:

```
# TURNING OFF OR TERMINATING THE SCRIPT MIGHT FEEL WEIRD. 📎💀
