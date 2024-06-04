
# Restaurant Name Generator with GEMINI Pro

This project is a Streamlit application that generates restaurant names and menu items based on the selected cuisine type. The application leverages the Google Generative AI model `gemini-pro` via the LangChain library.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

To get started, you need to have Python installed on your system. Follow the steps below to set up the project:

1. Clone the repository:
    ```sh
    git clone [https://github.com/yourusername/restaurant-name-generator.git](https://github.com/athul-22/Restaurant-name-generator/)
    cd restaurant-name-generator
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your Google API Key. You can do this by setting an environment variable or entering it when prompted:
    ```sh
    export GOOGLE_API_KEY="your_google_api_key"
    ```

## Usage

Run the Streamlit app with the following command:
```sh
streamlit run main.py
