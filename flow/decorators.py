___author__ = 'Aram Koorn'

"""
make a logging decorator
"""


__author__ = "Aram Koorn"
__maintainer__ = "Aram Koorn"
__email__ = "aram.koorn@nielsen.com"
__status__ = "Development"


def logg(func):

    """

    :param func: function
    :return: Print logging statements of the function. Additionally loggings if output is a Pandas DataFrame.
    """
    def wrapper(*args, **kwargs):
        tic = datetime.datetime.now()


        retval = func(*args, **kwargs)
        toc = datetime.datetime.now()

        is_df = isinstance(retval, pd.DataFrame)

        # Check if output is a pandas dataframe
        if is_df:
            shape = retval.shape
            na_col = len(retval.loc[:, retval.isna().any()].columns)

        # print statement
        print(Fore.YELLOW + f'Function: {func.__name__} took: {(toc - tic).seconds} seconds')
        if is_df:
            print(f'Dataframe shape: {shape}')
            print(f'Nr. of columns with NA values: {na_col}')

        # Reset printing colors
        print(Fore.RESET)

        return retval

    return wrapper


if __name__ == '__main__':

    # Create random dataframe
    df = pd.DataFrame([[1, 1], [1, 1]], columns=['x', 'dd'])

    @logg
    def some_function(x):
        return x

    # Check if logging works with output DF
    some_function(x=df)

    # Output != pd.DataFrame
    some_function(x=2)