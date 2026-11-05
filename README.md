
# Odoo Office Equipment Tracker

A custom Odoo 18 Community module for managing
company equipment and employee assignments.

## Overview

This project helps a company track its office
equipment, assigned users, due dates, and
equipment availability.

## Features

- Register and manage office equipment
- Categorize equipment
- Assign equipment to internal users
- Track checkout and return dates
- Detect overdue equipment
- Filter available, assigned, and overdue items
- Prevent duplicate asset codes
- Mark equipment as returned

## Technologies

- Odoo 18 Community Edition
- Python
- PostgreSQL
- XML
- Docker and Docker Compose
- Git and GitHub

## Module Structure

```text
office_equipment_tracker/
├── __init__.py
├── __manifest__.py
├── models/
├── security/
└── views/
```

## Installation

1. Start Docker Desktop.
2. Run `docker compose up -d`.
3. Open http://localhost:8069.
4. Create an Odoo database.
5. Activate Developer Mode.
6. Update the Apps List.
7. Search for Office Equipment Tracker.
8. Install the module.

## What I Learned

- Creating custom Odoo modules
- Working with the Odoo ORM
- Defining relational database fields
- Creating XML list and form views
- Configuring access permissions
- Implementing business logic and validation
- Running Odoo with Docker and PostgreSQL

## Author

Shoon Lae Than Tun
