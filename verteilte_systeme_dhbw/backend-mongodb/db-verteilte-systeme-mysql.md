# Database Model for MongoDB

## Question
```json
{
  "_id": "<ObjectId>",
  "level": 5,
  "question": "Die Fragestellung",
  "topic": "Thema der Frage",
  "solution": {
      "a": "Antwort A",
      "b": "Antwort B",
      "c": "Antwort C",
      "correct_answer": "a",
      "explanation": "Erklärung der Lösung"
    }
}
```

## User
```json
{
  "_id": "<ObjectId>",
  "level": 1,
  "answered_questions": [
    {
      "question": "<ObjectId von Question>",
      "answer": true
    },
    {
      "question": "<ObjectId von Question>",
      "answer": false
    }
  ]
}
```

