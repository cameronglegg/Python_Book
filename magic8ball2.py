import random

messages = [
    'It is decided so.',
    'It is certain',
    'Yes! Definitely.',
    'Reply hazy, Try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is, No',
    'Outlook not so good...',
    'Very doubtfull'
]

print(messages[random.randint(0, len(messages) -1)])