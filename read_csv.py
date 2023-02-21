import pandas

# pandas.read_csv
# Source: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv

filepath_or_buffer = ""

pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None,
                squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
                true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None,
                na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True,
                parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False,
                cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.',
                lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None,
                encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False,
                low_memory=True, memory_map=False, float_precision=None, storage_options=None)
