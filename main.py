import random
import string

def generate_random_email():
    # Generate a random username
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))

    # Generate a random domain
    domain_length = random.randint(5, 10)
    domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=domain_length))

    # Choose a random top-level domain
    top_level_domains = ['com', 'net', 'org', 'info', 'biz']
    top_level_domain = random.choice(top_level_domains)

    # Construct the email address
    email = f"{username}@{domain}.{top_level_domain}"

    return email

if __name__ == "__main__":
    random_email = generate_random_email()
    print("Random Email:", random_email)