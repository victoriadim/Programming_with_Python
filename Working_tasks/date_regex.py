import re

email = """Hi, 
my name is Jane and my phone number is 555-123-4567. 
My email address is jane_doe@example.com. 
I live on 123 Main St. Apt. #456, and I was born on January 11th, 1990. I have an appointment on 2023-05-15 at 2:30pm at 789 Oak Ln. #3 and backup on 2023/05/21. 
Please give me a call or send me an email to confirm. In case the dates are unavailable, please set up a meeting sometime in June. I would love June 19h.
Thank you!"""
pattern = r"([0-9]{1,4}\/[0-9]{2}\/[0-9]{2})|([0-9]{1,4}-[0-9]{2}-[0-9]{2})|([A-Z][a-z]+ [0-9]{1,2}[a-z]{2}, [0-9]{1,4})"
extracted_dates = re.findall(pattern, email)
for extracted_date in extracted_dates:
    cleaned_date = [date for date in extracted_date if date][0]
    print(cleaned_date)