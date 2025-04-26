# Tavily Query Project

This project utilizes the Tavily API to process queries and handle follow-up questions using Langchain, which uses TogetherAI's API key. It has a Menu that allows a user to ask follow-up questions on a topic that has been scraped using Tavily's web-scraper
## Project Structure

```
tavily-query-project
├── src
│   ├── follow_up_handler.py   # Handles follow-up questions using Langchain-Together AI
│   └── response.py            # Tavily search responses generated here
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
   - Create a `.env` file in the root directory and add your Tavily and Together API keys:
     ```
     TAVILY_API_KEY=your_api_key_here
     ```

## Usage

1. To process a query using the Tavily API, run the `response.py` file:
   ```
   python src/response.py
   ```
It will automatically handle follow-up questions for you too.

## Contributing

Feel free to submit issues or pull requests for enhancements or bug fixes. 

## License

This project is licensed under the MIT License.