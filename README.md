# Contact List

<div align="center">
  <p><strong>A clean full-stack contact manager built with React, Vite, Flask, and SQLite.</strong></p>
  <p>Create contacts, update details, remove entries, and manage everything through a simple browser-based UI.</p>
</div>

---

## Preview

```text
React + Vite frontend  <-->  Flask REST API  <-->  SQLAlchemy  <-->  SQLite
```

This project is a lightweight CRUD application for managing contacts. The frontend handles the user experience, while the backend exposes a small API for creating, reading, updating, and deleting contact records.

## Highlights

- Clean React interface for viewing and managing contacts
- Modal-based form for creating and editing entries
- Flask API with clear CRUD endpoints
- SQLite persistence through Flask-SQLAlchemy
- CORS enabled for local frontend/backend development
- Small, easy-to-understand project structure for learning and extending

## Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | React 19, Vite |
| Backend | Flask 3, Flask-SQLAlchemy, Flask-CORS |
| Database | SQLite |
| Tooling | ESLint, npm |

## Project Structure

```text
Contact-List/
|-- backend/
|   |-- config.py
|   |-- main.py
|   |-- models.py
|   `-- requirements.txt
|-- frontend/
|   |-- package.json
|   |-- src/
|   |   |-- App.jsx
|   |   |-- ContactForm.jsx
|   |   |-- ContactList.jsx
|   |   |-- App.css
|   |   `-- index.css
|   `-- vite.config.js
`-- README.md
```

## Features

- View all saved contacts in a table
- Add a new contact with first name, last name, and email
- Edit an existing contact from the same form modal
- Delete contacts instantly from the list
- Refresh the UI automatically after mutations

## API Endpoints

| Method | Route | Purpose |
| --- | --- | --- |
| `GET` | `/contacts` | Fetch all contacts |
| `POST` | `/create_contact` | Create a new contact |
| `PATCH` | `/update_contact/<user_id>` | Update an existing contact |
| `DELETE` | `/delete_contact/<user_id>` | Delete a contact |

## Local Setup

### 1. Backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

The backend starts on `http://127.0.0.1:5000`.

Notes:

- The SQLite database is created automatically on first run.
- The app currently runs with `debug=True` for development.

### 2. Frontend

Open a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

The frontend usually starts on `http://localhost:5173`.

## How It Works

1. The React app loads contacts from the Flask API on startup.
2. Form submissions send `POST` or `PATCH` requests depending on whether a contact is being created or edited.
3. Delete actions send a `DELETE` request to the backend.
4. SQLAlchemy writes changes into SQLite and the frontend refreshes the list.

## Development Notes

- The frontend currently calls the backend using hardcoded local URLs at `http://127.0.0.1:5000`.
- Email addresses must be unique in the database model.
- This project is a strong starter base for search, pagination, validation, authentication, or deployment work.

## Future Improvements

- Add client-side and server-side validation
- Introduce environment-based API configuration
- Improve styling and responsive layout
- Add success/error toast notifications
- Add tests for API routes and UI flows

## License

This project is available for personal learning and customization.
