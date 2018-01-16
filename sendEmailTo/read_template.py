from string import Template


def read_template(
        filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()

    return Template(template_file_content)
