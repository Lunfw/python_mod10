from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from sys import exit, stderr
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    '''
        #   Reduces spell powers.
    '''
    c: int = 0
    try:
        c = reduce(operation_lib()[operation], spells)
    except KeyError:
        print('Error: Invalid operation, aborting.', file=stderr)
        exit(1)
    return c


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    '''
        #   Partial enchanter.
    '''
    return {
        'fire_enchant': partial(base_enchantment,
                                target='goblin', power=50, element='fire'),
        'ice_enchant': partial(base_enchantment,
                               target='goblin', power=50, element='ice'),
        'lightning_enchant':
            partial(base_enchantment,
                    target='goblin', power=50, element='lightning')
    }


@lru_cache
def memoized_fibonacci(n: int):
    '''
        #   Memoized fibonacci.
    '''
    if n < 2:
        return (n)
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable:
    '''
        #   Spell dispatcher.
    '''
    @singledispatch
    def cast_spell(spell) -> str:
        return (f'Cannot cast spell of type {type(spell).__name__}')

    @cast_spell.register(int)
    def _(spell: int) -> str:
        '''
            #   Cast spell of type int.
        '''
        if spell < 0:
            return ('Invalid damage value')
        elif spell < 50:
            return (f'Casting weak fireball: {spell} damage')
        else:
            return (f'Casting powerful meteor: {spell} damage')

    @cast_spell.register(str)
    def _(spell: str) -> str:
        '''
            #   Cast spell of type str.
        '''
        valid_enchantments = ['fire', 'ice', 'lightning', 'heal']
        if spell.lower() in valid_enchantments:
            return (f'Enchantment \'{spell}\' successfully applied')
        else:
            return (f'Unknown enchantment: {spell}')

    @cast_spell.register(list)
    def _(spell: list) -> str:
        '''
            #   Cast spell of type list.
        '''
        if not spell:
            return ('No spells to cast')
        results = []
        for i in spell:
            results.append(cast_spell(i))
        return (
                'Multi-cast complete:\n'
                + '\n'.join(
                  f'  - {r}' for r in results
                )
            )
    return (cast_spell)


def operation_lib() -> dict:
    '''
        #   Small lib to rec operations (Callable) and operations (str)
    '''
    temp: dict = {
        'add': add,
        'mul': mul,
        'max': max,
        'min': min
    }
    return (temp)


def reducer_exec() -> None:
    '''
        #   Reducer exec.
    '''
    spells: list[int] = [10, 20, 50, 25, 10]
    print(f'Sum: {spell_reducer(spells, "add")}')
    print(f'Product: {spell_reducer(spells, "mul")}')
    print(f'Max: {spell_reducer(spells, "max")}')


def partial_exec() -> None:
    '''
        #   Partial exec.
    '''
    x: Callable = partial_enchanter(base_enchantment)
    print(x['fire_enchant']())
    print(x['ice_enchant']())
    print(x['lightning_enchant']())


def spell_exec() -> None:
    '''
        #   Spell exec.
    '''
    x: Callable = spell_dispatcher()
    print(x(10))
    print(x('fire'))
    print(x([10, 20, 30]))


def base_enchantment(power: int, element: str, target: str) -> str:
    '''
        #   Base enchantment.
    '''
    return (f'{element} enchantment on {target} with power {power}')


def main_exec() -> None:
    '''
        #   Main execution program.
    '''
    print('\nTesting spell reducer...')
    reducer_exec()

    print('\nTesting partial partial enchanter...')
    partial_exec()

    print('\nTesting memoized fibonacci...')
    print(f'Fib(10): {memoized_fibonacci(10)}')
    print(f'Fib(15): {memoized_fibonacci(15)}')

    print('\nTesting spell dispatcher...')
    spell_exec()


def main() -> None:
    main_exec()


if (__name__ == '__main__'):
    main()
