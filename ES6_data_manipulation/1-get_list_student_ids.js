export default function getListStudentIds(students) {
  // Vérifier si l'argument est un tableau
  if (!Array.isArray(students)) {
    return [];
  }

  // Utiliser map pour extraire les ids
  return students.map((student) => student.id);
}
