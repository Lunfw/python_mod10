from typing import Callable


def mage_counter() -> Callable:
    '''
        #   Counter function.
    '''
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return (count)
    return (counter)


def spell_accumulator(initial_power: int) -> Callable:
    '''
        #   Accumulator function.
    '''
    power = initial_power

    def accumulator() -> int:
        nonlocal power
        power += initial_power
        return (power)
    return (accumulator)


def enchantment_factory(enchantment_type: str) -> Callable:
    '''
        #   Enchantment function.
    '''

    def enchantment() -> str:
        temp: str = (
            enchantment_type.split()[0] + ' ' + enchantment_type.split()[1]
        )
        return (temp)
    return (enchantment)


def memory_vault() -> dict[str, Callable]:
    '''
        #   Memory vault function.
    '''
    lib: dict = {}

    def store(key: str, value: Callable) -> None:
        lib[key] = value

    def recall(key: str) -> Callable:
        try:
            _ = lib[key]
            return (lib[key])
        except KeyError:
            raise KeyError('Memory not found')
    return (lib)


def counter_exec() -> None:
    '''
        #   Counter exec.
    '''
    f: Callable = mage_counter()
    for i in range(1, 4):
        print(f'Call {i}: {f()}')


def acc_exec() -> None:
    '''
        #   Accumulator exec.
    '''
    acc: Callable = spell_accumulator(5)
    for i in range(1, 4):
        print(f'Call {i}: {acc()}')


def enchant_exec(mats: tuple) -> None:
    '''
        #   Enchantment exec.
    '''
    for i in mats:
        en: Callable = enchantment_factory(i)
        print(f'{en()}')


def memory_exec() -> None:
    '''
        #   Memory exec.
    '''
    vault: dict[str, Callable] = memory_vault()
    vault['counter'] = counter_exec
    vault['accumulator'] = acc_exec
    for i, j in vault.items():
        print(f'{i}: {j}')


def main_exec() -> None:
    '''
        #   Main execution program.
    '''
    print('\nTesting mage counter...')
    counter_exec()

    print('\nTesting spell accumulator...')
    acc_exec()

    print('\nTesting enchantment factory...')
    temp: tuple = ('Flaming Sword', 'Frozen Shield')
    enchant_exec(temp)

    print('\nTesting memory vault...')
    memory_exec()


def main() -> None:
    '''
        #   Small main program.
    '''
    main_exec()


if (__name__ == '__main__'):
    main()
