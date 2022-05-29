# TKV API
API in charge of create accounts for customers.

# Getting Docker

## Windows

[Set up for Windows](https://docs.docker.com/desktop/windows/install/)

## Linux

[Set up for Linux](https://docs.docker.com/desktop/linux/install/)

## Mac

[Set up for MacOS](https://docs.docker.com/desktop/mac/install/)


# Cloning the repository

Open a terminal (for Windows you can use git bash)

Type:
```
git clone https://github.com/rjunior8/tkv_api.git
cd tkv_api
```

Make sure that Docker service is running.

# Build the containers and start them.

## Creating the environment variables.

Create a file named ```.env``` in the root directory (in the same place of Dockerfile).

```
MYSQL_DATABASE=database_name
MYSQL_USER=user_name
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=root_password
```

Now you can build the containers.

```
docker-compose up --build
```

To run in detached mode (run containers in the background).
```
docker-compose up --build -d
```

## See more Docker compose commands in:
[docker compose](https://docs.docker.com/engine/reference/commandline/compose/)

# Accessing the API GUI.

Open a browser and type:
```
http://0.0.0.0:9741/
```

You'll see:

![This is the caption](https://github.com/rjunior8/tkv_api/blob/main/tkv_api.png?raw=true)