# Interview Project for Python backend developer

Create a private git repo and implement the following projet.

## Goal
1. Create a Django project
2. Use Postgres as DB (in Docker container)
3. Add tables:
    - Person (name, email, age, phone, address, created datetime, modified datetime)
    - Employee (person_id Foreign Key, department, role, line_manager person_id Foreign Key, created datetime, modified datetime)
4. Django Admin views for Person and Employee models
5. REST APIs to add, delete, modify single or multiple
    - Person(s)
    - Employees(s) 
7. REST APIs to bulk query Persons or Employees over any combinations of the fields of the two models
8. Postman file demonstrating the REST APIs

## Quality Assurance
1. Tests run in Git Action on all pull request commits
2. Code coverage with coverage.py after all tests run - target for 100% code coverage (exclude all 3rd party libraries)
3. Lint
4. Document source code with pydoc

## Interview Demo
Interviewee will demonstrate the project in action and perfrom certion operation as requested. Questions will be asked about your different coding choices in the project and on any part of the repository.
