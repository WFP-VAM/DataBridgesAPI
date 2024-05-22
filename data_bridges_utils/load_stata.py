import stata_setup


class DataBridgesStata:
    """
    Retrieves data using the specified Stata installation.
    Load the data from python into Stata active dataframe (requires clearing data).
    Adapts the data type to the types recognized in Stata.
    """
    def __init__(self, stata_path, stata_edition):
        valid = {'se', 'mp', 'be'}
        if stata_edition not in valid:
            raise ValueError("stata_edition: edition must be one of '%s'" % valid)
        try:
            self.configuration = stata_setup.config(stata_path, stata_edition)
            from sfi import Data, Macro, SFIToolkit, Frame, Datetime as dt
        except OSError:
            print("Stata executable not found. Please install Stata and add it to your PATH.")

    def __repr__(self):
        return "DataBridgesStata(Stata_path='%s')" % self.configuration

    def __str__(self):
        return ("DataBridgesStata(yamlpath='%s') \n\n Brought to you with <3 by SHAPES \n\n"
                % self.configuration.host)

    def load_stata(self, df):
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