def get_menu_option():
    return input("Option: ")

def get_conversion_input(validate_currency):

    source_currency = input("Source Currency: ").upper()
    is_valid_currency(validate_currency(source_currency))     
    
    target_currency = input("Target Currency: ").upper()
    is_valid_currency(validate_currency(target_currency))     
    
    try:
        amount = float(input("Amount: "))
    except ValueError:
        raise ValueError("Please enter a valid amount.")
    
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
     
    return source_currency, target_currency, amount

def is_valid_currency(isValid):
    if not isValid: raise ValueError("INVALID Currency")

2