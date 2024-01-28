# data loading and basic cleaning
from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import pandas as pd
from pyspark import SparkFiles

if TYPE_CHECKING:
    from pyspark.sql import SparkSession, DataFrame


def file_loader(spark: SparkSession, path: str, info: Optional[bool] = False) -> DataFrame:
    """
    load the data from the given path and generate the info: schema,
    :param spark:
    :param path:
    :param info:
    :return: loaded data in the form of dataframe
    """
    df = spark.read.csv(path, header=True, inferSchema=True)
    if not info:
        return df
    print(df.printSchema())
    df_info = pd.DataFrame(df.dtypes, columns=["Column Name", "Data Type"])
    print(df_info)
    # creating description of the dataset
    df_description = df.describe().toPandas()
    print("?? Descriptive Report.")
    print(df_description)
    print("?? header:")
    print(df.limit(5).toPandas())
    return df


def url_loader(spark: SparkSession, path: str, local_name: str) -> DataFrame:
    """ Loading the data from an url. only csv file
    :param spark: current spark session obj
    :param path: url path
    :param local_name: name of the file
    :return: dataframe created.
    TODO: bug fix. path issue.
    """
    spark.sparkContext.addFile(path)
    df = spark.read.csv(SparkFiles.get(local_name), header=True, inferSchema=True)
    print("?? Descriptive Report")
    df.describe().toPandas()
    return df


if __name__ == "__main__":
    from initializer import init_spark_objs

    print("loading the data")
    spark_, _ = init_spark_objs()
    data = file_loader(spark_, path="../../Data/iris.csv", info=True)
