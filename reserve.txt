# data_store.py

MOCK_WEB = {
    "https://www.cyberspace.com": {
        "title": "Main Frame",
        "links": ["https://www.cyberspace.com/network", "https://social.meta.com", "https://dev.blog.io"]
    },
    "https://social.meta.com": {
        "title": "Social Gateway",
        "links": ["https://social.meta.com/error_404", "https://www.cyberspace.com"]
    },
    "https://social.meta.com/error_404": {
        "title": "Access Denied",
        "links": ["https://social.meta.com/help", "https://www.cyberspace.com"]
    },
    "https://social.meta.com/help": {
        "title": "Support Terminal",
        "links": ["https://www.cyberspace.com"]
    },
    "https://dev.blog.io": {
        "title": "Dev Logs",
        "links": ["https://dev.blog.io/search_algos", "https://www.cyberspace.com"]
    },
    "https://dev.blog.io/search_algos": {
        "title": "Target Found",
        "links": [] # The goal node
    }
}