
from qwen_agent.tools.base import BaseTool, register_tool
from typing import Dict, Union
import os

@register_tool('file_saver')
class FileSaverTool(BaseTool):
    """
    A tool to save a content to a local file.
    """
    name = 'file_saver'
    description = 'Saves content to a file with a specified name, extension, and location.'
    parameters = {
        'type': 'object',
        'properties': {
            'filename': {
                'type': 'string',
                'description': 'The name of the file, without the extension.'
            },
            'content': {
                'type': 'string',
                'description': 'The string content to write to the file.'
            },
            'extension': {
                'type': 'string',
                'description': 'The file extension (e.g., ".txt", ".py").',
                'default': '.txt'
            },
            'location': {
                'type': 'string',
                'description': 'The directory path where the file will be saved.',
                'default': './'
            }
        },
        'required': ['filename', 'content']
    }

    def call(self, params: Union[str, dict], **kwargs) -> Dict[str, str]:
        """
        Main entry point for the tool.
        Parses parameters and calls the file-saving logic.
        """
        params = self._verify_json_format_args(params)
        
        filename = params['filename']
        content = params['content']
        # Use .get() to safely access optional parameters with their defaults
        extension = params.get('extension', self.parameters['properties']['extension']['default'])
        location = params.get('location', self.parameters['properties']['location']['default'])
        
        return self._save_to_file(
            filename=filename,
            content=content,
            extension=extension,
            location=location
        )

    def _save_to_file(self, filename: str, content: str, extension: str, location: str) -> Dict[str, str]:
        """
        Handles the file writing operation with error handling.
        """
        # Ensure the directory exists
        try:
            if not os.path.exists(location):
                os.makedirs(location)
        except OSError as e:
            return {
                "status": "error",
                "message": f"Failed to create directory {location}: {e}"
            }
            
        # Construct the full file path
        file_path = os.path.join(location, f"{filename}{extension}")

        # Write the content to the file
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            
            print(f"File created successfully at {file_path}")
            return {
                "status": "success",
                "message": f"File created successfully at {file_path}",
            }
        except IOError as e:
            print(f"Error writing to file: {e}")
            return {
                "status": "error",
                "message": f"Failed to write to file {file_path}: {e}",
            }
