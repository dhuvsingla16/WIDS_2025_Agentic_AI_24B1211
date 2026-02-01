from agents.scraper_agent import scrape_page, save_raw_text
from agents.chunking_agent import chunk_text
from agents.embedding_agent import create_vector_store
from agents.query_agent import retrieve_context
from agents.response_agent import generate_response

# 1. SCRAPE
url = "https://www.ee.iitb.ac.in/web/academics/"
raw_text = scrape_page(url)
save_raw_text(raw_text, "academics.txt")

# 2. CHUNK
chunks = chunk_text(raw_text)

# 3. EMBED + STORE
create_vector_store(chunks)

# 4. QUERY
query = "What courses are offered in the department?"
context = retrieve_context(query)

# 5. RESPONSE
response_prompt = generate_response(query, context)
print(response_prompt)
