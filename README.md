# Kavish Business Management

Internal owner/partner business management application.

## Stack
- Frontend: React + Vite + Tailwind CSS + PWA
- Backend: Django + Django REST Framework
- Database: PostgreSQL (configure your Django settings for production)

## Run locally

### Backend
Open PowerShell in `backend`:

```powershell
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8001
```

The API runs at `http://127.0.0.1:8001/api`.

### Frontend
Open a second PowerShell in `frontend`:

```powershell
npm install
npm run dev
```

Open the Vite URL shown in the terminal, normally `http://localhost:5173`.

If the API is on another URL, copy `.env.example` to `.env` and set `VITE_API_URL`.

## Default local login
The supplied backend accepts the normal Django REST token endpoint. Create/use your Django user in the backend environment. If your local copy already has an owner user, use those credentials.

## Frontend modules
Dashboard, Sales, Expenses, Purchases, Stock, Petrol & Travel, Allowance, Salary, Partners, Customers, Suppliers, Cash, Bank, General Transactions, Reports and Settings.

The UI is mobile-first and includes responsive navigation, CRUD forms, search, pagination, confirmation before delete, calculated sale/purchase/petrol/salary values, loading/error/empty states and PWA configuration.

## Important
The frontend only claims a record was saved after the backend request succeeds. It does not use browser localStorage as the business database; localStorage is used only for the authentication token/session convenience.

The current backend ZIP contains the API/model foundation that was already migrated successfully. For production, configure PostgreSQL, environment variables, secure CORS/auth settings, backup/restore and the remaining server-side financial workflows before deployment.
