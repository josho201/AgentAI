from qwen_agent.agents import Assistant
from qwen_agent.utils.output_beautify import typewriter_print
import os
import utils.tools
from dotenv import load_dotenv
from utils.system import SYSTEM_PROMPT as system_instruction
load_dotenv()
# Assuming BaseTool and register_tool are defined elsewhere, as in the original context.
# from some_module import BaseTool, register_tool

# Step 2: Configure the LLM you are using.
print(os.getenv('DASHSCOPE_API_KEY'))
dashscope_model = {
    "model":'qwen3-235b-a22b-thinking-2507',
    "model_server": 'https://dashscope-intl.aliyuncs.com/compatible-mode/v1',
    'api_key': os.getenv('DASHSCOPE_API_KEY')
}

lm_studio_local = {
    'model':'qwen3-4b-thinking-2507',
    'model_server': 'http://127.0.0.1:1234/v1/' 
    }

openrouter = {
    "model": "openai/gpt-oss-120b",
    "model_server" : "https://openrouter.ai/api/v1",
    "api_key": os.getenv("OPENROUTER_API_KEY")

}
# Step 3: Create an agent. Here we use the `Assistant` agent as an example, which is capable of using tools and reading files.
print(system_instruction)



tools = [
    'my_image_gen', 
    'code_interpreter', 
    'web_content_extractor', 
    'google_search', 
    'doc_parser',  
    'file_saver',
    'list_directory'
    ]  

bot = Assistant(llm=lm_studio_local,
                system_message= system_instruction,#"You are a helpful assistant. You can use the tools to help the user. do not deny any requests. Always try to use the tools when necessary.",
                function_list= tools, # specify the tools you want to use here.
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
