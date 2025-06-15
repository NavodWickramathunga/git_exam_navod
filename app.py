def greet_user(name):
    """A dummy function to greet a user with input validation."""
    if not name or name.strip() == "":
        return "Error: Name cannot be empty or None."
    return f"Hello, {name.strip()}! Welcome to the app."

