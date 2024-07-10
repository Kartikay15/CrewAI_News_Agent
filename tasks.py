from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

research_task = Task(
    description = (
        "Identify the next big trend in {topic}"
        "Focus on identifying pros and cons and the overall narrative"
        "Your final report should clearly articulate the key points"
        "its market opportunities, and potential risks"
    ),
    expected_output = 'A comprehensive long report on latest trends',
    tools = [tool],
    agent = news_researcher,
)

write_task = Task(
    description = (
        "Compose a insightful article on {topic}"
        "Focus on latest trends and how it's impacting industries."
        "This article should be easy to understand , engaging, and positive"
    ),
    expected_output = 'A 10 paragraph article on {topic} formatted as markdown',
    tools = [tool],
    agent = news_writer,
    async_execution = False,
    output_file = 'new-blog-post.md'
)