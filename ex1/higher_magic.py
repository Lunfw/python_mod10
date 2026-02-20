from typing import Callable


def fspell() -> str | int:
    '''
        #   First spell.
    '''
    return ('Fireball hits Dragon', 10)


def sspell() -> str:
    '''
        #   Second spell.
    '''
    return ('Heals Dragon', 20)


def put_str(string: str) -> str:
    '''
        #   Format output.
    '''
    return (str)


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    '''
        #   Returns a function that combines the effects of two spells.
    '''
    def combined():
        return (str(spell1()[0]) + ', ' + str(spell2()[1]))
    return (combined)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    '''
        #   Returns a function that amplifies the power of a spell.
    '''
    def amplified():
        get_name: str = base_spell()[0].split(' ')[0].lower()
        return ('mega_' + str(get_name), base_spell()[1] * multiplier)
    return (amplified)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    '''
        #   Only casts if condition is met.
    '''
    def can_cast() -> str:
        if (not condition()):
            return ('Spell fizzled')
        return (spell)
    return (can_cast)


def spell_sequence(spells: list[Callable]) -> Callable:
    '''
        #   Returns a function that casts a sequence of spells.
    '''
    def sequence() -> list[str]:
        temp: list = []
        for i in spells:
            print(i())
            temp.append(i())
        return (temp)
    return (sequence)


def main_exec():
    '''
        #   Main execution program.
    '''
    print('\nTesting spell combined...')
    print(f'{spell_combiner(fspell, sspell)()}')

    print('\nTesting power amplifier...')
    print(f'Original: {fspell()[1]}, ', end='')
    print(f'Amplified: {power_amplifier(fspell, 3)()[1]}')

    print('\nTesting conditional caster...')
    print(f'{conditional_caster(lambda: False, fspell)()}')

    print('\nTesting spell sequence...')
    _: list = spell_sequence([fspell, sspell])()


def main():
    '''
        #   Small main program.
    '''
    main_exec()


if (__name__ == "__main__"):
    main()
