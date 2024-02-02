from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
pattern_name = r'\w+'

email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if len(email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    if findall(pattern_name, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores")

    print("Email is valid")

    email = input()