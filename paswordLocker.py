#! python3
# an insecure password locker program

PASSWORDS = {'email': 'shdfikr3rfwkhef',
            'blog': 'fewgfefgwekjf',
            'luggage': 'fehwikfhwkf'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # second command line argument is the account name

if account in PASSWORDS.keys:
    pyperclip.copy(PASSWORDS[account])
else:
    print(f'There is no account named: {account}')
