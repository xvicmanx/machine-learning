# Machine learning

Machine Learning is a subfield of Artificial Intelligence which goal is to develop technique to make computers (machines) learn.

The purpose of these repository is to solve some machine learning problems for academic purposes.


## GRPC service

### Compiling
Move to `grpc_service` directory and run:
```sh
python -m grpc_tools.protoc -I .  --python_out=. --grpc_python_out=. ./service.proto
```

### Starting server

Run the following command:
```sh
python start_server.py
```

### Run client demo

Run the following command:
```sh
python grpc_client.py
```