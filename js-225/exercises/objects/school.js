// From official solution of past exercise
function createStudent(name, year) {
  return {
    name,
    year,
    courses: [],
    info() {
      console.log(`${this.name} is a ${this.year} year student`);
    },

    listCourses() {
      return this.courses;
    },

    addCourse(course) {
      this.courses.push(course);
    },

    addNote(courseCode, note) {
      const course = this.courses.filter(({code}) => code === courseCode)[0];

      if (course) {
        if (course.note) {
          course.note += `; ${note}`;
        } else {
          course.note = note;
        }
      }

    },

    viewNotes() {
      this.courses.forEach(course => {
        if (course.note) {
          console.log(`${course.name}: ${course.note}`);
        }
      });
    },

    updateNote(courseCode, note) {
      const course = this.courses.filter(({code}) => code === courseCode)[0];

      if (course) {
        course.note = note;
      }
    },
  };
}

/*
Create a school object. The school object uses the same kind of student object as the previous exercise.
It has methods that use and update information about the student.
Be sure to check out the previous exercise for the other arguments that might be needed by the school object.
Implement the following methods for the school object:

addStudent: Adds a student by creating a new student and adding the student to a collection of students.
  The method adds a constraint that the year can only be any of the following values:
  '1st', '2nd', '3rd', '4th', or '5th'. Returns a student object if year is valid otherwise it logs "Invalid Year".
enrollStudent: Enrolls a student in a course.
addGrade: Adds the grade of a student for a course.
getReportCard: Logs the grades of a student for all courses.
  If the course has no grade, it uses "In progress" as the grade.
courseReport: Logs the grades of all students for a given course name.
  Only student with grades are part of the course report.

To test your code, use the three student objects listed below.
Using the three student objects, produce the following values from the
getReportCard and courseReport methods respectively.
*/

function createSchool() {
  return {
    students: [],
    addStudent(name, year) {
      if (!['1st', '2nd', '3rd', '4th', '5th'].includes(year)) {
        return 'Invalid Year'
      }
      let newStudent = createStudent(name, year);
      this.students.push(newStudent);
      return newStudent;
    },
    enrollStudent(student, course) {
      student.addCourse(course);
    },
    addGrade(student, courseCode, grade) {
      let course = student.listCourses().find(course => course.code === courseCode);
      course['grade'] = grade;
    },
    getReportCard(student) {
      for (let course of student.listCourses()) {
        console.log(`${course.name}: ${course.grade ?? 'In progress'}`);
      }
    },
    getStudentsWithGrades(courseName) {
      let students = [];
      for (let student of this.students) {
        let course = student.listCourses().find(course => course.name === courseName);
        if (course !== undefined && course.grade !== undefined) {
          students.push(student);
        }
      }
      return students;
    },
    courseReport(courseName) {
      let courseStudents = this.getStudentsWithGrades(courseName);
      if (courseStudents.length === 0) {
        console.log(undefined);
        return;
      }

      let grades = [];
      console.log(`=${courseName} Grades=`);
      for (let student of courseStudents) {
        let courseInfo = student.listCourses().find(course => course.name === courseName);
        grades.push(courseInfo.grade);
        console.log(`${student.name}: ${courseInfo.grade}`);
      }
      console.log('---');
      console.log(`Course Average: ${(grades.reduce((acc, num) => acc + num, 0) / grades.length).toFixed(0)}`);
    }
  }
}

let school = createSchool();
let paul = school.addStudent('Paul', '3rd');
let mary = school.addStudent('Mary', '1st');
let kim = school.addStudent('Kim', '2nd');

let math = { name: 'Math', code: 101 };
let advancedMath = { name: 'Advanced Math', code: 102 };
let physics = { name: 'Physics', code: 202 };

school.enrollStudent(paul, {...math});
school.enrollStudent(paul, {...advancedMath});
school.enrollStudent(paul, {...physics});
school.enrollStudent(mary, {...math});
school.enrollStudent(kim, {...math});
school.enrollStudent(kim, {...advancedMath});

school.addGrade(paul, 101, 95);
school.addGrade(paul, 102, 90);
school.addGrade(mary, 101, 91);
school.addGrade(kim, 101, 93);
school.addGrade(kim, 102, 90);

school.getReportCard(paul);
school.courseReport('Math');
school.courseReport('Advanced Math');
school.courseReport('Physics');

// Examples of created student objects with grades; methods
// on the objects are not shown here for brevity. The
// following are only showing the properties that aren't
// methods for the three objects

console.log(paul);
// {
//   name: 'Paul',
//   year: '3rd',
//   courses: [
//     { name: 'Math', code: 101, grade: 95, },
//     { name: 'Advanced Math', code: 102, grade: 90, },
//     { name: 'Physics', code: 202, }
//   ],
// }

console.log(mary);
// {
//   name: 'Mary',
//   year: '1st',
//   courses: [
//     { name: 'Math', code: 101, grade: 91, },
//   ],
// }

console.log(kim);
// {
//   name: 'Kim',
//   year: '2nd',
//   courses: [
//     { name: 'Math', code: 101, grade: 93, },
//     { name: 'Advanced Math', code: 102, grade: 90, },
//    ],
// }


/*
getReportCard output:
> school.getReportCard(paul);
= Math: 95
= Advanced Math: 90
= Physics: In progress
*/

/*
courseReport output:
> school.courseReport('Math');
= =Math Grades=
= Paul: 95
= Mary: 91
= Kim: 93
= ---
= Course Average: 93

> school.courseReport('Advanced Math');
= =Advanced Math Grades=
= Paul: 90
= Kim: 90
= ---
= Course Average: 90

> school.courseReport('Physics');
= undefined
*/
