# Inkleaf Book House — Premium Book Store Landing Page

A frontend-focused, Django-rendered landing page for a fictional independent
bookstore. No database-driven ecommerce — all content lives in
`store/data.py` so it's easy for a client to edit without touching code.

---

## 1. Requirements

- Python 3.10+
- pip

## 2. Local setup

```bash
# Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply Django's built-in migrations (admin/auth/sessions only —
# this project has no application models)
python manage.py migrate

# Run the dev server
python manage.py runserver
```

Open **http://127.0.0.1:8000/**

## 3. Project structure

```text
book_store/
├── manage.py
├── requirements.txt
├── db.sqlite3                 (created after `migrate`, dev-only)
│
├── book_store/                 # project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── store/                       # the app
│   ├── views.py                  # home + enquiry views
│   ├── urls.py
│   ├── forms.py                   # ContactForm
│   ├── data.py                     # ALL editable site content lives here
│   ├── models.py                    # intentionally empty (see file for notes)
│   └── migrations/
│
├── templates/
│   ├── base.html
│   └── store/                        # one template per section
│       ├── home.html
│       ├── navbar.html, hero.html, stats.html, about.html,
│       ├── categories.html, featured_books.html, best_sellers.html,
│       ├── offers.html, author_spotlight.html, reading_section.html,
│       ├── why_choose_us.html, testimonials.html, gallery.html,
│       ├── events.html, delivery.html, contact.html, map.html,
│       ├── final_cta.html, footer.html
│
└── static/
    ├── css/style.css
    └── js/main.js
```

## 4. Editing content for a real client

Open `store/data.py`. Every section pulls from a Python variable there:

| Variable            | Powers                                       |
|-----------------------|------------------------------------------------|
| `BUSINESS`             | Name, phone, email, address, map, hours          |
| `STATS`                 | The 4-number trust strip                          |
| `CATEGORIES`             | Category cards                                     |
| `BOOKS`                   | Featured book cards + prices                        |
| `BEST_SELLERS`             | Slice of `BOOKS` shown in the carousel                |
| `OFFER`                     | Book Lovers' Week deal + countdown length              |
| `AUTHOR_SPOTLIGHT`           | The featured author section                             |
| `READING_BENEFITS`             | The five reading-benefit bullets                          |
| `WHY_CHOOSE_US`                  | The 6 trust cards                                           |
| `TESTIMONIALS`                     | Review carousel                                               |
| `GALLERY`                            | Instagram-style gallery grid                                    |
| `EVENTS`                               | Author meet & greets, book club, story time                       |
| `DELIVERY`                                | Delivery areas + free-delivery threshold                             |

Replace the Unsplash placeholder image URLs with the client's own book
photography and store interior shots before launch — swap them for files
under `static/images/` and point each entry in `data.py` at
`{% static 'images/...' %}` (or plain relative URLs if you keep hotlinking).

## 5. Enquiry form + email (optional)

The contact form works without any configuration — it validates and shows
a success message. To also forward enquiries by email, set these
environment variables before running the server:

```bash
export EMAIL_HOST_USER="your@gmail.com"
export EMAIL_HOST_PASSWORD="an-app-password"
export ENQUIRY_RECEIVING_EMAIL="hello@inkleafbooks.in"
```

Never commit real SMTP credentials — keep them in environment variables or
a `.env` file that is git-ignored.

## 6. Git

```bash
git init
git add .
git commit -m "Initial commit: Inkleaf Book House landing page"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

A `.gitignore` is already included, covering `.venv/`, `__pycache__/`,
`db.sqlite3`, `staticfiles/`, `media/` and `.env`.

## 7. Deployment

```bash
# Collect static files for production
python manage.py collectstatic --noinput

# Set production environment variables
export DJANGO_DEBUG=False
export DJANGO_SECRET_KEY="a-long-random-production-secret"
export DJANGO_ALLOWED_HOSTS="www.yourdomain.com,yourdomain.com"

# Serve with a production WSGI server, e.g. gunicorn
pip install gunicorn whitenoise
gunicorn book_store.wsgi:application --bind 0.0.0.0:8000
```

For static files in production, the simplest option is `whitenoise`: add
`'whitenoise.middleware.WhiteNoiseMiddleware'` right after
`SecurityMiddleware` in `MIDDLEWARE`, then run `collectstatic`.

Note: Django is not a natural fit for Vercel's serverless model (no
persistent filesystem, no long-running WSGI process). If the client
specifically wants a Vercel deployment, the practical options are:
(a) deploy this project as-is to Render, Railway, PythonAnywhere or a
small VPS, which all support Django natively, or (b) use Vercel's
Python/WSGI runtime with `@vercel/python`, keeping `DEBUG=False` and
serving static files via whitenoise or an external bucket — but a
traditional host will be simpler and cheaper for a small landing page.

## 8. Future extensibility (not implemented yet)

`store/models.py` documents where a future `Book`, `Category`, `Author`,
`Customer`, `Cart`, `Wishlist`, `Order`, `Payment` and `Inventory` model
set would live once the client is ready for a real, database-driven
online store with an admin dashboard.
