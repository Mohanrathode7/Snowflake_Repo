#Import Libraries mohan
from __future__ import annotations
from snowflake.snowpark.session import Session
from snowflake.snowpark import DataFrame
from snowflake.snowpark.functions import udf, sproc, col
from snowflake.snowpark.types import IntegerType, FloatType, StringType, BooleanType, Variant
from snowflake.snowpark import functions as fn

import numpy as np
import pandas as pd
conn_config = {
    "account": "he84082.europe-west4.gcp",
    "user": "Mohan89",
    "password": "Test789@#",
    "role" : "ACCOUNTADMIN",
    "warehouse" : "COMPUTE_WH",
    "database" : "MOHAN",
    "schema" : "PRACTICE"
}

#Invoking Snowpark Session for Establishing Connection
new_session = Session.builder.configs(conn_config).create()
query=new_session.sql("Select * from emp")
query.show()
