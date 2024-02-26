# PA-ML-Assignment
![Flask_Semantic_Search_Flowchart](https://github.com/shafdsai25/my-project/assets/114987491/d3085b84-8ec3-4131-b89d-6d9d92ee29a3)


## Flask Semantic Search Application

This project is a Flask web application that implements a semantic search service for patent documents. It allows users to query a collection of patent documents for relevant results based on semantic similarity. The application utilizes Docker for easy setup and deployment, and it's designed to be scalable both vertically and horizontally to meet varying load demands.

## Features

- Semantic search on a dataset of patent documents.
- Flask RESTful API to handle search queries.
- Dockerized application for easy setup and deployment.
- Designed for scalability to handle increased load.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose are installed on your machine.
- Basic knowledge of Docker, Flask, and RESTful APIs.

## Installation and Setup

1. **Clone the repository**

    ```
    git clone https://github.com/shafdsai25/PA-ML-Assignment
    ```

2. **Navigate to the project directory**

    ```
    cd PA-ML-Assignment
    ```

3. **Build and run the Docker containers**

    ```
    docker-compose up --build
    ```

    This command will build the Docker image for the Flask application and start the service as defined in `docker-compose.yml`.

## How It Works & Scalability

### Data Preparation

Upon startup, the application extracts patent documents contained in `patent_jsons_ML Assignment.zip`. These documents are in JSON format and include various fields relevant to patent information. The system indexes these documents into a searchable collection, preparing them for semantic querying.

### Semantic Search Engine

At the core of the application is a semantic search engine built with Flask. It utilizes the Sentence Transformers library to generate embeddings for both the search queries and the patent documents. These embeddings capture the semantic meaning of the text, allowing for efficient retrieval of relevant documents based on semantic similarity.

### API Layer

The application exposes a RESTful API, built with Flask, that handles search queries. Users can search for patents using simple GET requests, and the system returns documents that are semantically related to the query terms.

### Containerization with Docker

The entire system is containerized using Docker, facilitating easy setup and deployment. The `docker-compose.yml` file defines the application service and any additional services required for the system to function, such as a database or a message queue if needed for scaling.

### Scalability

- **Vertical Scaling**: The Docker containers can be configured with more resources (CPU, RAM) to handle increased loads. This is suitable for immediate scaling needs.

- **Horizontal Scaling**: For long-term scalability, the application can be deployed across multiple instances behind a load balancer. This approach allows the system to handle significantly more requests by distributing the load evenly across instances. If the search workload increases, additional instances of the application can be deployed easily thanks to Docker.

- **Stateless Design**: The Flask application is designed to be stateless, ensuring that it can scale horizontally without session management complexities. This design choice supports deploying multiple instances of the application to handle increased traffic.

- **Database & Search Index**: The scalability of the database and search index is also considered. Technologies like Elasticsearch can be utilized for the search index, which supports distributed environments and can scale with the application.

## Usage

To use the semantic search service, send a GET request to the search endpoint with your query. For example:

    ```
    GET /search?query=processor
    ```

This will return a list of patent documents related to "processor".

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please refer to the CONTRIBUTING.md for guidelines on how to contribute to the project.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Flask for the simple and powerful web framework.
- Docker for the containerization solution.
- Sentence Transformers and ChromaDB for enabling semantic search capabilities.

## Contact

For any queries or further assistance, please reach out to farheenshafeena@gmail.com.
