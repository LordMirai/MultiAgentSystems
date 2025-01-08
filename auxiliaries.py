from faker import Faker

from tools import Tools

fake = Faker()

greek_letters = [
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta',
    'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho',
    'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega'
]

"""
The Auxiliaries file is simply for setup and testing purposes.
It should not be considered part of the main project.
"""


# if not os.path.exists('files'):
#     os.mkdir('files')
# for letter in greek_letters:
#     with open(f'files/{letter}.txt', 'w') as file:
#         for _ in range(100):
#             file.write(fake.text() + '\n')

cmd = "<<SEARCH>> why"
print(Tools.parse(cmd))

cmd = "<<RANDCOLNUM>>"
print(Tools.parse(cmd))

cmd = "This is a test"
print(Tools.parse(cmd))

cmd = "<<DATETIME>>"
print(Tools.parse(cmd))

# cmd = "<<WRITE>> Hello, World!"
# print(Tools.parse(cmd))

cmd = "<<READLINE>> 51"
print(Tools.parse(cmd))

cmd = "<<EXIT>>"
print(Tools.parse(cmd))

print("EOF - not going to be run")
