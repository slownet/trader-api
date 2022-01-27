# Shamelessly stolen from the StackOverflow: https://stackoverflow.com/a/64778375

from dataclasses import asdict as std_asdict


def asdict(obj):
    return {**std_asdict(obj),
            **{a: getattr(obj, a) for a in getattr(obj, '__add_to_dict__', [])}}
