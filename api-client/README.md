# API client

The APIs exposed by this project access the mock project.

Start the mock server

Enter the mock directory:
```
uvicorn mock:app --reload --port 8010
```

Start the api-client project

Enter the api-client directory:
```
uvicorn mock:app --reload
```

