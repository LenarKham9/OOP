from OOP import SavingsAccount


def test_savings_account_balance():
    account = SavingsAccount("Пользователь")
    account.deposit(500)
    account.withdraw(100)
    account.apply_interest()

    assert account.get_balance() > 0
    assert account.get_balance() == 420.0