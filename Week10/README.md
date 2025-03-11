# Lab Week 10 - Coding Questions

## Due Date
**Saturday, March 19 - Midnight**

## Overview
This lab focuses on database query manipulation using SQLite in Python. Students will work with string indexing, row deletion, database connection handling, and error validation. The provided `main.py` and `function.py` files serve as a starting point, with potential syntactical or logical errors that will be addressed during the lab session. If you miss the lab, you are expected to resolve these errors independently before submission.

## Tasks

### 1. String Indexing
- Create a new query `query_q1` that selects all rows where `id > 14`.
- Use **string indexing** to extract only the names from the query results.
- Use the following SQLite connection setting to enable indexing:
  ```python
  db_con.row_factory = sqlite3.Row
  ```
- Refer to **page 10/17** of the Lab Manual for additional guidance.

### 2. Delete Row
- Prompt the user for a `row id` to delete and store it in a variable `del_row`.
- Create a new query `query_q2` that deletes all rows in the table `demo` where `id < del_row`.
- Display a confirmation message, replacing `5` with the actual number of affected rows:
  ```
  "5 rows affected. Are you sure you want to continue?"
  ```
- Refer to **page 12-13** of the Lab Manual for details.

### 3. Database Connection Handling
- Convert all instances of:
  ```python
  db_con.close()
  ```
  to use the `with closing(...)` syntax for automatic connection handling.
- Refer to **page 16/17** of the Lab Manual for examples.

### 4. Error Handling (Validation)
- Add `try-except` blocks in **5 key locations** in the code:
  1. Attempting to connect to the database.
  2. Executing queries.
- Refer to **page 17/17** of the Lab Manual for best practices.

## Submission Instructions
1. **Fix any errors** encountered during the lab session (if applicable).
2. Submit the following files:
   - `main.py`
   - `function.py`

## Notes
- The lab session will start with an empty `main.py` gradually building toward the final versions.
- If you miss the lab, you are responsible for troubleshooting and fixing any syntax or logic errors before submission.
- Use the Lab Manual as a reference throughout the implementation process.

---
**Lab Manual References:**
- Page 10/17: String Indexing
- Page 12-13: Row Deletion
- Page 16/17: Database Connection Handling
- Page 17/17: Error Handling
