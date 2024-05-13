import stata_setup

try:
    stata_setup.config('C:/Program Files/Stata18', 'se')
    from sfi import Data, Macro,  SFIToolkit, Frame, Datetime as dt
except OSError:
    print("Stata executable not found. Please install Stata and add it to your PATH.")

def test_load_stata(df):
    print(df.head())

def load_stata(df):
    """
    Loads a Pandas DataFrame into a Stata data file format.
    
    Args:
        df (pandas.DataFrame): The DataFrame to be loaded into Stata format.
    
    Returns:
        pandas.DataFrame: The original DataFrame.
    """
    colnames = df.columns
    Data.setObsTotal(len(df))
    for i in range(len(colnames)):
        dtype = df.dtypes[i].name
        print(dtype)
        # make a valid Stata variable name
        varname = SFIToolkit.makeVarName(colnames[i], retainCase=True)
        print(colnames[i])
        # varname = colnames[i]
        varval = df[colnames[i]].values.tolist()
        if dtype == "int64":
            Data.addVarInt(varname)
            Data.store(varname, None, varval)
        elif dtype == "float64":
            Data.addVarDouble(varname)
            Data.store(varname, None, varval)
        elif dtype == "bool":
            Data.addVarByte(varname)
            Data.store(varname, None, varval)
        elif dtype == "datetime64[ns]":
            Data.addVarFloat(varname)
            price_dt_py = [dt.getSIF(j, '%tdCCYY-NN-DD') for j in df[colnames[i]]]
            Data.store(varname, None, price_dt_py)
            Data.setVarFormat(varname, '%tdCCYY-NN-DD')
        else:
            # all other types store as a string
            Data.addVarStr(varname, 1)
            s = [str(i) for i in varval]
            Data.store(varname, None, s)
    return df


if __name__ == "__main__":
    pass