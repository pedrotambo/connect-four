# Connect Four

This codebase was used for making a web application to play the [Connect Four](https://en.wikipedia.org/wiki/Connect_Four) game.

## Links

* [Frontend (AWS S3)](http://connect-four-pepi.s3-website-us-east-1.amazonaws.com/)
* [Backend API (AWS ES2)](http://ec2-54-87-213-213.compute-1.amazonaws.com:8000)
* [API Documentation](http://ec2-54-87-213-213.compute-1.amazonaws.com:8000/docs)

## Development
The development process involved:
* Game logic
* Backend API
* Persistence layer
* Frontend
* Deployment: AWS EC2 (backend instance) and S3 (frontend statics)

### Backend
* Python3
* FastAPI
* PickleShare (key-value database)

### Frontend:
* React
* TypeScript


## Design

#### Game Logic
Was built based on the principle of maintaining a state and having a single point of mutability:

```GameState + Input -> GameState'```

As a side note, the development was made using TDD.

#### Persistence
Was used a key-value database. As it was only wanted to save the game states without creating relationships between entities, this was the database style preferred. In addition, for rapid development was used a file system based database. In a real environment it would be necessary to choose a more consistent one.

#### API
For rapid development, it was decided to develop a REST API and making use of long-polling + refetching on demand in the frontend. As a future development might be enriching to develop the communication making use of WebSockets or Server-sent events so the frontend could be notified about any change in the game state to improve the overload in the requests and frontend responsiveness.
