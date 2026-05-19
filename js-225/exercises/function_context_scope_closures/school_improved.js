/*
In an earlier exercise, we created a school object. It works, however, it can still be improved. The following are improvements for you to implement in the solution provided:

Make the list students private. Right now, anyone can gain access to it and manipulate it.
Make the constraint for allowed values for years a private variable. As a private variable it avoids an unnecessary statement in the addStudent method and at the same time makes the code more declarative.
Make the getCourse function accessible in the addGrade method also. As it is, only the courseReport method has access.
*/

let school = (() => {
  const students = [];
  const ALLOWED_YEARS = ['1st', '2nd', '3rd', '4th', '5th'];
  const getCourse = (student, courseName) => {
    return student.listCourses().find(course => course.name === courseName);
  };

  return {
    addStudent(name, year) {
      if (!ALLOWED_YEARS.includes(year)) {
        return 'Invalid Year'
      }
      let newStudent = createStudent(name, year);
      students.push(newStudent);
      return newStudent;
    },
    enrollStudent(student, course) {
      student.addCourse(course);
    },
    addGrade(student, courseName, grade) {
      let course = getCourse(student, courseName);
      course['grade'] = grade;
    },
    getReportCard(student) {
      for (let course of student.listCourses()) {
        console.log(`${course.name}: ${course.grade ?? 'In progress'}`);
      }
    },
    getStudentsWithGrades(courseName) {
      let studentsWithGrades = [];
      for (let student of students) {
        let course = getCourse(student, courseName);
        if (course !== undefined && course.grade !== undefined) {
          studentsWithGrades.push(student);
        }
      }
      return studentsWithGrades;
    },
    courseReport(courseName) {
      let courseStudents = this.getStudentsWithGrades(courseName);
      if (courseStudents.length === 0) {
        return;
      }

      let grades = [];
      console.log(`=${courseName} Grades=`);
      for (let student of courseStudents) {
        let courseInfo = getCourse(student, courseName);
        grades.push(courseInfo.grade);
        console.log(`${student.name}: ${courseInfo.grade}`);
      }
      console.log('---');
      console.log(`Course Average: ${(grades.reduce((acc, num) => acc + num, 0) / grades.length).toFixed(0)}`);
    }
  }
})();