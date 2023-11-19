# Home Assistant LLM Interface

This project provides an interface between Home Assistant and OpenAI's Language Model (LLM), specifically GPT4, to process and handle user queries.

## Files

1. `query.bash`: A bash script that sends a POST request to the local server, processes the JSON response, and sends commands to the Home Assistant API.

2. `server.py`: A Flask server that receives POST requests, sends the request data to OpenAI's API, and returns the response.

3. `config.sample`: A sample configuration file containing API keys and endpoints for OpenAI and Home Assistant.

## Usage

1. Rename `config.sample` to `config` and fill in your OpenAI and Home Assistant API keys and endpoints.

2. Run the Flask server using the command `python server.py`.

3. Send a query to the server using the `query.bash` script with your query as an argument. For example, `./query.bash "turn on the lights"`.

## Dependencies

- Flask
- OpenAI
- jq
- curl

## Note

This project is for demonstration purposes only. Be sure to secure your API keys and endpoints.
