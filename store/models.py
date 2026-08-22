from django.db import models  # noqa: F401

# ---------------------------------------------------------------------------
# NOTE: This version of the site is a Django-rendered landing page only.
# There are intentionally no application models yet. All display content
# (books, categories, testimonials, events, etc.) lives in store/data.py so
# a non-technical client can update it without touching the database.
#
# When the client is ready for a real online store, this is where the
# following models would live: Book, Category, Author, Customer, Cart,
# Wishlist, Order, Payment, Inventory. Keeping this file empty now keeps
# the migration history clean for that future step.
# ---------------------------------------------------------------------------
