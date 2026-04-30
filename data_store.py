# data_store.py

# Each key is a URL/Page Name
# 'links' are the edges to other nodes
MOCK_WEB = {
    "home": {
        "title": "Welcome Home",
        "content": "Landing page of the simulation.",
        "links": ["facebook", "google", "blog"]
    },
    "facebook": {
        "title": "Error",
        "h1": "Sorry, something went wrong.",
        "links": ["help", "home"]
    },
    "help": {
        "title": "Help Center",
        "content": "FAQs and support documentation.",
        "links": ["home"]
    },
    "google": {
        "title": "Search",
        "content": "World's information at your fingertips.",
        "links": ["gmail", "maps", "target_page"]
    },
    "gmail": {
        "title": "Inbox",
        "links": ["google"]
    },
    "maps": {
        "title": "World Map",
        "links": ["google"]
    },
    "blog": {
        "title": "Tech Insights",
        "links": ["home", "post_1"]
    },
    "post_1": {
        "title": "Search Algorithms 101",
        "links": ["blog", "target_page"]
    },
    "target_page": {
        "title": "Hidden Manuscript",
        "content": "You found the target!",
        "links": []
    }
}