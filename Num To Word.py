from num2words import num2words

#Sayidan, numaraya cevirmek icin

def number_to_text(amount):
    # Split the amount into the integer and fractional part
    parts = str(amount).split('.')
    integer_part = int(parts[0])
    fractional_part = int(parts[1]) if len(parts) > 1 else 0
    
    # Convert the integer part to words and capitalize each word
    integer_part_text = num2words(integer_part, lang='en').replace('-', ' ').replace(',', '').title()
    
    # Convert the fractional part to words and format it
    fractional_part_text = f"{fractional_part:02d}/100"  # Ensure two decimal places
    
    # Replace 'And' after hundred and before tens with a comma
    integer_part_text = integer_part_text.replace(' And ', ' ')
    
    # Combine the parts with the currency and capitalize each word
    if fractional_part == 0:
        result = f"Saudi Riyals {integer_part_text} Only"
    else:
        result = f"Saudi Riyals {integer_part_text} And {fractional_part_text} Only"
    
    return result

# Example conversion
print(number_to_text("364525.86"))
