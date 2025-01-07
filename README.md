# [PROJECT-04] Advanced Email Validation Program:
This Python project provides an advanced email address validation system that combines both regular expression (Regex) and DNS lookup techniques to ensure email addresses are both syntactically and domain-valid. The goal of this project is to ensure that an email adheres to the correct format, domain and syntax rules commonly used for email addresses.
1) Regex Validation: The first layer of validation checks the email address format based on a widely accepted regular expression pattern. This ensures that the email follows the correct syntax, such as proper characters before and after the "@" symbol, a valid domain name, and an appropriate domain extension (e.g., .com, .org).
2) DNS Lookup: Once the format is verified, the second layer performs a DNS query to ensure that the domain of the email address actually exists and has valid mail exchange (MX) records. This step confirms that the email domain is capable of receiving messages, adding an extra layer of confidence in the email's deliverability.

# Features:
1) SYNTAX VALIDATION: The project checks whether the email follows the standard structure, including a local part, an "@" symbol, and a domain part (i.e. username@domain.com).
2) DOMAIN VALIDATION: The system checks whether the domain part of the email corresponds to a real domain.
3) EMAIL FORMAT SUGGESTIONS: If the email address is invalid the system can provide suggestions for correcting common mistakes (i.e. Missing "@"; Incorrect Domain; or Invalid Characters.
4) USER-FRIENDLY INTERFACE: A simple and interactive command-line interface (CLI) is available to input Email Addresses, with clear success or error messages indicating the result of the validation check.
