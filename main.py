from agents import Agent, Runner
from pydantic import BaseModel
import asyncio

# Define lyric poetry agent
lyrical_poetry_agent = Agent(
    name="Lyric Poetry Agent",
    instructions="You are the best lyrical agent. You have to analyze lyrical poetry and explain its emotional content.",
    handoff_description="This agent can provide a description of lyrical poetry."
)

# Define narrative poetry agent
narrative_poetry_agent = Agent(
    name="Narrative Poetry Agent",
    instructions="You are the best narrative agent. You have to analyze narrative poetry and explain the story.",
    handoff_description="This agent can provide a description of narrative poetry."
)

# Define dramatic poetry agent
dramatic_poetry_agent = Agent(
    name="Dramatic Poetry Agent",
    instructions="You are the best dramatic agent. You have to analyze dramatic poetry and explain the character's emotions.",
    handoff_description="This agent can provide a description of dramatic poetry."
)

# Define parent triage agent
parent_agent = Agent(
    name="Parent Agent",
    instructions=(
        "You are the parent agent. The user will give a poem. "
        "Your job is to classify whether it is Lyric, Narrative, or Dramatic poetry, "
        "and then hand off the task to the appropriate agent."
    ),
    handoffs=[lyrical_poetry_agent, narrative_poetry_agent, dramatic_poetry_agent]
)

# Ask a question and route it through the correct agent
async def ask_question(poem: str):
    print(f"\n📝 User's Poem:\n{poem}")
    result = await Runner.run(parent_agent, poem)

    agent = result.last_agent
    agent_name = agent.name if agent else "Unknown"

    print(f"\n🤖 Handoff To: {agent_name}")
    print(f"\n📜 Explanation:\n{result.final_output}\n")

# Main method to run
async def main():
    poem_input = """
    My heart is like a singing bird  
    Whose nest is in a watered shoot;  
    My heart is like an apple-tree  
    Whose boughs are bent with thick-set fruit;  
    """
    await ask_question(poem_input)

# Run the program
if __name__ == "__main__":
    asyncio.run(main())
