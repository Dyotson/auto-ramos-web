from .assets import alphabet
import numpy as np


def solve_captcha(captcha***REMOVED*** -> str:
    ***REMOVED***
    Solves the captcha.
    ***REMOVED***
    solutions_list = [***REMOVED***
    for key, symbol in alphabet.items(***REMOVED***:
        for i in range(captcha.shape[0***REMOVED*** - symbol.shape[0***REMOVED***:
            for j in range(captcha.shape[1***REMOVED*** - symbol.shape[1***REMOVED***:
                captcha_subset = captcha[i:symbol.shape[0***REMOVED*** + i, j:symbol.shape[1***REMOVED*** + j***REMOVED***
                if np.array_equal(captcha_subset, symbol***REMOVED***:
                    # print(f"FOUND! {i***REMOVED*** {j***REMOVED***"***REMOVED***
                    solutions_list.append((key[0***REMOVED***, j***REMOVED***
                    if len(solutions_list***REMOVED*** == 4:
                        return f"{''.join([y[0***REMOVED*** for y in sorted(solutions_list, key=lambda x: x[1***REMOVED******REMOVED******REMOVED***"
    return f"{''.join([y[0***REMOVED*** for y in sorted(solutions_list, key=lambda x: x[1***REMOVED******REMOVED******REMOVED***"


def write_failed(path, captcha, solution***REMOVED***:
    ***REMOVED***
    Writes the failed captcha to a file.
    ***REMOVED***
    with open(path, "a"***REMOVED*** as file:
        print(f"{captcha***REMOVED***: {solution***REMOVED***", file=file***REMOVED***
