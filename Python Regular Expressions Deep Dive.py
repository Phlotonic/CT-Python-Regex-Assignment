import re

# Sample text containing email addresses
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Define the domain to exclude
exclude_domain = "exclude.com"

# Regular expression pattern to match email addresses
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

# Find all email addresses in the text
emails = re.findall(pattern, text)

# Filter out email addresses from the excluded domain
filtered_emails = [email for email in emails if not email.endswith(f"@{exclude_domain}")]

# Print the extracted email addresses
print(filtered_emails)


