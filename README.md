## Count Visitor

### Project Explaining:

This project is built using on the basic FastAPI microframework. Apart from these, the project is
dockerized with the docker application.

The main purpose of this project is to calculate visitor entries and exits at the location.


* This project name: **Count Visitor**
* This project's basic folder: **counter**

### Required Application:

For the project to up; Docker application must be installed and running in your local.

### Clone Project:

**https://github.com/omerdemirarslan/count-visitor**

### Run The Project:
    
    -> Docker command:
        docker-compose up --build or
        docker-compose build
        docker-compose up

    -> Make command:
        make up-build
        make up
        make down
        make build
        make run
        make logs

---
### API Endpoints:

    -> /api/v1/visitor/count/       (Gets Calculated Visitor Count Data)

### Endpoints
---

#### Request
    METHOD: POST
    ENDPONINT: /api/v1/visitor/count/
    ROW:
```json
{
    "10:00-11:00": [{"type": "in", "value": 15}, {"type": "out", "value": 12}, {"type": "in", "value": 4}],
    "11:00-12:00": [{"type": "in", "value": 11}, {"type": "out", "value": 14}, {"type": "out", "value": 4}],
    "12:00-13:00": [{"type": "in", "value": 24}, {"type": "out", "value": 4}, {"type": "in", "value": 15}],
    "13:00-14:00": [{"type": "in", "value": 8}, {"type": "out", "value": 25}, {"type": "in", "value": 12}],
    "14:00-15:00": [{"type": "in", "value": 3}, {"type": "out", "value": 5}, {"type": "in", "value": 17}, {"type": "out", "value": 30}],
    "15:00-16:00": [{"type": "in", "value": 19}, {"type": "out", "value": 2}],
    "16:00-17:00": [],
    "17:00-18:00": [{"type": "in", "value": 4}, {"type": "out", "value": 36}]
}
```
---

#### Response

```
{
    "data": [
        "10:00-11:00: 19 kişi girdi, 12 kişi çıktı, 7 kişi içeride",
        "11:00-12:00: 11 kişi girdi, 18 kişi çıktı, 0 kişi içeride",
        "12:00-13:00: 39 kişi girdi, 4 kişi çıktı, 35 kişi içeride",
        "13:00-14:00: 20 kişi girdi, 25 kişi çıktı, 30 kişi içeride",
        "14:00-15:00: 20 kişi girdi, 35 kişi çıktı, 15 kişi içeride",
        "15:00-16:00: 19 kişi girdi, 2 kişi çıktı, 32 kişi içeride",
        "16:00-17:00: 0 kişi girdi, 0 kişi çıktı, 32 kişi içeride",
        "17:00-18:00: 4 kişi girdi, 36 kişi çıktı, 0 kişi içeride"
    ]
}
```

---

### Last Notes:

My project is always open to development. I admit it's not perfect, but my goal is not to be perfect, but to always be
able to do better. I am waiting for your positive or negative feedback.

---
