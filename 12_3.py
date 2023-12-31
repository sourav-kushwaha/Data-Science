# Assume you have a list of association rules with confidence and lift
association_rules = [
    {'antecedents': {'Wafer'}, 'consequents': {'Bread'}, 'confidence': 1.0, 'lift': 1.5},
    {'antecedents': {'Milk'}, 'consequents': {'Saffron'}, 'confidence': 0.8, 'lift': 1.2},
    # Add more rules as needed
]

# Apply Confidence Quotient Criterion
for rule in association_rules:
    confidence_quotient = rule['confidence'] * rule['lift']
    rule['confidence_quotient'] = confidence_quotient

# Sort rules by Confidence Quotient
sorted_rules = sorted(association_rules, key=lambda x: x['confidence_quotient'], reverse=True)

# Print sorted rules
for rule in sorted_rules:
    print(f"Antecedents: {rule['antecedents']} --> Consequents: {rule['consequents']}")
    print(f"Confidence: {rule['confidence']:.3f}, Lift: {rule['lift']:.3f}")
    print(f"Confidence Quotient: {rule['confidence_quotient']:.3f}")
    print(20 * "-")
