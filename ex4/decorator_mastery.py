from functools import wraps
from time import time, sleep
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    '''
        #   Spell timer.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''
            #   Spell timer.
        '''
        print(f'Casting {func.__name__}...')
        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start
        print(f'Spell completed in {elapsed:.3f} seconds')
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    '''
        #   Power validator.
    '''
    def decorator(func: Callable) -> Callable:
        '''
            #   Power validator.
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''
                #   Power validator.
            '''
            if len(args) >= 3:
                power = args[2]
            elif len(args) >= 1:
                power = args[0]
            elif 'power' in kwargs:
                power = kwargs['power']
            else:
                return ('Insufficient power for this spell')
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return ('Insufficient power for this spell')
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    '''
        #   Retry spell.
    '''
    def decorator(func: Callable) -> Callable:
        '''
            #   Retry spell.
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''
                #   Retry spell.
            '''
            for attempt in range(1, max_attempts + 1):
                try:
                    return (func(*args, **kwargs))
                except Exception:
                    if attempt < max_attempts:
                        print('Spell failed, retrying... '
                              f'(attempt {attempt}/{max_attempts})')
                    else:
                        return (
                            'Spell casting failed after'
                            f'{max_attempts} attempts'
                        )
        return (wrapper)
    return (decorator)


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        '''
            #   Validate mage name.
        '''
        if len(name) < 3:
            return False
        return (all(c.isalpha() or c.isspace() for c in name))

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        '''
            #   Cast spell.
        '''
        return (f'Successfully cast {spell_name} with {power} power')


def main_exec() -> None:
    '''
        #   Main execution program.
    '''
    print('\nTesting spell timer...')

    @spell_timer
    def fireball():
        sleep(0.1)
        return 'Fireball cast!'

    result = fireball()

    print(f'Result: {result}')
    print('\nTesting MageGuild...')
    print(MageGuild.validate_mage_name('Merlin'))
    print(MageGuild.validate_mage_name('Az'))

    guild = MageGuild()

    print(guild.cast_spell('Lightning', 15))
    print(guild.cast_spell('Thunder', 5))


def main():
    '''
        #   Small main program.
    '''
    main_exec()


if (__name__ == '__main__'):
    main()
