# LinkedIn Bullshit Meter

An AI-powered application that analyzes LinkedIn posts for vagueness, exaggeration, corporate jargon, lack of evidence, and filler.

The application uses the OpenAI API to generate a structured analysis and calculates an overall score from 0 to 100.

## Features

- Analyze a LinkedIn post through a browser interface.
- Score five dimensions, each from 0 to 20.
- Calculate an overall score from 0 to 100.
- Classify posts from "Substantive" to "Maximum LinkedIn".
- Explain the score and highlight suspicious phrases.
- Run a benchmark of sample posts.
- Run automated unit tests for scoring logic.

## Project Structure

- `streamlit_app.py` — browser interface
- `app.py` — command-line interface
- `analyzer.py` — AI analysis and scoring logic
- `prompts.py` — instructions and examples sent to the model
- `evaluation.py` — benchmark dataset
- `main.py` — evaluation runner
- `test_analyzer.py` — unit tests

## Requirements

- Python 3.9 or a compatible newer version supported by the dependencies
- An OpenAI API key with API access and available billing or credits

## Setup

Clone the repository and navigate into the project directory.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key.

Never commit your `.env` file or share your API key publicly.

## Run the Web Application

```bash
streamlit run streamlit_app.py
```

Open the local URL displayed in the terminal.

Paste a LinkedIn post and click **Analyze post**. Each analysis makes an OpenAI API request.

## Run the Command-Line Application

```bash
python app.py
```

Paste the post across multiple lines and type `DONE` on a new line when finished.

## Run the Evaluation Benchmark

```bash
python main.py
```

This runs the sample evaluation dataset and makes API requests for the posts being analyzed.

## Run Unit Tests

```bash
python -m unittest test_analyzer -v
```

The unit tests check score calculations and category boundaries without making API calls.

## Limitations

The score measures rhetorical style and the presence of supporting evidence. It does not determine whether a person is lying or whether a claim is factually true. Results may vary between model responses and should be interpreted as estimates rather than objective truth.