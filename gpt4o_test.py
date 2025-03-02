import openai
from env import API_KEY
client = openai.OpenAI(api_key=API_KEY)

# Make the API request
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system", 
      "content": ("You are a driving assistant trained to generate detailed action plans for vehicles in the CARLA simulator. "
                  "You will interpret a given situation based on the state of the front vehicle and the environment and generate specific "
                  "actions as a human agent would in that scenario.")
    },
    {
      "role": "user",
      "content": ("Given the image from the CARLA simulator and the following description of the front car: The front car is "
                  "driving steadily and appears to be keeping within its lane. No erratic behavior is observed, making it safe for "
                  "overtaking. As a human agent, I would signal to overtake the car, ensure it's safe to maneuver, and then "
                  "proceed to overtake.\n\nPlease generate a structured action plan including the following:\n- Throttle: "
                  "Increase\n- Steer: Slight left\n- Brake: None\n- Reverse: None\n- Hand brake: None\n- Manual: None\n- "
                  "Gear: Shift up to 3 or more if necessary")
    },
    {
      "role": "user", 
      "content": "Here is an image from the CARLA simulator:\n![Carla Simulator Image](https://github.com/DanielHfnr/Carla-Object-Detection-Dataset/blob/master/images/train/Town02_004680.png?raw=true)"
    }
  ]
  # image={
  #   "url": "https://github.com/DanielHfnr/Carla-Object-Detection-Dataset/blob/master/images/train/Town02_004680.png?raw=true"
  # }
)

# Print the response
# print(response.choices[0])
message_content = response.choices[0].message.content
print(message_content)