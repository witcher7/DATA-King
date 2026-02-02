from copy import deepcopy

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)
print(info_deepcopy)
print(id(info_deepcopy), id(info))

info_deepcopy['reviews'].append('Great course!')
info['reviews'].append('Thanks!')
print(id(info['reviews']), id(info_deepcopy['reviews']))

print(info)
print(info_deepcopy)
