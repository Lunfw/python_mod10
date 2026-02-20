def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda x: x['power']))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'average_power':
            round(sum(mage['power'] for mage in mages) / len(mages), 2)
    }


def artifact_lib() -> list[dict]:
    '''
        #   Artifact library.
    '''
    return [
        {'name': 'Sword of Power', 'power': 100},
        {'name': 'Shield of Defense', 'power': 80},
        {'name': 'Staff of Magic', 'power': 120},
        {'name': 'Amulet of Luck', 'power': 60}
    ]


def mage_lib() -> list[dict]:
    '''
        #   Mage library.
    '''
    return [
        {'name': 'Mage of Fire', 'power': 150},
        {'name': 'Mage of Ice', 'power': 130},
        {'name': 'Mage of Wind', 'power': 110},
        {'name': 'Mage of Earth', 'power': 90}
    ]


def spell_lib() -> list[str]:
    '''
        #   Spell library.
    '''
    return ['fireball', 'heal', 'shield']


def main_exec():
    '''
        #   Main execution program.
    '''
    print('\nTesting artifact sorter...')
    print(f'{artifact_sorter(artifact_lib())}\n')

    print('Testing power filter...')
    print(f'{power_filter(mage_lib(), 130)}\n')

    print('Testing spell transformer...')
    print(f'{spell_transformer(spell_lib())}\n')

    print('Testing mage stats...')
    print(f'{mage_stats(mage_lib())}')


def main():
    '''
        #   Small main program.
    '''
    main_exec()


if (__name__ == '__main__'):
    main()
