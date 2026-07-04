USERS = [
    {
        "username": "alice",
        "role": "student",
        "mfa_enabled": True,
        "password_length": 14,
        "password_last_changed_days": 60,
        "breach_flag": False,
        "email": "alice@example.com",
    },
    {
        "username": "bob",
        "role": "student",
        "mfa_enabled": False,  # fails MFA
        "password_length": 16,
        "password_last_changed_days": 45,
        "breach_flag": False,
        "email": "bob@example.com",
    },
    {
        "username": "charlie",
        "role": "student",
        "mfa_enabled": True,
        "password_length": 10,  # fails length
        "password_last_changed_days": 20,
        "breach_flag": False,
        "email": "charlie@example.com",
    },
    {
        "username": "dina",
        "role": "student",
        "mfa_enabled": True,
        "password_length": 12,
        "password_last_changed_days": 240,  # fails password age
        "breach_flag": False,
        "email": "dina@example.com",
    },
    {
        "username": "eve",
        "role": "student",
        "mfa_enabled": True,
        "password_length": 18,
        "password_last_changed_days": 90,
        "breach_flag": True,  # fails breach
        "email": "eve@example.com",
    },
    {
        "username": "frank",
        "role": "staff",
        "mfa_enabled": False,  # fails MFA
        "password_length": 9,  # fails length
        "password_last_changed_days": 365,  # fails age
        "breach_flag": True,  # fails breach
        "email": "frank@example.com",
    },
    {
        "username": "grace",
        "role": "staff",
        "mfa_enabled": True,
        "password_length": 12,
        "password_last_changed_days": 170,
        "breach_flag": False,
        "email": "grace@example.com",
    },
    {
        "username": "heidi",
        "role": "staff",
        "mfa_enabled": True,
        "password_length": 22,
        "password_last_changed_days": 10,
        "breach_flag": False,
        "email": "heidi@example.com",
    },
    {
        "username": "ivan",
        "role": "admin",
        "mfa_enabled": True,
        "password_length": 12,
        "password_last_changed_days": 181,  # just over the limit (fails age)
        "breach_flag": False,
        "email": "ivan@example.com",
    },
    {
        "username": "judy",
        "role": "admin",
        "mfa_enabled": False,  # fails MFA
        "password_length": 20,
        "password_last_changed_days": 30,
        "breach_flag": False,
        "email": "judy@example.com",
    },
]
