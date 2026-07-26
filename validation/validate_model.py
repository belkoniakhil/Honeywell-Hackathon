from validation.model_validation import ModelValidator
from validation.validation_report import ValidationReport

validator = ModelValidator()

results = validator.validate()

csv_path = validator.export_csv(results)

report_path = ValidationReport().generate(results)

print("\nValidation Completed\n")

print(f"CSV    : {csv_path}")
print(f"Report : {report_path}")