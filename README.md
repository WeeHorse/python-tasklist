# Tkinter Task List App (with PostgreSQL)

This is a simple desktop task list application built with **Tkinter** and **PostgreSQL**.

## Features

- Multiple users
- Each user can have multiple lists
- Each list can contain multiple tasks
- Tasks can be marked as done or not
- Add new tasks via UI

## Requirements

- Python 3.x
- PostgreSQL
- psycopg2 (Python PostgreSQL client)

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up the PostgreSQL database

Run the following SQL script using your PostgreSQL client or GUI:

```sql
-- See schema.sql for full script
```

Or run:

```bash
psql -U your_user -d your_db -f schema.sql
```

### 3. Update database credentials

Open `app.py` and edit the `psycopg2.connect` call with your database info.

### 4. Run the app

```bash
python app.py
```

