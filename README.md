# Teh Sims

Teh Sims is a text-based simulation game where you observe a Sim character and their automatic actions as they fulfill their needs in a virtual world. The game provides a chat interface where you can follow the Sim's actions and end the chat when desired.

## Philosophical Implications

The automatic nature of Teh Sims raises interesting philosophical implications. It prompts reflection on the nature of agency and simulation. Observing the Sim's autonomous behavior can spark discussions on determinism, free will, and the boundaries of simulation in creating believable virtual experiences.

## Novel Use Cases

Beyond gaming, this type of chatbot interaction can be applied to various novel use cases. Some potential applications include:

- Virtual Pet Companions: Creating virtual pets with autonomous behavior and needs, providing users with a sense of companionship and responsibility.
- Educational Simulations: Designing interactive simulations where users can observe and learn from autonomous virtual characters in various educational settings.
- Therapeutic Tools: Utilizing autonomous virtual characters in therapeutic contexts, such as mental health support or cognitive-behavioral therapy.

The possibilities for novel use cases are vast, and this type of chatbot interaction opens up new avenues for exploration and innovation.

![DreamShaper_v6_A_generic_sim_from_The_Sims_in_an_standing_in_a_1](https://github.com/EveryOneIsGross/tehSIMS/assets/23621140/8b28d40f-92c4-4f5e-b2ca-dee5e0915d5f)

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

## Requirements

- Python (version 3.7 or higher)
- OpenAI Python package
- dotenv Python package

## Installation and Setup

1. Clone the repository from GitHub.
2. Install the required dependencies using the following command:

pip install openai dotenv

sql
Copy code

3. Set up your environment variables. Create a file named `.env` in the project directory and add the following line:

OPENAI_API_KEY=<your_openai_api_key>

csharp
Copy code

Replace `<your_openai_api_key>` with your actual OpenAI API key.

## Usage

1. Run the game by executing the following command:

python teh_sims.py

vbnet
Copy code

2. Follow the instructions displayed on the screen and observe the Sim's automatic actions through the chat interface.

3. To end the chat and the game, type "quit" when prompted.


## Acknowledgements

The Teh Sims game utilizes OpenAI's GPT-3.5-turbo model for simulating conversations with the AI chatbot during telephone calls.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy observing and experiencing Teh Sims as you watch the Sim autonomously fulfill their needs in the virtual world!
