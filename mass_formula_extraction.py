from extract import ask_formula   # you already have this

formulas = {}   # store results here

unit_pairs = {
    'question_1': {'from_unit': 'inches', 'to_unit': 'centimeters'},
    'question_2': {'from_unit': 'feet', 'to_unit': 'meters'},
    'question_3': {'from_unit': 'miles', 'to_unit': 'kilometers'},
    'question_4': {'from_unit': 'pounds', 'to_unit': 'kilograms'},
    'question_5': {'from_unit': 'gallons', 'to_unit': 'liters'},
    'question_6': {'from_unit': 'quarts', 'to_unit': 'liters'},
    'question_7': {'from_unit': 'cups', 'to_unit': 'milliliters'},
    'question_8': {'from_unit': 'ounces', 'to_unit': 'grams'}
}

for key, pair in unit_pairs.items():
    from_unit = pair["from_unit"]
    to_unit = pair["to_unit"]

    result = ask_formula(from_unit=from_unit, to_unit=to_unit)

    # result.formula is the clean string
    formulas[key] = {
        "from_unit": from_unit,
        "to_unit": to_unit,
        "formula": result.formula
    }

print(formulas)
