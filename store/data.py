"""
Central content store for the Inkleaf Book House landing page.

There is no database-driven ecommerce in this version of the project, so
every piece of copy, pricing and imagery the templates render lives here
as plain Python data structures. This keeps `views.py` and the templates
clean, and means a client can update a price, add a testimonial, or list
a new event by editing one file — no migrations required.

When a real catalogue is introduced later, this file maps almost 1:1 onto
future `Book` / `Category` / `Author` / `Event` models.
"""

BUSINESS = {
    "name": "Inkleaf Book House",
    "short_name": "Inkleaf",
    "tagline": "Stories Bound. Minds Opened.",
    "phone_display": "+91 98450 22981",
    "phone_link": "919845022981",
    "email": "hello@inkleafbooks.in",
    "address_line1": "17 Chamiers Road",
    "address_line2": "Alwarpet, Chennai, Tamil Nadu 600018",
    "hours_weekday": "Monday – Saturday, 9:00 AM – 9:00 PM",
    "hours_sunday": "Sunday, 10:00 AM – 8:00 PM",
    "whatsapp_default_message": "Hi Inkleaf, I'd like to know more about your book collection.",
    "map_embed_src": "https://www.openstreetmap.org/export/embed.html?bbox=80.2470%2C13.0270%2C80.2770%2C13.0470&layer=mapnik&marker=13.0370%2C80.2620",
    "map_link": "https://www.openstreetmap.org/?mlat=13.0370&mlon=80.2620#map=15/13.0370/80.2620",
    "instagram": "https://instagram.com/",
    "facebook": "https://facebook.com/",
    "youtube": "https://youtube.com/",
}

STATS = [
    {"value": 11000, "suffix": "+", "label": "Books In Store"},
    {"value": 480, "suffix": "+", "label": "Authors Stocked"},
    {"value": 26000, "suffix": "+", "label": "Happy Readers"},
    {"value": 49, "suffix": "/5", "label": "Average Rating"},
]

ABOUT_FEATURES = [
    {"title": "Curated Collection", "text": "Every title on our shelves earned its place — we don't stock filler."},
    {"title": "Helpful Recommendations", "text": "Tell us what you loved last, and we'll find your next favourite."},
    {"title": "A Space For Readers", "text": "Armchairs, good light, and no one rushing you to check out."},
]

CATEGORIES = [
    {"name": "Fiction", "description": "Novels and short stories that stay with you long after the last page.",
     "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=800&q=80", "icon": "bi-book"},
    {"name": "Self Development", "description": "Habits, mindset and craft — practical wisdom for the life you want.",
     "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=800&q=80", "icon": "bi-graph-up-arrow"},
    {"name": "Technology", "description": "Code, design and the ideas shaping how we build things.",
     "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80", "icon": "bi-cpu"},
    {"name": "Business", "description": "Strategy, leadership and the stories behind great companies.",
     "image": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=800&q=80", "icon": "bi-briefcase"},
   {
    "name": "Children's Books",
    "description": "Picture books and early readers that spark a lifelong habit.",
    "image": "https://blog.siliconvalleyinternational.org/hubfs/Miscellaneous/Imported_Blog_Media/kid-4092600-1.jpg",
    "icon": "bi-emoji-smile"
},
    {"name": "Academic", "description": "Reference texts and coursebooks for school, college and beyond.",
     "image": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=800&q=80", "icon": "bi-mortarboard"},
    {"name": "Biography", "description": "Real lives, honestly told — the ones worth learning from.",
     "image": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=800&q=80", "icon": "bi-person-lines-fill"},
    {"name": "Exam Preparation", "description": "Structured guides and practice sets for competitive exams.",
     "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=800&q=80", "icon": "bi-clipboard-check"},
]

BOOKS = [
    {"title": "Atomic Habits", "author": "James Clear", "price": 599, "category": "Self Development",
     "rating": 5, "badge": "Bestseller",
     "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=500&q=80"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "price": 399, "category": "Fiction",
     "rating": 5, "badge": "Reader Favourite",
     "image": "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?auto=format&fit=crop&w=500&q=80"},
    {"title": "Ikigai", "author": "H\u00e9ctor Garc\u00eda", "price": 449, "category": "Self Development",
     "rating": 5, "badge": "New Arrival",
     "image": "https://images.unsplash.com/photo-1589998059171-988d887df646?auto=format&fit=crop&w=500&q=80"},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "price": 499, "category": "Business",
     "rating": 5, "badge": "Bestseller",
     "image": "https://images.unsplash.com/photo-1552581234-26160f608093?auto=format&fit=crop&w=500&q=80"},
    {"title": "Deep Work", "author": "Cal Newport", "price": 549, "category": "Self Development",
     "rating": 4, "badge": "Staff Pick",
     "image": "https://images.unsplash.com/photo-1495446815901-a7297e633e8d?auto=format&fit=crop&w=500&q=80"},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "price": 399, "category": "Business",
     "rating": 4, "badge": "Bestseller",
     "image": "https://images.unsplash.com/photo-1526243741027-444d633d7365?auto=format&fit=crop&w=500&q=80"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "price": 349, "category": "Business",
     "rating": 4, "badge": "Classic",
     "image": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=500&q=80"},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen Covey", "price": 699, "category": "Self Development",
     "rating": 5, "badge": "Reader Favourite",
     "image": "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=500&q=80"},
]

BEST_SELLERS = BOOKS[:6]

OFFER = {
    "eyebrow": "Book Lovers' Week",
    "headline": "20% off selected titles",
    "subtext": "Your next great read is waiting — the discount applies automatically when you order on WhatsApp.",
    "cta": "Shop The Offer",
    "ends_in_hours": 40,
}

AUTHOR_SPOTLIGHT = {
    "name": "James Clear",
    "role": "Author of Atomic Habits",
    "bio": (
        "James Clear writes about habits, decision-making and continuous "
        "improvement. His work distils behavioural science into practical, "
        "everyday steps — which is exactly why our readers keep coming back "
        "to his shelf."
    ),
    "quote": "Small habits can lead to remarkable results.",
    "image": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=700&q=80",
    "books": ["Atomic Habits", "The Habits Academy Journal"],
}

READING_BENEFITS = [
    {"icon": "bi-lightbulb", "title": "Expand Your Knowledge", "text": "Every book adds a room to the house of what you know."},
    {"icon": "bi-eye", "title": "Discover New Perspectives", "text": "See the world through eyes that aren't your own."},
    {"icon": "bi-bullseye", "title": "Improve Focus", "text": "A habit that trains your attention span, one page at a time."},
    {"icon": "bi-stars", "title": "Fuel Creativity", "text": "The best ideas often arrive by way of someone else's story."},
    {"icon": "bi-arrow-repeat", "title": "Build Better Habits", "text": "Reading nightly is one of the easiest habits worth keeping."},
]

WHY_CHOOSE_US = [
    {"icon": "bi-collection", "title": "Curated Collection", "text": "Carefully selected books, not warehouse overflow."},
    {"icon": "bi-chat-heart", "title": "Expert Recommendations", "text": "We help you find your next great read."},
    {"icon": "bi-whatsapp", "title": "Easy Ordering", "text": "Order through WhatsApp or phone in under a minute."},
    {"icon": "bi-truck", "title": "Fast Delivery", "text": "Books delivered safely, straight to your doorstep."},
    {"icon": "bi-gift", "title": "Gift Wrapping", "text": "Beautiful wrapping for every occasion, at no extra cost."},
    {"icon": "bi-people", "title": "Friendly Service", "text": "A bookstore that actually knows its readers by name."},
]

TESTIMONIALS = [
    {"name": "Priya Raman", "type": "Regular Reader", "rating": 5,
     "text": "I always find something interesting here. The staff recommendations are excellent, every single time.",
     "avatar": "https://randomuser.me/api/portraits/women/65.jpg"},
    {"name": "Arun Kumar", "type": "Book Lover", "rating": 5,
     "text": "Great collection, reasonable prices and very friendly service. My Saturday ritual now.",
     "avatar": "https://randomuser.me/api/portraits/men/41.jpg"},
    {"name": "Meena Suresh", "type": "Parent & Reader", "rating": 5,
     "text": "My favourite place to discover new books. The children's section is genuinely wonderful.",
     "avatar": "https://randomuser.me/api/portraits/women/33.jpg"},
    {"name": "Vignesh Rao", "type": "Student", "rating": 4,
     "text": "Found every exam-prep book I needed for a fraction of what I'd pay elsewhere.",
     "avatar": "https://randomuser.me/api/portraits/men/23.jpg"},
    {"name": "Divya Menon", "type": "Book Club Host", "rating": 5,
     "text": "We host our monthly book club here. The team always sets aside a quiet corner for us.",
     "avatar": "https://randomuser.me/api/portraits/women/76.jpg"},
]

GALLERY = [
    {"image": "https://images.unsplash.com/photo-1526243741027-444d633d7365?auto=format&fit=crop&w=600&q=80", "caption": "Floor-to-ceiling shelves"},
    {"image": "https://images.unsplash.com/photo-1521123845560-14093637aa7d?auto=format&fit=crop&w=600&q=80", "caption": "This week's new arrivals"},
    {"image": "https://images.unsplash.com/photo-1524578271613-d550eacf6090?auto=format&fit=crop&w=600&q=80", "caption": "Our reading corner"},
    {"image": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=600&q=80", "caption": "Readers browsing"},
    {"image": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=600&q=80", "caption": "Stacks worth getting lost in"},
 {
    "image": "https://cdn.shopify.com/s/files/1/0614/5776/0511/files/MS_Reading_Corner_1024x1024.jpg?v=1719603695",
    "caption": "The children's corner"
},
    {"image": "https://images.unsplash.com/photo-1490633874781-1c63cc424610?auto=format&fit=crop&w=600&q=80", "caption": "Author meet & greet"},
    {"image": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=600&q=80", "caption": "Inside Inkleaf"},
]

EVENTS = [
    {"title": "Author Meet & Greet", "date": "Saturday", "time": "6:00 PM",
     "description": "An evening with a bestselling local author, Q&A and signed copies.",
     "location": "Main Reading Hall"},
    {"title": "Book Club Night", "date": "Every Friday", "time": "5:30 PM",
     "description": "This month: The Psychology of Money. New readers always welcome.",
     "location": "The Reading Corner"},
    {"title": "Kids' Story Time", "date": "Sunday", "time": "11:00 AM",
     "description": "A read-aloud session for ages 4–8, with a craft table after.",
     "location": "Children's Section"},
]

DELIVERY = {
    "areas": ["Chennai", "Tambaram", "Velachery", "Medavakkam", "Pallikaranai", "Sholinganallur"],
    "same_day": "Same-day delivery available on orders placed before 4pm",
    "free_above": 999,
    "packing_note": "Every book is wrapped and cushioned before it leaves the store",
}

ENQUIRY_TOPICS = [
    ("book", "Book Enquiry"),
    ("bulk", "Bulk Book Order"),
    ("school", "School / College Books"),
    ("corporate", "Corporate Books"),
    ("gift", "Gift Books"),
    ("event", "Book Event"),
    ("visit", "Store Visit"),
    ("other", "Other"),
]
