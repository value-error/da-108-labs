def get_temperature():
    while True:
        try:
            s = input("Enter temperature: ")
            s = s.strip().lower()

            if s[-1] not in ('c', 'f'):
                raise ValueError("invalid temperature")
            
            return float(s[:-1]), s[-1]
        except ValueError:
            print("error: invalid temperature")
            print("enter values of the form 32c, 32.0f etc.\n")

value, unit = get_temperature()

if unit == 'c':
    converted_value = value * 1.8 + 32
    print("%.1f\u00b0 C = %.1f\u00b0 F" % (value, converted_value))
else:
    converted_value = (value - 32) / 1.8
    print("%.1f\u00b0 F = %.1f\u00b0 C" % (value, converted_value))
