# todo_app

# Pre-requisite
  
  1. Docker and Docker Compose: https://www.docker.com/

Clone this repository and follow the instruction below, please choose either Option 1 or Option 2:

# Option 1: Instruction for running the app using docker-compose
  
1. Run docker-compose*

  ```docker-compose up```
  
# Option 2: Instruction for building and running the app using Docker

  1. Change directory to web

  ```cd web```
  
  2. to build Docker image

  ```docker build . -t todo_app```
  
  3. to run in container

  ```docker run -p 5000:5000 todo_app```
  
  # To execute APIs after the container is running (Recommended to use Postman: https://www.postman.com/):
  
  1. To login to the app

```
curl -L -X POST "http://localhost:5000/login" -H "Content-Type: application/json" -H "Cookie: session=eyJ1c2VybmFtZSI6InRvZG9hcHBAZ21haWwuY29tIn0.Ys28xw.IXw0uDRyZGWCzRZtFS3W9YuqGzQ" --data-raw "{\"username\":\"todoapp@gmail.com\",\"password\":\"mypass123\"}"
```

  2. Home page - checking the either login or not into the app

```
curl -L -X GET "http://localhost:5000" -H "Cookie: session=eyJ1c2VybmFtZSI6InRvZG9hcHBAZ21haWwuY29tIn0.Ys28xw.IXw0uDRyZGWCzRZtFS3W9YuqGzQ"
```

  3. To add to-do into the list

```
curl -L -X POST "http://localhost:5000/add" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY1MDM3NSwianRpIjoiMDE4MDBkZDgtMTE1My00NjU3LTljNDgtZTFiOTVjOGI5NTdlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRvZG9hcHBAZ21haWwuY29tIiwibmJmIjoxNjU3NjUwMzc1LCJleHAiOjE2NTc2NTEyNzV9.2z6WsvxuZzoBO80b-4TuzIb3zM1tSHBtBvdG8WviDWk" -H "Content-Type: application/json" -H "Cookie: session=eyJ1c2VybmFtZSI6InRvZG9hcHBAZ21haWwuY29tIn0.Ys28xw.IXw0uDRyZGWCzRZtFS3W9YuqGzQ" --data-raw "{
    \"todo\": \"go for karting\"
}"
```

  4. To display all the list

```
curl -L -X GET "http://localhost:5000/listall" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY1MDM3NSwianRpIjoiMDE4MDBkZDgtMTE1My00NjU3LTljNDgtZTFiOTVjOGI5NTdlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRvZG9hcHBAZ21haWwuY29tIiwibmJmIjoxNjU3NjUwMzc1LCJleHAiOjE2NTc2NTEyNzV9.2z6WsvxuZzoBO80b-4TuzIb3zM1tSHBtBvdG8WviDWk" -H "Cookie: session=eyJ1c2VybmFtZSI6InRvZG9hcHBAZ21haWwuY29tIn0.Ys28xw.IXw0uDRyZGWCzRZtFS3W9YuqGzQ"
```

  5. To mark a selected to-do from the list

```
curl -L -X POST "http://localhost:5000/complete" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY1MDM3NSwianRpIjoiMDE4MDBkZDgtMTE1My00NjU3LTljNDgtZTFiOTVjOGI5NTdlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRvZG9hcHBAZ21haWwuY29tIiwibmJmIjoxNjU3NjUwMzc1LCJleHAiOjE2NTc2NTEyNzV9.2z6WsvxuZzoBO80b-4TuzIb3zM1tSHBtBvdG8WviDWk" -H "Content-Type: application/json" -H "Cookie: session=eyJ1c2VybmFtZSI6InRvZG9hcHBAZ21haWwuY29tIn0.Ys28xw.IXw0uDRyZGWCzRZtFS3W9YuqGzQ" --data-raw "{
    \"tomark\": \"go for swimming\"
}"
```

  6. To delete a selected to-do from the list

```
curl -L -X DELETE "http://localhost:5000/deltodo" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NzY1MDM3NSwianRpIjoiMDE4MDBkZDgtMTE1My00NjU3LTljNDgtZTFiOTVjOGI5NTdlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRvZG9hcHBAZ21haWwuY29tIiwibmJmIjoxNjU3NjUwMzc1LCJleHAiOjE2NTc2NTEyNzV9.2z6WsvxuZzoBO80b-4TuzIb3zM1tSHBtBvdG8WviDWk" -H "Content-Type: application/json" -H "Cookie: session=eyJ1c2VybmFtZSI6InRvZG9hcHBAZ21haWwuY29tIn0.Ys28xw.IXw0uDRyZGWCzRZtFS3W9YuqGzQ" --data-raw "{
    \"todelete\": \"go for karting\"
}"
```

  7. To logout from the app

```
curl -L -X GET "http://localhost:5000/logout"
```

# Information 
*The ```docker-compose down``` command helps to Stop and remove containers, networks, images, and volumes.

This application and all APIs call are execute from Windows.

During excution of cURL command please keep in mind to maintain cookie session value to avoid getting Unauthorized message. 
