from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


def init_spark_objs(appname: str = "daEL1"):
    conf = SparkConf().setAppName(appname).setMaster("local")
    spark_context: SparkContext = SparkContext(conf=conf)
    spark_session: SparkSession = SparkSession(sparkContext=spark_context)
    return spark_session, spark_context
