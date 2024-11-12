# PurpleSector Backend Technical Challenge

## Instructions
During the Technical Challenge you will be asked to share your screen and talk through your thinking as you go.

To ensure you are prepared, please run the following steps ahead of the interview and confirm everything is working:

Ensure you have:
   * A stable internet connection.
   * A working webcam and microphone.
   * A quiet environment to conduct the interview.
   * Your code editor setup.
   * Have run the `Setup` steps


## Setup

### Pre-requisites
Make sure the following are installed on your system prior to running the project
* [Docker](https://docs.docker.com/engine/install/)
* [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

### Run the API
Create a `.env` file using `.env.dist` as a template.

```bash
cd .dev
docker-compose up --build
```
The API is available at `http://localhost:8000`.

## Clean-up
To remove all images and volumes created by docker-compose
```bash
docker-compose down -v --rmi all
```

# Technical Challenge - What do I need to do?
The questions and instructions for the technical challenge will be provided to you during the interview.
