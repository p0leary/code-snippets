# Comand to generate a simple dataframe in pyspark interpreter
df = sqlContext.createDataFrame([('a', 'bob'), ('a', 'susan')], ['col1', 'col2'])
