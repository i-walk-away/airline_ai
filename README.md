# Airline AI

Choose an airport and ask your question. The model will generate an answer based on current flights. 

## Architecture of LLM integration

The LLM integration is implemented through a dedicated [DeepSeekClient](src/clients/llm/deepseek.py) class
which inherits from the [AbstractLlmClient](src/clients/llm/abstract.py) class to ensure scalability in case we want
to implement other LLM models. The OpenRouter API is used to query the LLM.

The [FlightsService](src/services/flights.py) retrieves airport data and its schedule from FlightAPI in Pydantic model
format, passes it to the [prompt](src/static/prompts.py) and sends it to the LLM. The model returns a plain-text Markdown
answer, which is then rendered on the frontend.

## Query flow

1. The user selects an airport and types their question in the frontend form.
2. The frontend sends a POST request to `/ask` with form data.
3. The FastAPI route forwards this request to `FlightsService`.
4. In the `FlightsService`:
    - Calls `FlightApiClient` to retrieve data and schedule for the given airport.
    - Formats airport data from JSON to Pydantic models.
    - Builds a prompt based on airport data and schedule.
5. `DeepSeekClient` sends the prompt to the LLM via OpenRouter API.
6. The model responds with either plain-text or markdown-formatted answer.
7. The backend returns the answer to the frontend, which displays it on the page.

## Why this approach

The overall architecture of this project ensures all layers are separated by their responsibility, which allows
for scalability, maintainability and extensibility:

- External integrations (FlightAPI, OpenRouter API) are isolated in the `clients` layer.
- All application logic, including prompt construction, data preprocessing, and complex response interpretation,
  is handled in the `services` layer.
- FastAPI-dependent code is isolated in the presentation layer (`routes`) and is kept lightweight.
