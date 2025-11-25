# TODO App

A simple Django TODO application to manage your tasks.

## 🌟 Features

### Core Functionality
- ✅ **Create TODOs** - Add new tasks with title, description, and optional due dates
- ✏️ **Edit TODOs** - Update task details at any time
- 🗑️ **Delete TODOs** - Remove completed or unwanted tasks
- ✓ **Mark as Resolved** - Toggle task completion status
- 📅 **Due Date Assignment** - Set deadlines for your tasks

### User Experience
- 🎨 **Modern UI** - Clean, responsive design with Bootstrap 5
- 📱 **Mobile Friendly** - Works seamlessly on all devices
- 💬 **User Feedback** - Success/error messages for all actions
- 🎯 **Smart Sorting** - Unresolved TODOs displayed first

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/winggotayy/ai-dev-tools.git
cd /workspaces/ai-dev-tools/01-todo
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and navigate to:

```bash
"$BROWSER" http://localhost:8000
```

- **Main App:** http://localhost:8000

## 🧪 Testing

### Run All Tests

```bash
python manage.py test
```

### Run Tests with Verbose Output

```bash
python manage.py test -v 2
```

### Run Specific Test Module

```bash
python manage.py test todo.tests.TodoModelTest
```

### Test Coverage

The application includes comprehensive tests for:
- ✅ Model creation and validation
- ✅ View functionality (GET/POST requests)
- ✅ CRUD operations
- ✅ Todo resolution toggle
- ✅ Template rendering

## 📁 Project Structure

```
01-todo/
├── todo_project/           # Main Django project
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project URL configuration
│   └── wsgi.py
├── todo/                   # TODO app
│   ├── migrations/         # Database migrations
│   ├── templates/
│   │   └── todos/
│   │       ├── list.html
│   │       ├── create.html
│   │       ├── edit.html
│   │       └── delete.html
│   ├── __init__.py
│   ├── admin.py            # Admin interface configuration
│   ├── apps.py
│   ├── forms.py            # Django forms
│   ├── models.py           # Database models
│   ├── tests.py            # Unit tests
│   ├── urls.py             # App URL routing
│   └── views.py            # View functions
├── templates/              # Base templates
│   ├── base.html
│   ├── create_todo.html
│   ├── edit_todo.html
│   └── delete_todo.html
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
├── venv/                   # Virtual environment
└── README.md               # This file
```

## 🗄️ Database Schema

### Todo Model

```python
- id (Primary Key)
- title (CharField, max_length=200)
- description (TextField, optional)
- due_date (DateTimeField, optional)
- is_resolved (BooleanField, default=False)
- created_at (DateTimeField, auto-generated)
- updated_at (DateTimeField, auto-updated)
```

## 🔗 URL Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display all TODOs |
| `/create/` | GET/POST | Create new TODO |
| `/<id>/edit/` | GET/POST | Edit TODO |
| `/<id>/delete/` | GET/POST | Delete TODO |
| `/<id>/toggle/` | POST | Toggle resolved status |
| `/admin/` | GET/POST | Django admin panel |

## 💡 Usage Examples

### Creating a TODO

1. Click **"+ New TODO"** button
2. Enter title and optional description
3. Set optional due date
4. Click **"Create TODO"**

### Editing a TODO

1. Click **"✏️ Edit"** on any TODO card
2. Update the fields as needed
3. Optionally mark as resolved
4. Click **"Update TODO"**

### Completing a TODO

1. Click **"✓ Resolve"** on active TODOs
2. Task moves to "Resolved TODOs" section
3. Click **"↩️ Unresolve"** to reopen

### Deleting a TODO

1. Click **"🗑️ Delete"** on any TODO
2. Confirm deletion on confirmation page
3. TODO is permanently removed

## 🎨 Customization

### Change Styling

Edit `/workspaces/ai-dev-tools/01-todo/templates/base.html` to customize colors and styling.

### Add New Fields

1. Update `todo/models.py` with new fields
2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Update `todo/forms.py` to include new fields
4. Update templates as needed

### Create Admin Users

```bash
python manage.py createsuperuser
```

## 🐛 Troubleshooting

### Port 8000 Already in Use

```bash
python manage.py runserver 8001
```

### Database Issues

Reset the database:

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Template Not Found

Ensure `templates/` directory exists and `settings.py` has correct `TEMPLATES` configuration.

### Module Not Found Errors

Activate virtual environment:

```bash
source venv/bin/activate
```
---

**Happy Task Managing! 🚀**

Last Updated: November 25, 2025