# OpenAI with BrightData MCP

A Python application that integrates OpenAI's GPT models with BrightData's MCP (Model Context Protocol) server for enhanced web search and data retrieval capabilities.

## Features

- **Interactive AI Chat**: Ask questions and get AI-powered responses with web search capabilities
- **BrightData Integration**: Leverages BrightData's MCP server for real-time web scraping and search
- **Rich Markdown Display**: Beautiful terminal output with proper markdown rendering using Rich
- **Environment-based Configuration**: Secure API key management using environment variables

## Prerequisites

- Python 3.13 or higher
- OpenAI API key
- BrightData API token

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd openai-with-brightdatamcp
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Set up environment variables:
Create a `.env` file in the project root with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
BRIGHT_DATA_API_TOKEN=your_brightdata_token_here
```

## Usage

Run the application:
```bash
uv run main.py
```

The program will prompt you with "What would you like to know?" - simply type your question and press Enter. The AI will use BrightData's web search capabilities to provide comprehensive, up-to-date answers.

### Example Questions

- "What are the latest phones to buy in 2025?"
- "Can you recommend good books to read?"
- "What's the current weather in New York?"
- "Find me the best restaurants in San Francisco"

## How It Works

1. **User Input**: The application prompts for user questions
2. **MCP Integration**: Questions are sent to OpenAI's GPT-4o model with BrightData MCP tools enabled
3. **Web Search**: BrightData's MCP server performs real-time web searches and data extraction
4. **AI Processing**: GPT-4o processes the web data and generates comprehensive responses
5. **Rich Display**: Responses are rendered with beautiful markdown formatting in the terminal

## Dependencies

- `openai>=2.0.0` - OpenAI Python client
- `python-dotenv>=1.1.1` - Environment variable management
- `rich>=14.1.0` - Rich text and markdown rendering

## Configuration

The application uses two main configuration points:

- **OpenAI API Key**: Required for GPT model access
- **BrightData API Token**: Required for MCP server access and web search capabilities

Both are loaded from environment variables for security.

## Error Handling

The application includes proper error handling for:
- Missing API keys
- Network connectivity issues
- MCP server unavailability
- Invalid responses

## License

This project is open source. Please check the license file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Support

For issues related to:
- **OpenAI API**: Check the [OpenAI Documentation](https://platform.openai.com/docs)
- **BrightData MCP**: Check the [BrightData Documentation](https://brightdata.com/)
- **This Project**: Open an issue in this repository
