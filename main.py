from qwen_agent.agents import Assistant
from qwen_agent.utils.output_beautify import typewriter_print
import os
import utils.tools
import dotenv
from utils.system import SYSTEM_PROMPT as system_instruction

# Assuming BaseTool and register_tool are defined elsewhere, as in the original context.
# from some_module import BaseTool, register_tool

# Step 2: Configure the LLM you are using.

dashcope_model = {
    "model":'qwen3-235b-a22b-thinking-2507',
    "model_server": 'https://dashscope-intl.aliyuncs.com/compatible-mode/v1',
    'api_key': os.getenv('DASHSCOPE_API_KEY')
}

lm_studio_local = {
    'model':'qwen/qwen3-14b', #'qwen/qwen3-4b-thinking-2507',
    'model_server': 'http://192.168.5.108:1234/v1/',#, # 'http://127.0.0.1:1234/v1/',
}

# Step 3: Create an agent. Here we use the `Assistant` agent as an example, which is capable of using tools and reading files.
print(system_instruction)



tools = [
    'my_image_gen', 
    'code_interpreter', 
    'web_content_extractor', 
    'google_search', 
    'doc_parser',  
    'file_saver'
    ]  

bot = Assistant(llm=dashcope_model,
                system_message=system_instruction,
                function_list=tools,
                )

from qwen_agent.gui import WebUI
WebUI(bot).run()  # bot is the agent defined in the above code, we do not repeat the definition here for saving space.


"""
# Step 4: Run the agent as a chatbot.
messages = []  # This stores the chat history.
while True:
    # For example, enter the query "draw a dog and rotate it 90 degrees".
    query = input('\nuser query: ')
    # Append the user query to the chat history.
    messages.append({'role': 'user', 'content': query})
    response = []
    response_plain_text = ''
    print('bot response:')
    for response in bot.run(messages=messages):
        # Streaming output.
        response_plain_text = typewriter_print(response, response_plain_text)
    # Append the bot responses to the chat history.
    messages.extend(response)

"""
