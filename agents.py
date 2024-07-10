from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

## call the gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))

news_researcher = Agent(
    role = 'Senior Researcher',
    goal = 'Uncover advancements in {topic}',
    verbose = True,
    memory = True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation , eager to explore and share knowledge that could"
        "change the world"
    ),
    tools=[tool],
    llm = llm,
    allow_tools = True,
    allow_delegation = True
)

# Creating a write agent with custom tools responsible for writing news blog

news_writer = Agent(
    role = 'Senior Researcher',
    goal = 'Narrate compelling stories about {topic}',
    verbose = True,
    memory = True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaing narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm = llm,
    allow_tools = True,
    allow_delegation = False
)

