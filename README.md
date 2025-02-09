## Graphlexity is an ai internet search engine.
It uses google serper to search internet and scrapes the top link(s) using crawl4ai.

## Used technologies
- Crew ai for creating agents, tasks
- Langchain to create custom tools and general llm calls
- Google serper langchain tool to search internet. Which is also used as citations.

###### My initial idea was to scrape the web page in markdown format and pass the content to llm and get a summary, to make the citations as accurate as possible but because the scraped content is a lot and it consumes lots of openai credit, I'm not adding this feature.
###### The google serper web page snippet is passed to the llm for now.
