/*
Create an object factory for a student object.
The student object should have the following methods and it should produce the expected results
demonstrated in the sample code:

info: Logs the name and year of the student.
addCourse: Enrolls student in a course. A course is an object literal that has properties for its name and code.
listCourses: Returns a list of the courses student has enrolled in.
addNote: Adds a note property to a course. Takes a code and a note as an argument.
  If a note already exists, the note is appended to the existing one.
updateNote: Updates a note for a course. Updating a note replaces the existing note with the new note.
viewNotes: Logs the notes for all the courses. Courses without notes are not displayed.
*/

function createStudent(name, year) {
  return {
    name,
    year,
    courses: [],
    notes: {},

    info() {
      console.log(`${this.name} is a ${this.year} year student`);
    },
    listCourses() {
      console.log(this.courses);
    },
    addCourse(course) {
      this.courses.push(course);
    },
    getCourseName(code) {
      let selectedCourse = this.courses.filter(course => String(course.code) === code)[0];
      return selectedCourse.name;
    },
    addNote(code, note) {
      this.notes[code] = this.notes[code] ?? [];
      this.notes[code].push(note);
    },
    updateNote(code, note) {
      this.notes[code] = [note];
    },
    viewNotes() {
      for (let code in this.notes) {
        let courseName = this.getCourseName(code);
        console.log(`${courseName}: ${this.notes[code].join('; ')}`);
      }
    }
  }
}

let foo = createStudent('Foo', '1st');
foo.info();
// "Foo is a 1st year student"
foo.listCourses();
// [];
foo.addCourse({ name: 'Math', code: 101 });
foo.addCourse({ name: 'Advanced Math', code: 102 });
foo.listCourses();
// [{ name: 'Math', code: 101 }, { name: 'Advanced Math', code: 102 }]
foo.addNote(101, 'Fun course');
foo.addNote(101, 'Remember to study for algebra');
foo.viewNotes();
// "Math: Fun course; Remember to study for algebra"
foo.addNote(102, 'Difficult subject');
foo.viewNotes();
// "Math: Fun course; Remember to study for algebra"
// "Advance Math: Difficult subject"
foo.updateNote(101, 'Fun course');
foo.viewNotes();
// "Math: Fun course"
// "Advanced Math: Difficult subject"