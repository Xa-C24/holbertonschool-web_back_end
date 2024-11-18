export default function updateStudentGradeByCity(students, city, newGrades) {
  // Filtre les étudiants par ville
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      // Trouve la nouvelle note correspondante à l'étudiant
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);

      // Retourne l'étudiant avec la note mise à jour ou "N/A"
      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}
