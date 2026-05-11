"""
Knowledge Agent — Person 1
==========================
RAG pipeline: embeds past project docs into Supabase (pgvector), retrieves similar ones on query.

Dependencies: supabase-py, app.utils.llm_wrapper (get_embedding)

How Supabase vector search works:
  1. You store embeddings in a table with a `vector` column (using pgvector extension)
  2. You use Supabase's `.rpc()` to call a SQL function that does similarity search
  3. The SQL function uses cosine distance to find nearest neighbors

Setup required in Supabase Dashboard (one-time):
  1. Go to SQL Editor → run: CREATE EXTENSION IF NOT EXISTS vector;
  2. Create the documents table (see below)
  3. Create the match function (see below)

SQL to run in Supabase SQL Editor:
  
  -- Enable pgvector
  CREATE EXTENSION IF NOT EXISTS vector;

  -- Create documents table
  CREATE TABLE documents (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    content TEXT,
    metadata JSONB,
    embedding vector(1536),
    created_at TIMESTAMPTZ DEFAULT now()
  );

  -- Create similarity search function
  CREATE OR REPLACE FUNCTION match_documents(
    query_embedding vector(1536),
    match_count INT DEFAULT 5,
    filter JSONB DEFAULT '{}'
  ) RETURNS TABLE (
    id UUID,
    content TEXT,
    metadata JSONB,
    similarity FLOAT
  ) LANGUAGE plpgsql AS $$
  BEGIN
    RETURN QUERY
    SELECT
      documents.id,
      documents.content,
      documents.metadata,
      1 - (documents.embedding <=> query_embedding) AS similarity
    FROM documents
    ORDER BY documents.embedding <=> query_embedding
    LIMIT match_count;
  END;
  $$;
"""

from supabase import create_client
from app.utils.llm_wrapper import get_embedding
from app.config import settings

# Initialize Supabase client
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


async def ingest_document(text: str, metadata: dict) -> str:
    """
    TODO (Person 1): Implement this function.
    
    Steps:
      1. Chunk the text into ~500 token pieces (use langchain text splitter)
      2. Generate embeddings for each chunk using get_embedding()
      3. Store in Supabase 'documents' table with metadata
      4. Return the document ID
    
    Example:
      embedding = get_embedding("some text chunk")
      result = supabase.table("documents").insert({
          "content": "some text chunk",
          "metadata": {"project_name": "Client X", "type": "case_study"},
          "embedding": embedding
      }).execute()
    """
    # STUB — replace with real implementation
    return "doc_stub_id"


async def search_knowledge(query: str, top_k: int = 5) -> list[dict]:
    """
    TODO (Person 1): Implement this function.
    
    Steps:
      1. Generate embedding for the query using get_embedding()
      2. Call the match_documents function via Supabase RPC
      3. Return top-K results with scores and metadata
    
    Example:
      query_embedding = get_embedding("RAG pipeline for healthcare")
      result = supabase.rpc("match_documents", {
          "query_embedding": query_embedding,
          "match_count": top_k
      }).execute()
    
    Expected output:
    [
        { "project_name": "Client X - RAG System", "score": 0.92, "summary": "..." },
        { "project_name": "Client Y - Chatbot", "score": 0.87, "summary": "..." },
    ]
    """
    # STUB
    return [{"project_name": "Stub Project", "score": 0.0, "summary": "Not implemented"}]
