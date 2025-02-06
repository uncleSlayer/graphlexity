    # @tool("scrape_tool", args_schema=CustomScrapeToolSchema)
    # def scrape_tool(scraping_information: CustomScrapeToolSchema) -> list[dict]:
    #     """
    #     this tool uses the openai gpt-4 model to scrape the given urls and extract the most relevant information.

    #     args: a list of information to scrape from.

    #     returns:
    #         a list of scraped information.
    #     """

    #     from textwrap import dedent
    #     from crawl4ai.extraction_strategy import llmextractionstrategy
    #     from crawl4ai import crawlerrunconfig, cachemode, asyncwebcrawler

    #     class search_result_schema(BaseModel):
    #         title: str
    #         link: str
    #         content: str

    #     try:

    #         scraped_information = []

    #         for info in scraping_information.scraping_information:

    #             url = info.url
    #             title = info.title

    #             llm_strategy = llmextractionstrategy(
    #                 provider="openai/gpt-4o-mini",
    #                 api_token=ENV_SETTINGS.OPENAI_API_KEY,
    #                 schema=search_result_schema,
    #                 extraction_type="schema",
    #                 instruction=dedent(
    #                     f"""
    #                     you are a scraper. get the most relevant information from the given url. always return a concise answer.
    #                 """
    #                 ),
    #                 chunk_token_threshold=1000,
    #                 overlap_rate=0.5,
    #                 apply_chunking=True,
    #                 input_format="markdown",
    #                 extra_args={"temperature": 0.5, "max_tokens": 500},
    #             )

    #             crawl_config = crawlerrunconfig(
    #                 extraction_strategy=llm_strategy,
    #                 cache_mode=cachemode.bypass,
    #             )

    #             with asyncwebcrawler(config=crawl_config) as crawler:

    #                 crawl_result = asyncio.run(crawler.arun(
    #                     url,
    #                     config=crawl_config,
    #                 ))

    #                 if crawl_result.success:

    #                     scraped_data = json.loads(crawl_result.extracted_content)

    #                     scraped_information.append(
    #                         {
    #                             "title": title,
    #                             "link": url,
    #                             "content": scraped_data,
    #                         }
    #                     )

    #                     print("the scraped information is: ", scraped_data)

    #                     print(f"used tokens: {llm_strategy.show_usage()}")

    #                 else:
    #                     print(
    #                         f"error while scraping {url}: {crawl_result.error_message}"
    #                     )

    #         return scraped_information

    #     except Exception as e:
    #         print(e)

    #         return "Error while scraping"
