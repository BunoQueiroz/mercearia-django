import re

def non_numeric_field(field, field_name, list):
    if any(char.isdigit() for char in field):
        list[field_name] = 'Este campo não aceita números'

"""def email_valid(field, field_name, list):
    pattern = "[a-zA-Z.0-9]{1-20}" #type: ignore
    pattern_valid = re.findall(pattern, field)
    if not pattern_valid:
        list[field_name] = 'Email Inválido'"""

def phone_valid(field, field_name, list):
    pattern = '[0-9]{2}9[0-9]{8}'
    pattern_valid = re.findall(pattern, field)
    if not pattern_valid:
        list[field_name] = 'O número de telefone deve seguir o seguinte formato: (00900000000)'

def message_valid(field, field_name, list):
    if len(field) < 10:
        list[field_name] = 'Sua mensagem é muito pequena. Por favor, explique-se melhor'
