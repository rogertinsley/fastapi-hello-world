# fastapi hello-world

fastapi & mongodb.

```bash
docker-compose up --build

curl -X POST "http://127.0.0.1:8000/todos/" -H "Content-Type: application/json" -d '{"title": "Test Todo", "description": "This is a test"}'
curl -X GET "http://127.0.0.1:8000/todos/"
```