# -*- coding: utf-8 -*-


def mymin(*args, **kwargs):
    key = kwargs.get("key", None)

    if (len(kwargs) == 1) and ("key" in kwargs.keys()):
        # We have only the key in kwargs
        n_kwargs = 0
    else:
        if ("key" in kwargs.keys()):
            # We have key and more arguments is kwargs
            n_kwargs = len(kwargs)-1
            del kwargs["key"]
        else:
            # We don't have a key, but we have arguments in kwargs
            n_kwargs = len(kwargs)

    n_args = len(args)

    if (n_args + n_kwargs == 1) :
        # We have a single iterable
        if (n_args == 1):
            # Argument is in args
            if (type(args[0]) == type(x for x in range(1))) or (type(args[0]) == type(filter(str.isalpha,"@"))) or (type(args[0]) == type({1,2})):
                # Argument is a generator
                arg = list(args[0])
            else:
                arg = args[0]
            if (key is not None):
                arg = list(map(key, arg))
                minimum = arg[0]
                min_i = 0
                for x in range(len(arg)):
                    if (minimum > arg[x]):
                        minimum = arg[x]
                        min_i = x
                return args[0][min_i]

            minimum = arg[0]
            for x in arg:
                if (minimum > x):
                    minimum = x
        else:
            # Argument is in kwargs
            if (type(kwargs[list(kwargs.keys())[0]]) == type(x for x in range(1))) or (type(kwargs[list(kwargs.keys())[0]]) == type(filter(str.isalpha,"@"))) or (type(kwargs[list(kwargs.keys())[0]]) == type({1,2})):
                # Argument is a generator
                arg = list(kwargs[list(kwargs.keys())[0]])
            else:
                arg = kwargs[list(kwargs.keys())[0]]
            if (key is not None):
                arg = list(map(key, kwargs[list(kwargs.keys())[0]]))
                minimum = arg[0]
                min_i = 0
                for x in range(len(arg)):
                    if (minimum > arg[x]):
                        minimum = arg[x]
                        min_i = x
                return kwargs[list(kwargs.keys())[0]][min_i]
            else:
                arg = kwargs[list(kwargs.keys())[0]]
                minimum = arg[0]
                for x in arg:
                    if (minimum > x):
                        minimum = x
    else:
        # We have two or more  arguments
        if (key is not None):
            all_args = []
            if (n_args >= 1):
                foo_args = []
                for x in args:
                    if (type(x) == type(i for i in range(1))) or (type(x) == type(filter(str.isalpha,"@"))) or (type(x) == type({1,2})):
                        foo_args.append(list(x))
                    else:
                        foo_args.append(x)
                all_args += list(map(key, foo_args))
            if (n_kwargs >= 1):
                foo_kwargs = []
                for x in kwargs.values():
                    if (type(x) == type(i for i in range(1))) or (type(x) == type(filter(str.isalpha,"@"))) or (type(x) == type({1,2})):
                        foo_kwargs.append(list(x))
                    else:
                        foo_kwargs.append(x)
                all_args += list(map(key, foo_kwargs))
            minimum = all_args[0]
            min_i = 0
            for arg_i in range(len(all_args)):
                if (minimum > all_args[arg_i]):
                    minimum = all_args[arg_i]
                    min_i = arg_i
            if (min_i+1 > n_args):
                return foo_kwargs[min_i - n_args]
            else:
                return foo_args[min_i]
        else:
            all_args = []
            if (n_args >= 1):
                foo_args = []
                for x in args:
                    if (type(x) == type(i for i in range(1))) or (type(x) == type(filter(str.isalpha,"@"))) or (type(x) == type({1,2})):
                        foo_args += list(x)
                    else:
                        foo_args += [x]
                minimum = args[0]
                all_args += foo_args
            else:
                foo_args = []
                for x in kwargs.values():
                    if (type(x) == type(i for i in range(1))) or (type(x) == type(filter(str.isalpha,"@"))) or (type(x) == type({1,2})):
                        foo_args += list(x)
                    else:
                        foo_args += [x]
                minimum = kwargs[list(kwargs.keys())[0]]
                all_args += foo_args

            for arg in all_args:
                if (minimum > arg):
                    minimum = arg

    return minimum


def mymax(*args, **kwargs):
    key = kwargs.get("key", None)

    if (len(kwargs) == 1) and ("key" in kwargs.keys()):
        # We have only the key in kwargs
        n_kwargs = 0
    else:
        if ("key" in kwargs.keys()):
            # We have key and more arguments is kwargs
            n_kwargs = len(kwargs)-1
            del kwargs["key"]
        else:
            # We don't have a key, but we have arguments in kwargs
            n_kwargs = len(kwargs)

    n_args = len(args)

    if (n_args + n_kwargs == 1) :
        # We have a single iterable
        if (n_args == 1):
            # Argument is in args
            if (type(args[0]) == type(x for x in range(1))) or (type(args[0]) == type(filter(str.isalpha,"@"))) or (type(args[0]) == type({1,2})):
                # Argument is a generator
                arg = list(args[0])
            else:
                arg = args[0]
            if (key is not None):
                arg = list(map(key, arg))
                maximum = arg[0]
                max_i = 0
                for x in range(len(arg)):
                    if (maximum < arg[x]):
                        maximum = arg[x]
                        max_i = x
                return args[0][max_i]

            maximum = arg[0]
            for x in arg:
                if (maximum < x):
                    maximum = x
        else:
            # Argument is in kwargs
            if (type(kwargs[list(kwargs.keys())[0]]) == type(x for x in range(1))) or (type(kwargs[list(kwargs.keys())[0]]) == type(filter(str.isalpha,"@"))) or (type(kwargs[list(kwargs.keys())[0]]) == type({1,2})):
                # Argument is a generator
                arg = list(kwargs[list(kwargs.keys())[0]])
            else:
                arg = kwargs[list(kwargs.keys())[0]]
            if (key is not None):
                arg = list(map(key, kwargs[list(kwargs.keys())[0]]))
                maximum = arg[0]
                max_i = 0
                for x in range(len(arg)):
                    if (maximum < arg[x]):
                        maximum = arg[x]
                        max_i = x
                return kwargs[list(kwargs.keys())[0]][max_i]
            else:
                arg = kwargs[list(kwargs.keys())[0]]
                maximum = arg[0]
                for x in arg:
                    if (maximum < x):
                        maximum = x
    else:
        # We have two or more  arguments
        if (key is not None):
            all_args = []
            if (n_args >= 1):
                foo_args = []
                for x in args:
                    if (type(x) == type(i for i in range(1))) or (type(x) == type(filter(str.isalpha,"@"))) or (type(x) == type({1,2})):
                        foo_args.append(list(x))
                    else:
                        foo_args.append(x)
                all_args += list(map(key, foo_args))
            if (n_kwargs >= 1):
                foo_kwargs = []
                for x in kwargs.values():
                    if (type(x) == type(i for i in range(1))) or (type(x) == type(filter(str.isalpha,"@"))) or (type(x) == type({1,2})):
                        foo_kwargs.append(list(x))
                    else:
                        foo_kwargs.append(x)
                all_args += list(map(key, foo_kwargs))
            maximum = all_args[0]
            max_i = 0
            for arg_i in range(len(all_args)):
                if (maximum < all_args[arg_i]):
                    maximum = all_args[arg_i]
                    max_i = arg_i
            if (max_i+1 > n_args):
                return foo_kwargs[max_i - n_args]
            else:
                return foo_args[max_i]
        else:
            all_args = []
            if (n_args >= 1):
                foo_args = []
                for x in args:
                    if (type(x) == type(i for i in range(1))) or (type(x) == type(filter(str.isalpha,"@"))) or (type(x) == type({1,2})):
                        foo_args += list(x)
                    else:
                        foo_args += [x]
                maximum = args[0]
                all_args += foo_args
            else:
                foo_args = []
                for x in kwargs.values():
                    if (type(x) == type(i for i in range(1))) or (type(x) == type(filter(str.isalpha,"@"))) or (type(x) == type({1,2})):
                        foo_args += list(x)
                    else:
                        foo_args += [x]
                maximum = kwargs[list(kwargs.keys())[0]]
                all_args += foo_args

            for arg in all_args:
                if (maximum < arg):
                    maximum = arg

    return maximum

if __name__ == '__main__':
    #    print(mymin(a=[1,2,3,4,5, -8, 7]))
#    print(mymax([2,3], [5,2], argument1=[i-2 for i in range(2)], key=lambda x: x[1]))
#    print(mymax(2.2, 5.6, 5.9, key=int))
#    print(mymax(abs(i) for i in range(-10, 10)))
#    print(mymax(3, 2))
#    print(mymin(filter(str.isalpha,"@v$e56r5CY{]")))
    print(mymin({1, 2, 3, 4, -10}))