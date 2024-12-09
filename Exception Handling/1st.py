# Custom Exception
class InvalidVoterException(Exception):
    pass

# Function to check voting eligibility
def check_voter_eligibility(age):
    try:
        if age < 18:
            raise InvalidVoterException("Age is less than 18. Not eligible to vote.")
        print("Eligible to vote!")
    except InvalidVoterException as e:
        print(f"Exception: {e}")

# Example Usage
age = int(input("Enter your age: "))
check_voter_eligibility(age)
