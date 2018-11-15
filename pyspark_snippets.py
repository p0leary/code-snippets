# Comands to generate a simple dataframe in pyspark interpreter
df = sqlContext.createDataFrame([('a', 'bob'), ('a', 'susan')], ['col1', 'col2'])
df = sqlContext.createDataFrame([('1', 12, '1'), ('2', 13, '1')], ['col1', 'col2', 'col3'])

