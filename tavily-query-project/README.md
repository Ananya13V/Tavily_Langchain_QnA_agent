# Tavily Query Project

This project utilizes the Tavily API to process queries and handle follow-up questions using Langchain. It is structured to allow easy integration and expansion of functionalities.

## Project Structure

```
tavily-query-project
├── src
│   ├── app.py                # Main application file for processing queries with Tavily
│   ├── follow_up_handler.py   # Handles follow-up questions using Langchain
│   └── utils
│       └── __init__.py       # Utility functions and classes
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd tavily-query-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory and add your Tavily API key:
     ```
     TAVILY_API_KEY=your_api_key_here
     ```

## Usage

1. To process a query using the Tavily API, run the `app.py` file:
   ```
   python src/app.py
   ```

2. To handle follow-up questions based on the initial response, you can use the `follow_up_handler.py` file. Import the necessary functions and pass the initial response as context.

## Contributing

Feel free to submit issues or pull requests for enhancements or bug fixes. 

## License

This project is licensed under the MIT License.