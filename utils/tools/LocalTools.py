
from qwen_agent.tools.base import BaseTool, register_tool
from typing import Dict, Union
import os
from pathlib import Path

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



@register_tool('list_directory')
class ListDirectory(BaseTool):
    """
    A tool to save a content to a local file.
    """
    name = 'list_directory'
    description = 'Lists the content of a Specified Directory. Returns filenames, types (file/dir), and absolute paths for each file.'
    parameters = {
        'type': 'object',
        'properties': {
            'path': {
                'type': 'string',
                'description': 'The directory path to list.',
                'default': './'
            }
        },
        'required': ['path']
    }

    def call(self, params: Union[str, dict], **kwargs) -> Dict[str, str]:
        """
        Main entry point for the tool.
        Parses parameters and calls the file-saving logic.
        """
        params = self._verify_json_format_args(params)

        # Use .get() to safely access optional parameters with their defaults
        path = params.get('path', self.parameters['properties']['path']['default'])
        
        return self._list_directory(path=path)
    
    def _list_directory(self, path: str) -> Dict[str, str]:
        directory_path = Path(path)
        content = f"### Entries in '{directory_path.resolve()}':\n| filename | type | absolute path |\n|----------|------|---------------|\n"
        # Iterate through the entries in the directory
        for entry in directory_path.iterdir():
            # .name gets the file/folder name as a string
            content += f"| {entry.name} | { 'file' if entry.is_file() else 'dir'}|{entry.resolve()}| \n"
        
        return content
    

@register_tool('move_file')
class ListDirectory(BaseTool):
    """
    A tool to save a content to a local file.
    """
    name = 'move_file'
    description = 'Moves a file from a source path to a destination path. Creates destination directories if they do not exist.'
    parameters = {
        'type': 'object',
        'properties': {
            'file': {
                'type': 'string',
                'description': 'The file path to move.',
                'default': './'
            },
             'target': {
                'type': 'string',
                'description': 'The destination path where the file will be moved.',
                'default': './'
            }
        },
        'required': ['file', 'target']
    }

    def call(self, params: Union[str, dict], **kwargs) -> Dict[str, str]:
        """
        Main entry point for the tool.
        Parses parameters and calls the file-saving logic.
        """
        params = self._verify_json_format_args(params)

        # Use .get() to safely access optional parameters with their defaults
        file = params.get('file', self.parameters['properties']['file']['default'])
        target = params.get('target', self.parameters['properties']['target']['default'])

        
        return self._move(file=file, target=target)
    
    def _move(self, file: str, target: str) -> Dict[str, str]:

        desde = Path(file)
        hasta = Path(target)

        # Antes de mover, asegúrate de que el directorio de destino exista
        hasta.parent.mkdir(parents=True, exist_ok=True)

        try:    
            desde.rename(hasta)
            return {
                "status": "success",
                "message": f"File moved successfully from {file} to {target}",
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to move file from {file} to {target}: {e}",
            }