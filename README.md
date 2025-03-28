# fastapi hello-world

```bash
curl -X POST "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"name": "Laptop"}'
curl -X GET "http://127.0.0.1:8000/items/1"
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"name": "Gaming Laptop"}'
curl -X DELETE "http://127.0.0.1:8000/items/1"
```