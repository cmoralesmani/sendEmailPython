def get_contacts(
        filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])

    return names, emails
