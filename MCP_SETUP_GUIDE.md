# MCP Server Setup Guide

## Overview
This guide helps you set up your custom MCP server for PR analysis and RAG-based PDF querying.

## Prerequisites

### 1. Install Dependencies
Make sure all dependencies are installed:
```bash
cd C:\Users\username\projects\pr_reviewer
pip install -e .
```

### 2. Set Up Environment Variables
Create or update your `.env` file with:
```env
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3

# GitHub API (for PR analysis)
GITHUB_TOKEN=your_github_token_here

# Notion Integration (optional)
NOTION_API_KEY=your_notion_api_key
NOTION_PAGE_ID=your_notion_page_id
```

### 3. Start Ollama
Make sure Ollama is running with your model:
```bash
# Start Ollama service
ollama serve

# In another terminal, pull the model if needed
ollama pull llama3
```

## Running Your MCP Server

### Method 1: Standalone MCP Server
Run your custom MCP server:
```bash
cd C:\Users\username\projects\pr_reviewer
python main.py
```

This will start your MCP server with all the RAG tools available.

### Method 2: Testing Before MCP
First validate your RAG system works:
```bash
cd C:\Users\username\projects\pr_reviewer
python test_rag.py
```

## Connecting Claude to Your MCP Server

### Option 1: Claude Desktop Configuration
If using Claude Desktop, add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "pr-reviewer": {
      "command": "python",
      "args": ["C:\\Users\\username\\projects\\project_folder\\main.py"],
      "cwd": "C:\\Users\\username\\projects\\project_folder"
    }
  }
}
```

### Option 2: Multiple MCP Servers
To run both filesystem and your custom server, you can configure multiple servers:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\Users\\username\\projects"]
    },
    "pr-reviewer": {
      "command": "python", 
      "args": ["C:\\Users\\username\\projects\\project_folder\\main.py"],
      "cwd": "C:\\Users\\username\\projects\\project_folder"
    }
  }
}
```

## Available MCP Tools

Once connected, you'll have these tools available:

### 1. `fetch_pr(repo_owner, repo_name, pr_number)`
Fetch and analyze GitHub pull requests.

### 2. `index_pdf(filename)`
Index a PDF file from the `data/pdfs/` directory into the vector database.
Example: `index_pdf("Barclays-PLC-Annual-Report-2020.pdf")`

### 3. `query_vector_db(query, top_k=5)`
Query the indexed documents using RAG.
Example: `query_vector_db("What was Barclays' revenue in 2020?")`

### 4. `list_indexed_documents()`
List all documents currently indexed in the vector database.

### 5. `create_notion_page(title, content)`
Create a Notion page with analysis results.

## Testing Your Setup

### Step 1: Test RAG System
```bash
python test_rag.py
```

### Step 2: Test MCP Server
```bash
python main.py
```
Should show: "Running MCP Server for GitHub PR Analysis..."

### Step 3: Test in Claude
Once connected, try:
1. `index_pdf("Barclays-PLC-Annual-Report-2020.pdf")`
2. `query_vector_db("What is Barclays' business model?")`
3. `list_indexed_documents()`

## Troubleshooting

### Common Issues:

1. **Ollama Connection Failed**
   - Make sure Ollama is running: `ollama serve`
   - Check the model is available: `ollama list`
   - Verify the base URL in your .env file

2. **PDF Not Found**
   - Ensure the PDF is in `data/pdfs/` directory
   - Check the exact filename matches

3. **Import Errors**
   - Install dependencies: `pip install -e .`
   - Check Python environment is activated

4. **MCP Server Not Connecting**
   - Verify the server starts without errors
   - Check Claude's MCP configuration
   - Ensure paths are correct in config

### Debug Mode
Add this to your `.env` for more verbose logging:
```env
DEBUG=true
```

## Usage Examples

### Indexing the Barclays PDF:
```python
# This will be available as an MCP tool
index_pdf("Barclays-PLC-Annual-Report-2020.pdf")
```

### Querying the Report:
```python
query_vector_db("What were the key financial highlights for 2020?", top_k=3)
query_vector_db("How did COVID-19 impact Barclays' business?")
query_vector_db("What are Barclays' main business segments?")
```

### Analyzing a PR:
```python
fetch_pr("usernamecostanzo", "mcp-rag-server", 1)
```
