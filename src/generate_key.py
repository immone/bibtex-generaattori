import secrets

def generate_key_if_not_exist(filename):
    # Create file
    open(filename, 'a').close()
    # Check for existing key
    has_secret_key = False
    with open(filename) as env_file:
        for line in env_file:
            if line.startswith("SECRET_KEY"):
                has_secret_key = True

    if not has_secret_key:
        # Generate key and write to file
        with open(filename, "a") as env_file:
            env_file.write(f"SECRET_KEY={secrets.token_hex(32)}")
