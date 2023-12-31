# GPTEngineModel Class Documentation

The `GPTEngineModel` class is designed to interact with the OpenAI GPT-3.5 Turbo engine using prompts from a .doc file. It provides a convenient way to generate responses based on tasks and input prompts.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Class Details](#class-details)
   - [Attributes](#attributes)
   - [Methods](#methods)
4. [Example](#example)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

Before using the `GPTEngineModel` class, make sure you have the required dependencies installed:

```bash
pip install openai
pip install python-docx
```

## Usage

To use the `GPTEngineModel` class, follow these steps:

1. Create a configuration file containing your OpenAI API key. Refer to the `config.py` file in the code for an example.

2. Import the `GPTEngineModel` class:

```python
from your_module import GPTEngineModel
```

3. Initialize an instance of the GPTEngineModel class with your main task and input prompt:
```python
engine = GPTEngineModel("Main task description", "Input prompt text")
```
4. Use the generate_response method to generate responses based on a .doc file:
```python
response = engine.generate_response("path/to/your/file.docx")
print(response)
```

## Class Details

### Attributes

- `main_task` (str): The main task description.
- `input_prompt` (str): The input prompt for the GPT-3.5 Turbo engine.
- `api_key` (str): The OpenAI API key for authentication.

### Methods

#### `generate_response(file_path: str) -> str`

Generate a response from OpenAI based on the provided .doc file.

- **Parameters**:
  - `file_path` (str): The path to the .doc file.

- **Returns**:
  - `str`: The response from OpenAI.

### Private Methods

- `_setup_openai()`: Set up the OpenAI API key for authentication.
- `_get_context() -> str`: Get the context for the current task.
- `_get_file(file_path: str) -> str`: Read the .doc file and return the text content.
- `_batch_process(file_path: str) -> List[dict]`: Batch process the instructions and input prompt.

## Example

```python
from your_module import GPTEngineModel

# Initialize the GPTEngineModel
engine = GPTEngineModel("Summarize an article", "Please summarize the following article:")

# Generate a response from OpenAI based on a .doc file
response = engine.generate_response("path/to/your/article.docx")
print(response)
```

## Contributing

If you would like to contribute to this project or report issues, please refer to the project's GitHub repository https://github.com/mbsuraj/gptEngine.git.

## License
This project is licensed under the MIT. See the LICENSE.md file for details.