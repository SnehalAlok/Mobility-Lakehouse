# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from typing import List
from pyspark.sql import DataFrame
from pyspark.sql.window import Window

# COMMAND ----------

class transformations:
    
    def dedup(self,df:DataFrame, dedup_cols:List,cdc:str):
        df= df.withColumn("dedupKey",concat(*dedup_cols))
        df= df.withColumn("dedupCounts",row_number().over(Window.partitionBy("dedupKey").orderBy(desc(cdc))))
        df= df.filter(df.dedupCounts==1)
        df= df.drop("dedupKey","dedupCounts")
        return df
    def process_timestamp(self,df):
        df= df.withColumn("process_timestamp",current_timestamp())
        return df

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Customers**

# COMMAND ----------

df_cust = spark.read.table("pysparkdbt.bronze.customers")

# COMMAND ----------

display(df_cust.count())

# COMMAND ----------

df_cust = spark.read.table("pysparkdbt.bronze.customers")
display(df_cust)

# COMMAND ----------

df_cust = df_cust.withColumn("domain",split(col("email"),"@")[1])
display(df_cust)

# COMMAND ----------

df_cust.printSchema()

# COMMAND ----------

df_cust = df_cust.withColumn("Full_Name", concat_ws(" ", col("first_name"), col("last_name")))
display(df_cust)

# COMMAND ----------

df_cust = df_cust.drop('first_name','last_name')
display(df_cust)

# COMMAND ----------

cust_obj = transformations()
cust_df_trns = cust_obj.dedup(df_cust,['customer_id'],'last_updated_timestamp')
display(cust_df_trns)

# COMMAND ----------

df_cust=cust_obj.process_timestamp(cust_df_trns)
display(df_cust)

# COMMAND ----------

from delta.tables import DeltaTable
if spark.catalog.tableExists("pysparkdbt.silver.customers"):
  df.write.format("delta")\
      .mode("append")\
      .saveAsTable("pysparkdbt.silver.customers")
else:
  df.write.format("delta")    