# Data Pipeline

This repository contains code for a data pipeline that scrapes data from multiple websites, transforms it into a common format, and stores it in a PostgreSQL database. The pipeline is implemented using Python and Apache Airflow.

## Requirements

To run this pipeline, you will need:

- Docker
- Docker Compose

## Installation

To install the pipeline, follow these steps:

1. Clone this repository to your local machine.
2. Build the Docker image using the following command: docker build -t data-pipeline 
3. Start the Docker container using the following command: docker-compose up -d
This will start the PostgreSQL database and the Apache Airflow web server and scheduler.
4. Access the Apache Airflow web interface by navigating to `http://localhost:8080` in your web browser.
5. Configure the pipeline by setting up the connections to the data sources and the PostgreSQL database. You can do this using the Airflow web interface.
6. Start the pipeline by triggering the DAG (Directed Acyclic Graph) in the Airflow web interface.

## Usage

To use the pipeline, follow these steps:

1. Configure the pipeline by setting up the connections to the data sources and the PostgreSQL database. You can do this using the Airflow web interface.
2. Start the pipeline by triggering the DAG (Directed Acyclic Graph) in the Airflow web interface.
3. Monitor the pipeline using the Airflow web interface.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make your changes and commit them to your branch.
4. Submit a pull request to this repository.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

