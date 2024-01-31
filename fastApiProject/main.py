from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "Orsok",
        "age": 22,
        "class": "year 2"
    }
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/students/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]

@app.post("/students")
async def add_student(student_name: str, student_age: int, student_birthday: int, student_class: int):
    students[student_name] = students
