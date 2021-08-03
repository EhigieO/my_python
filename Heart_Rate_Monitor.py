print('|{:<5s}|{:^6s}|{:>6s}|'.format('-----', '------', '------'))
print('|{:<5s}|{:^6s}|{:>6s}|'.format('n', 'n^2', 'n^3'))
print('|{:<5s}|{:^6s}|{:>6s}|'.format('-----', '------', '------'))
for i in range(15):
    print('|{:<5d}|{:^6d}|{:>6d}|'.format(i, i ** 2, i ** 3))

print('|{:<5s}|{:^6s}|{:>6s}|'.format('-----', '------', '------'))

print(list(range(10)))

names = ['james', 'bola', 'tinubu', 'ade', 'oshoma', 'lateef']
for index, name in enumerate(names):

    print(index, name)


