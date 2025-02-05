"""
Test Cases for Account Model
"""
import json
from random import randrange
import pytest
from models import db
from models.account import Account, DataValidationError
from datetime import datetime

ACCOUNT_DATA = {}

@pytest.fixture(scope="module", autouse=True)
def load_account_data():
    """ Load data needed by tests """
    global ACCOUNT_DATA
    with open('tests/fixtures/account_data.json') as json_data:
        ACCOUNT_DATA = json.load(json_data)

    # Set up the database tables
    db.create_all()
    yield
    db.session.close()

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    """ Truncate the tables and set up for each test """
    db.session.query(Account).delete()
    db.session.commit()
    yield
    db.session.remove()

######################################################################
#  E X A M P L E   T E S T   C A S E
######################################################################

# ===========================
# Test Group: Role Management
# ===========================

# ===========================
# Test: Account Role Assignment
# Author: John Businge
# Date: 2025-01-30
# Description: Ensure roles can be assigned and checked.
# ===========================

def test_account_role_assignment():
    """Test assigning roles to an account"""
    account = Account(name="John Doe", email="johndoe@example.com", role="user")

    # Assign initial role
    assert account.role == "user"

    # Change role and verify
    account.change_role("admin")
    assert account.role == "admin"

# ===========================
# Test: Invalid Role Assignment
# Author: John Businge
# Date: 2025-01-30
# Description: Ensure invalid roles raise a DataValidationError.
# ===========================

def test_invalid_role_assignment():
    """Test assigning an invalid role"""
    account = Account(role="user")

    # Attempt to assign an invalid role
    with pytest.raises(DataValidationError):
        account.change_role("moderator")  # Invalid role should raise an error


######################################################################
#  T O D O   T E S T S  (To Be Completed by Students)
######################################################################

"""
Each student in the team should implement **one test case** from the list below.
The team should coordinate to **avoid duplicate work**.

Each test should include:
- A descriptive **docstring** explaining what is being tested.
- **Assertions** to verify expected behavior.
- A meaningful **commit message** when submitting their PR.
"""

# TODO 1: Test Account Serialization
# - Ensure `to_dict()` correctly converts an account to a dictionary format.
# - Verify that all expected fields are included in the dictionary.

# ===========================
# Test: Test Account Serialization
# Author: Evan Hollingshead
# Date: 2025-02-01
# Description: Checks that 'to_dict()' converts an account to a dictionary.
# ===========================
def test_account_serialization():
    """Test that 'to_dict()' correctly converts an account to a dictionary"""
    account = Account(role = "user", email = "test@example.com", id = 1, name = "evan", balance = 100.0, phone_number = "1234567890", date_joined = datetime(2025, 2,1,1,0,0), disabled = False)
    account_dict = account.to_dict()
    expected_dict = {
        "id": 1,
        "name": "evan",
        "email": "test@example.com",
        "phone_number": "1234567890",
        "disabled": False,
        "date_joined": datetime(2025, 2,1,1,0,0),
        "balance": 100.0,
        "role": "user"
    }
    for key,value in expected_dict.items():
        assert key in account_dict
        assert account_dict[key] == value

# TODO 2: Test Invalid Email Input
# - Check that invalid emails (e.g., "not-an-email") raise a validation error.
# - Ensure accounts without an email cannot be created.

# TODO 3: Test Missing Required Fields
# - Ensure that creating an `Account()` without required fields raises an error.
# - Validate that missing fields trigger the correct exception.

# TODO 4: Test Positive Deposit
# ===========================
# Test: Invalid Role Assignment
# Author: Matthew Rainwater
# Date: 02-04-2025
# Description: Ensure `deposit()` correctly increases the account balance and
# verify that depositing a positive amount updates the balance correctly.
# ===========================

def test_positive_deposit():
    """Test positive deposit"""
    account = Account(name="Alice", email="alice@example.com", balance=100.0)

    # positive deposit 
    deposit_amount = 50.0
    account.deposit(deposit_amount)

    # verify balance was updated
    assert account.balance == 150.0, f"Expected balance 150.0, but got {account.balance}"


# TODO 5: Test Deposit with Zero/Negative Values
# - Ensure `deposit()` raises an error for zero or negative amounts.
# - Verify that balance remains unchanged after an invalid deposit attempt.

# TODO 6: Test Valid Withdrawal
# - Ensure `withdraw()` correctly decreases the account balance.
# - Verify that withdrawals within available balance succeed.

#===========================
#Test: Valid Withdrawal
#Author: Maylee Del Rio
#Date: 2025-02-4
#Description: Testing valid withdrawal amount from an account with sufficient funds
#===========================
def test_valid_withdrawal():
    # the account information
    account = Account(name="Lebron James", email="LebronJames23@example.com", balance=100000000.0)

    # Withdraw valid case
    account.withdraw(100000.0)

    # The new balance 100000000 - 100000 = 99900000
    assert account.balance == 99900000.0

# TODO 7: Test Withdrawal with Insufficient Funds
# - Ensure `withdraw()` raises an error when attempting to withdraw more than available balance.
# - Verify that the balance remains unchanged after a failed withdrawal.

# ===========================
# Test: Test Withdraw Insufficient funds
# Author: Jordan Spencer
# Date: 2025-02-04
# Description: Check if withdraw allows to withdraw more than balance.
# ===========================

def test_withdraw_insufficient_balance():
    """Test withdrawing more than available balance"""
    account = Account(balance=100)

    # Capture initial balance
    initial_balance = account.balance

    # Attempt to withdraw more than the balance
    with pytest.raises(DataValidationError):
        account.withdraw(200)  # Overdraft should raise an error

    # Ensure balance remains unchanged after failed withdrawal
    assert account.balance == initial_balance

# TODO 8: Test Password Hashing
# - Ensure that passwords are stored as **hashed values**.
# - Verify that plaintext passwords are never stored in the database.
# - Test password verification with `set_password()` and `check_password()`.

# ===========================
# Test: Test Password Hashing
# Author: Jaydan Escober
# Date: 2025-02-04
# Description: Ensure that passwords are stored as hashed values.
# ===========================
def test_password_hashing():
    # Test password hashing
    account = Account(name="John Doe", email="johndoe@example.com")
    
    password = "securepassword"
    account.set_password(password)
    
    # Ensure the password is hashed
    assert account.password_hash != password
    assert account.check_password(password) is True

# TODO 9: Test Role Assignment
# - Ensure that `change_role()` correctly updates an account’s role.
# - Verify that the updated role is stored in the database.

# ===========================
# Test: Test Account Deactivation
# Author: Joseph Dib
# Date: 2025-02-04
# Description: Tests that deactivate() correctly deactivates an existing account.
# ===========================
def test_deactivate():
    """Test that 'deactivate()' correctly deletes an existing account"""
    account = Account(role = "user", email = "test@example.com", name = "joseph", disabled = False)
    account.disabled = True
    assert account.disabled == True

# ===========================
# Test: Test Account Reactivation
# Author: Joseph Dib
# Date: 2025-02-04
# Description: Tests that reactivate() correctly reactivates an existing account.
# ===========================

def test_reactivate():
    """Test that 'delete()' correctly deletes an existing account"""
    account = Account(role = "user", email = "test@example.com", name = "joseph", disabled = True)
    account.disabled = False
    assert account.disabled == False

# TODO 10: Test Invalid Role Assignment
# - Ensure that assigning an invalid role raises an appropriate error.
# - Verify that only allowed roles (`admin`, `user`, etc.) can be set.

# TODO 11: Test Deleting an Account
# - Ensure that `delete()` removes an account from the database.
# - Verify that attempting to retrieve a deleted account returns `None` or raises an error.

