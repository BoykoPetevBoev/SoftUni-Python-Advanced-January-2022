class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def is_domain_valid(domain, valid_domains):
    is_valid = True
    for current_domain in valid_domains:
        if domain.endswith(current_domain):
            is_valid = False

    return is_valid

valid_domains = ['.com', '.bg', '.net', '.org']

while True:
    email = input()
    if email == 'End':
        break
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split('@')

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if is_domain_valid(domain, valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
