import getpass
import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from follow_up_handler import handle_follow_up
from langchain_tavily import TavilySearch

load_dotenv()
api_key = os.environ.get("TAVILY_API_KEY")
if api_key is None:
    api_key = getpass.getpass("Enter your Tavily API: ")


tool = TavilySearch(
    max_results=5,
    topic="general",
)


# tool.invoke({"query": "What happened at the last wimbledon"})
def get_tavily_response():
    query = input("Enter a topic that you want to search:")
    response = tool.invoke({"query": query})
    return response
# print(f"tavily Response: {response}")

tavily_response = get_tavily_response()

print("Successfully retrieved Tavily response.")
while True:
    print("\nOptions:")
    print("1. Ask Follow-up question")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        follow_up = input("Enter your follow-up question: ")
        answer = handle_follow_up(tavily_response, follow_up)
        print(f"Answer: {answer}")
    elif choice == '2':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ")
