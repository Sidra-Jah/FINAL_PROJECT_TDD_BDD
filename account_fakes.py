from factories import AccountFactory

def test_update_account(self):
    """Update an account"""
    account = AccountFactory
    account.create()

    #Fetcht it back
    account = Account.find(account.id)
    account.email = "vbdn@gbjj"
    account.update()

    #Fetch it back again
    account = Account.find(account.id)
    self.assertEqual(account.email,"vbdn@gbjj")