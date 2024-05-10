import stata_setup
stata_setup.config('C:/Program Files/Stata18', 'se')
from sfi import Data, Macro,  SFIToolkit, Frame, Datetime as dt

def load_stata(function):
    responses = function
    colnames = responses.columns
    Data.setObsTotal(len(responses))
    for i in range(len(colnames)):
        dtype = responses.dtypes[i].name
        print(dtype)
        # make a valid Stata variable name
        varname = SFIToolkit.makeVarName(colnames[i], retainCase=True)
        print(colnames[i])
        # varname = colnames[i]
        varval = responses[colnames[i]].values.tolist()
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
            price_dt_py = [dt.getSIF(j, '%tdCCYY-NN-DD') for j in responses[colnames[i]]]
            Data.store(varname, None, price_dt_py)
            Data.setVarFormat(varname, '%tdCCYY-NN-DD')
        else:
            # all other types store as a string
            Data.addVarStr(varname, 1)
            s = [str(i) for i in varval]
            Data.store(varname, None, s)
    return responses
