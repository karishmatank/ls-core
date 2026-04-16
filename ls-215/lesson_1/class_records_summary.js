let studentScores = {
  student1: {
    id: 123456789,
    scores: {
      exams: [90, 95, 100, 80],
      exercises: [20, 15, 10, 19, 15],
    },
  },
  student2: {
    id: 123456799,
    scores: {
      exams: [50, 70, 90, 100],
      exercises: [0, 15, 20, 15, 15],
    },
  },
  student3: {
    id: 123457789,
    scores: {
      exams: [88, 87, 88, 89],
      exercises: [10, 20, 10, 19, 18],
    },
  },
  student4: {
    id: 112233445,
    scores: {
      exams: [100, 100, 100, 100],
      exercises: [10, 15, 10, 10, 15],
    },
  },
  student5: {
    id: 112233446,
    scores: {
      exams: [50, 80, 60, 90],
      exercises: [10, 0, 10, 10, 0],
    },
  },
};

const EXAM_WEIGHT = 0.65;
const EXERCISE_WEIGHT = 0.35;

function generateClassRecordSummary(scores) {
  let studentGrades = Object.values(scores).map(getStudentGrade);
  let scoresPerExam = Object.values(scores).reduce(getScoresPerExam, []);
  let exams = scoresPerExam.map(summarizeExam);

  return {
    studentGrades,
    exams
  };
}

function summarizeExam(examScores) {
  let average = Number((addElements(examScores) / examScores.length).toFixed(1));
  let minimum = Math.min(...examScores);
  let maximum = Math.max(...examScores);
  return { average, minimum, maximum };
}

function getScoresPerExam(tally, { scores }) {
  scores.exams.forEach((score, idx) => {
    tally[idx] = tally[idx] || [];
    tally[idx].push(score);
  });
  return tally;
}

function getStudentGrade({ scores }) {
  let examAverage = addElements(scores.exams) / scores.exams.length;
  let exercisesTotal = addElements(scores.exercises);
  let finalScore = Math.round(examAverage * EXAM_WEIGHT + exercisesTotal * EXERCISE_WEIGHT);
  let grade = getLetterGrade(finalScore);
  return `${finalScore} (${grade})`;
}

function addElements(arr) {
  return arr.reduce((acc, ele) => acc + ele, 0);
}

function getLetterGrade(finalScore) {
  if (finalScore >= 93) {
    return 'A';
  } else if (finalScore >= 85) {
    return 'B';
  } else if (finalScore >= 77) {
    return 'C';
  } else if (finalScore >= 69) {
    return 'D';
  } else if (finalScore >= 60) {
    return 'E';
  } else {
    return 'F';
  }
}

console.log(generateClassRecordSummary(studentScores));

// returns:
// {
//   studentGrades: [ '87 (B)', '73 (D)', '84 (C)', '86 (B)', '56 (F)' ],
//   exams: [
//     { average: 75.6, minimum: 50, maximum: 100 },
//     { average: 86.4, minimum: 70, maximum: 100 },
//     { average: 87.6, minimum: 60, maximum: 100 },
//     { average: 91.8, minimum: 80, maximum: 100 },
//   ],
// }