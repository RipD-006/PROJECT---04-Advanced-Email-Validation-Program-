import re
import dns.resolver


def is_valid_email(email):
    # Basic regex pattern for email syntax validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check syntax using regex
    if not re.match(pattern, email):
        return False, "Invalid email syntax."

    # Extract domain part of the email
    domain = email.split('@')[1].lower()  # Convert domain to lowercase for DNS lookup

    # Check if domain has valid MX records
    try:
        # Try resolving MX records for the domain
        dns.resolver.resolve(domain, 'MX')
        return True, "Valid email address."
    except dns.resolver.NoAnswer:
        return False, "Domain exists, but no mail exchange records (MX) found."
    except dns.resolver.NXDOMAIN:
        return False, "Domain does not exist."
    except dns.resolver.Timeout:
        return False, "DNS query timed out. Try again later."
    except Exception as e:
        # Catch any other unexpected errors
        return False, f"An error occurred: {str(e)}"


# Example usage
email = "test@example.com"
valid, message = is_valid_email(email)
print(f"Validation result for '{email}': {valid}, Message: {message}")