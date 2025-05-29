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

## Running Your MCP Server

### Method 1: Standalone MCP Server
Run your custom MCP server:
```bash
cd C:\Users\username\projects\pr_reviewer
python pr_analyzer.py
```

This will start your MCP server with all the RAG tools available.

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

### 2. `create_notion_page(title, content)`
Create a Notion page with analysis results.

## Testing Your Setup

### Step 1: Test RAG System

### Step 2: Test MCP Server
```bash
python pr_analyzer.py
```
Should show: "Running MCP Server for GitHub PR Analysis..."

## Usage Examples

### Analyzing a PR:
in Claude
Once connected, try:
`Analyse this PR [link to PR]`

