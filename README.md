# Airflow Accelerator

Welcome to the Airflow training repository!

This repository is designed as a comprehensive guide for both beginners and advanced users interested in mastering 
Apache Airflow. Whether you are just starting out or looking to enhance your existing knowledge of Airflow, this resource 
offers a structured path to understanding and implementing effective data workflows using Airflow.

## What is Apache Airflow?
Apache Airflow is an open-source tool for orchestrating complex computational workflows and data processing pipelines. 
It enables scheduling and management of workflows so you can programmatically author, schedule, and monitor workflows.

## Repository Structure
This repository is divided into several specialized subfolders, each focusing on a different aspect of Airflow. 
Here’s what each folder contains:

### easy/
This folder provides step-by-step guidance on constructing basic Airflow Directed Acyclic Graphs (DAGs). It includes 
examples using both the context manager and decorator approaches to suit different preferences and needs. Ideal for 
those who are new to Airflow.

### python/
Explore how to build Extract, Transform, Load (ETL) DAGs using Python operators in this folder. It’s focused on tasks 
involving data manipulation using Python in a non-decorator fashion. Perfect for users with a Python background looking 
to leverage their skills in data processing workflows.

### xcom/
Dive into the concept of XComs (cross-communication) in Airflow, which allows different tasks to pass data among themselves. 
This folder covers practical examples and best practices for using XComs effectively in your DAGs.

### advanced/
For those who are comfortable with the basics and ready to tackle more complex scenarios, this folder explores advanced 
concepts and techniques in Airflow, especially within the context of ETL workflows.

### data_product_as_dag/
See a real-world example of an Airflow DAG designed as a data product at Astrafy. This section combines all the previously 
mentioned techniques to demonstrate a complete ETL pipeline, including integration with dbt for data transformations.