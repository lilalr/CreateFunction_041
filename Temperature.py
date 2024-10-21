def convert_temperature(value, unit):
    if unit.upper() == 'C':
        converted_value = (value * 9/5) + 32
        return converted_value, 'F'
    elif unit.upper() == 'F':
        converted_value = (value - 32) * 5/9
        return converted_value, 'C'
    else:
        return ValueError("Temp Invalid")
    
temp = float(input("Masukan Temperatur : "))
unit = input("Pilih (F/C)")
final_result = convert_temperature(temp, unit)

print(final_result)