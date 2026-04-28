# data_store.py

MOCK_WEB = {
    # --- SECTOR 01: MAIN INFRASTRUCTURE ---
    "https://www.cyberspace.com": {
        "title": "Main Frame",
        "links": [
            "https://www.cyberspace.com/network", 
            "https://social.meta.com", 
            "https://dev.blog.io",
            "https://archive.org/vault",
            "https://security.defense.gov" # New link
        ]
    },
    "https://www.cyberspace.com/network": {
        "title": "Network Topology",
        "links": ["https://www.cyberspace.com/firewall", "https://www.cyberspace.com/status"]
    },
    "https://www.cyberspace.com/firewall": {
        "title": "Security Layer",
        "links": ["https://www.cyberspace.com"]
    },
    "https://www.cyberspace.com/status": {
        "title": "System Status",
        "links": ["https://www.cyberspace.com/network"]
    },

    # --- SECTOR 02: SOCIAL CLUSTER (Cycles & Loops) ---
    "https://social.meta.com": {
        "title": "Social Gateway",
        "links": ["https://social.meta.com/profile/user01", "https://social.meta.com/error_404"]
    },
    "https://social.meta.com/profile/user01": {
        "title": "User Profile",
        "links": ["https://social.meta.com/profile/user01/friends", "https://social.meta.com/profile/user01/photos"]
    },
    "https://social.meta.com/profile/user01/friends": {
        "title": "Friend List",
        "links": ["https://social.meta.com/profile/user02", "https://social.meta.com/profile/user03"]
    },
    "https://social.meta.com/profile/user02": {
        "title": "Friend Profile 2",
        "links": ["https://social.meta.com/profile/user01"]
    },
    "https://social.meta.com/profile/user03": {
        "title": "Friend Profile 3",
        "links": ["https://social.meta.com/profile/user01"]
    },
    "https://social.meta.com/error_404": {
        "title": "Access Denied",
        "links": ["https://social.meta.com/help", "https://www.cyberspace.com"]
    },
    "https://social.meta.com/help": {
        "title": "Support Terminal",
        "links": ["https://www.cyberspace.com"]
    },

    # --- SECTOR 03: DEVELOPMENT & RESEARCH ---
    "https://dev.blog.io": {
        "title": "Dev Logs",
        "links": ["https://dev.blog.io/search_algos", "https://dev.blog.io/security_updates"]
    },
    "https://dev.blog.io/search_algos": {
        "title": "Algorithm Research",
        "links": ["https://dev.blog.io/search_algos/pathfinding", "https://dev.blog.io/target_node"]
    },
    "https://dev.blog.io/search_algos/pathfinding": {
        "title": "Pathfinding Details",
        "links": ["https://dev.blog.io/search_algos"]
    },
    "https://dev.blog.io/security_updates": {
        "title": "Security News",
        "links": ["https://www.cyberspace.com/firewall"]
    },
    "https://dev.blog.io/target_node": {
        "title": "TARGET_FOUND",
        "links": [] 
    },

    # --- SECTOR 04: GOVERNMENT DEFENSE (New Deep Data) ---
    "https://security.defense.gov": {
        "title": "Defense Portal",
        "links": ["https://security.defense.gov/classified", "https://security.defense.gov/public_records"]
    },
    "https://security.defense.gov/classified": {
        "title": "Classified Files",
        "links": ["https://security.defense.gov/classified/top_secret"]
    },
    "https://security.defense.gov/classified/top_secret": {
        "title": "Encrypted Vault",
        "links": ["https://dev.blog.io/target_node"] # Another way to reach the target
    },
    "https://security.defense.gov/public_records": {
        "title": "Public Archives",
        "links": ["https://archive.org/vault"]
    },

    # --- SECTOR 05: GLOBAL ARCHIVE ---
    "https://archive.org/vault": {
        "title": "Data Vault",
        "links": ["https://archive.org/vault/historical", "https://archive.org/vault/backups"]
    },
    "https://archive.org/vault/historical": {
        "title": "History Index",
        "links": ["https://archive.org/vault"]
    },
    "https://archive.org/vault/backups": {
        "title": "Backup Files",
        "links": ["https://archive.org/vault"]
    }
}