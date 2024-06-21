### Relational Algebra Operations

#### Selection (σ)
Filters rows based on a specified condition.
- **Syntax:** `σ_condition(Relation)`
- **Example:** `σ_Age > 20(Students)`

#### Projection (π)
Extracts specific columns from a relation.
- **Syntax:** `π_column1, column2, ...(Relation)`
- **Example:** `π_Name, Major(Students)`

#### Union (∪)
Combines the tuples of two relations and eliminates duplicates.
- **Syntax:** `Relation1 ∪ Relation2`
- **Example:** `Students_2023 ∪ Students_2024`

#### Set Difference (−)
Returns the tuples that are in the first relation but not in the second.
- **Syntax:** `Relation1 − Relation2`
- **Example:** `Students − GraduatedStudents`

#### Cartesian Product (×)
Combines each tuple of the first relation with every tuple of the second relation.
- **Syntax:** `Relation1 × Relation2`
- **Example:** `Students × Courses`

#### Rename (ρ)
Renames the output relation.
- **Syntax:** `ρ_newName(Relation)`
- **Example:** `ρ_EnrolledStudents(Students)`

### Additional Operations

#### Intersection (∩)
Returns the tuples that are common to both relations.
- **Syntax:** `Relation1 ∩ Relation2`
- **Example:** `EnrolledStudents ∩ HonorsStudents`

#### Join (⨝)
Combines related tuples from two relations based on a condition.
- **Syntax:** `Relation1 ⨝_condition Relation2`
- **Example:** `Students ⨝ Students.StudentID = Enrollments.StudentID Enrollments`

#### Division (÷)
Used when you want to find a relation that is paired with all tuples of another relation.
- **Syntax:** `Relation1 ÷ Relation2`
- **Example:** `StudentsWhoTookAllCourses ÷ RequiredCourses`