def get_menu_option():
    return input("Option: ")

def get_conversion_input(valid_currencies):
    source_currency = input("Source Currency: ").upper()
    validate_currency(source_currency, valid_currencies)       
    
    target_currency = input("Target Currency: ").upper()
    validate_currency(target_currency, valid_currencies)  
    
    amount = float(input("Amount: "))
    
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
     
    return source_currency, target_currency, amount

def validate_currency(currency, valid_currencies):
    if currency not in valid_currencies:
        raise ValueError("INVALID currency")