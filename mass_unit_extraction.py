from extract import ExtractUnits

extractor = ExtractUnits()

questions = {
    "question_1": "How do I convert inches to centimeters?",
    "question_2": "How do I convert feet to meters?",
    "question_3": "How do I convert miles to kilometers?",
    "question_4": "How do I convert pounds to kilograms?",
    "question_5": "How do I convert gallons to liters?",
    "question_6": "How do I convert quarts to liters?",
    "question_7": "How do I convert cups to milliliters?",
    "question_8": "How do I convert ounces to grams?",
    "question_9": "How do I convert yards to meters?",
    "question_10": "How do I convert tons to kilograms?",
    "question_11": "How do I convert milliliters to liters?",
    "question_12": "How do I convert grams to kilograms?",
    "question_13": "How do I convert centimeters to inches?"
}

unit_pairs = {}

for key, q in questions.items():
    result = extractor(q)

    unit_pairs[key] = {
        "from_unit": result.from_unit,
        "to_unit": result.to_unit
    }

print(unit_pairs)
