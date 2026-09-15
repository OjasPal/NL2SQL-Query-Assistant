# NL2SQL Query Assistant 🗄️

A simple Streamlit app that converts natural language questions into SQL queries using Google's Gemini AI, then runs them against a SQLite database and shows the results.

## Features

- Ask questions about a student database in plain English
- Gemini converts your question into a SQL query
- The generated query runs automatically against a local SQLite database
- View both the generated SQL and the query results

## Tech Stack

- [Streamlit](https://streamlit.io/) — web UI
- [Google Gemini API](https://ai.google.dev/) — natural language to SQL
- SQLite — local database
- python-dotenv — environment variable management

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/OjasPal/NL2SQL-Query-Assistant
   cd NL2SQL-Query-Assistant
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**

   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. **(Optional) Regenerate the database**

   A `student.db` file with sample data is already included. If you want to reset or recreate it, run:
   ```bash
   python sqlite.py
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then:
1. Type a question about the student database (e.g. *"Tell names of people who have more than or equal to 90 marks"*)
2. Click **Generate & Run Query**
3. View the generated SQL query and the results below it

## Sample Database Schema

The `STUDENT` table contains:

| Column  | Type        |
|---------|-------------|
| NAME    | VARCHAR(25) |
| CLASS   | VARCHAR(25) |
| SECTION | VARCHAR(25) |
| MARKS   | INT         |

## Project Structure

```
.
├── app.py             # Main Streamlit application
├── sqlite.py           # Creates/populates the sample SQLite database
├── student.db            # Sample SQLite database
├── requirements.txt       # Python dependencies
├── .gitignore              # Files/folders excluded from git
├── LICENSE                  # Project license
└── README.md                 # Project documentation
```

## Notes

- Make sure `.env` is listed in `.gitignore` so your API key isn't pushed to GitHub.
- This app is not deployed — it's meant to run locally for now.
