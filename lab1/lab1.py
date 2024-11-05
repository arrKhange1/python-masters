zoo_creatures = { 
    'capibara': ['lama', 'japanese makaka'],
    'japanese makaka': ['goose', 'bober'],
    'goose': ['duck', 'japanese makaka', 'pavlin'],
    'duck': ['goose', 'flamingo'],
    'flamingo': ['spider', 'duck'],
    'spider': ['flamingo', 'fazan'],
    'fazan': ['spider', 'big panda'],
    'big panda': ['fazan', 'manul'],
    'manul': ['big panda', 'giraffe', 'bear-gubach', 'lil panda']
}

print(zoo_creatures['manul'])
print(zoo_creatures['duck'])