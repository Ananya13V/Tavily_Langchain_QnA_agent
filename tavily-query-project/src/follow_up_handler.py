import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Together
import warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()


def handle_follow_up(response, follow_up_question):
    together_api_key = os.getenv("TOGETHER_API_KEY")
    if not together_api_key:
        raise ValueError("TOGETHER_API_KEY is not set in the environment variables.")

    # Initialize the Together LLM
    llm = Together(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=0.7,
        max_tokens=512,
        together_api_key=together_api_key,
    )

    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are an assistant. Use the following context to answer the question in a chatbot-like format. "
            "Provide the answer and include relevant links for reference.\n\n"
            "Context: {context}\n\n"
            "Question: {question}\n\n"
            "Answer (include links for reference):"
        ),
    )

    # Create an LLM chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain with the response and follow-up question
    answer = chain.run({"context": response, "question": follow_up_question})

    return answer


# if __name__ == "__main__":
#     # Example usage
#     tavily_response = "The last Wimbledon was won by Novak Djokovic."
#     follow_up = "How many times has he won Wimbledon?"
#     print(handle_follow_up(tavily_response, follow_up))
