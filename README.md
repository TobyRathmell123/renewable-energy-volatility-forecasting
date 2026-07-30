# RAG-Project

RAG is Retrieval Augmented Generation, this is different to LLMs as LLMs can only respond based off of data its trained off of and conversations its already had. A RAG model, however, doesn't purely rely on memory it finds relevant pages, reads them and writes answers based on those pages.

The general flow is Question -> Retriever -> Relevant documents -> LLM -> Answer

Retrieval works by sending relevant chunks to the LLM rather than entire documents as to not waste tokens and optimise response time. 

These Chunks are searched using embeddings where an embedding converts text into a vector that capture its meaning and these vectors are stored in a vector database. This is better than keyword search as it allows for synonyms.

The retrieval process is: 
- convert question to embedding
- compare it with stored chunk embeddings
- find closest Chunk
- returns 5 similar matches

The received chunks are then added to the prompt and the LLM now has the relevant data. Instead of relying on memory is relies on documents and LLM reasoning. 

The RAG doesn't 
