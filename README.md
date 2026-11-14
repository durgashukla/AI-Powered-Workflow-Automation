# AI-Powered Workflow Automation System

## Project Overview

AI-Powered Workflow Automation System is a web-based application designed to automate customer enquiry management using Artificial Intelligence.

The system collects customer enquiries, analyzes their requirements using AI, identifies the relevant service category and priority, and generates a suggested response for the admin.

It helps businesses manage customer enquiries more efficiently.

## Features

- Customer enquiry submission form
- AI-powered enquiry analysis
- Automatic service category identification
- Budget and location extraction
- High, Medium, and Low priority classification
- Requirement summary and missing information detection
- AI-generated suggested response
- Editable suggested response for admins
- Admin login and dashboard
- View and search customer enquiries
- Filter enquiries by category, priority, and status
- Update enquiry status:
  - New
  - In Progress
  - Converted
- Dashboard charts for category and priority distribution

## Technology Stack

**Backend:** Python, Django

**Frontend:** HTML, CSS, JavaScript

**AI Integration:** Groq API

**AI Model:** openai/gpt-oss-20b

**Database:** SQLite

**Environment Management:** python-dotenv

## How It Works

1. Customer submits an enquiry through the website.
2. The enquiry message is sent to the AI service.
3. AI analyzes the message and extracts:
   - Service category
   - Budget
   - Location
   - Priority
   - Requirements
   - Missing information
   - AI summary
   - Suggested response
4. The extracted information is saved in the SQLite database.
5. Admin logs in to the dashboard.
6. Admin reviews enquiries, edits suggested responses, and updates their status.

## Database Models

### Enquiry

The Enquiry model stores:

- Customer name
- Phone number
- Email
- Enquiry message
- Service category
- Budget
- Location
- Priority
- Requirements
- Missing information
- AI summary
- Suggested response
- Enquiry status
- Created and updated timestamps

## Project Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Powered-Workflow
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your own API key.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Admin Account

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Security Note

- API keys are stored in environment variables.
- The `.env` file is excluded from Git using `.gitignore`.
- Never share your private API key publicly.

## Future Improvements

- Email notifications for new enquiries
- Advanced enquiry analytics
- Improved AI-based lead qualification
- Deployment to a production hosting platform


