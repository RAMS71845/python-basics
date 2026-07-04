raw="    softpro school of ai LAUNCHES new 45-day ai program!!!    "
print(f"{raw.strip().replace("!!!", "").title()}")

print(f"{len(raw)-len(raw.strip().replace("!!!", "").title())}")