# Student Details Submission Form

This is my **first GUI program**, built using Python's `tkinter` library. It's a simple desktop application for collecting and saving student registration details.

Since this is my first attempt at building a GUI, please excuse any rough edges in the code or design — I'm still learning! As I grow more comfortable with GUI programming, I plan to write much more clear, simplified, and well-structured programs.

## What a User Can Expect

When you run the program, a window titled **"Student Details Submission"** will open, containing:

- A **course list** on the left side, showing a scrollable list of 35+ available courses (Python, Java, C, Web Development, AI, etc.)
- A **"Select Course"** button to confirm your chosen course from the list
- A **Name** field to enter the student's name
- An **Age** dropdown (combobox) with a fixed range of valid ages (18–24)
- A **Phone Number** field for contact details
- An **Address** text box for entering a multi-line address
- An **academy logo image** displayed in the center of the form
- A **Submit** button at the bottom to save the entered details

When you click **Submit**, the program checks that all fields are filled in correctly:
- If any field is empty, a warning popup will tell you exactly which one
- If the age entered isn't valid, you'll get a warning as well
- Once everything is valid, the details are saved and a success message appears, after which the window closes

## Program Interface

The interface is divided into sections (frames), each handling one part of the form:

| Section | Purpose |
|---|---|
| Top Frame | Displays the form title |
| Course Frame | Lists all available courses and lets the user select one |
| Name Frame | Input field for student name |
| Age Frame | Dropdown to select age |
| Phone Frame | Input field for phone number |
| Address Frame | Text box for address |
| Image Label | Displays the academy logo |
| Submit Button | Validates and saves the form data |

## Note on Code Formatting

I've added **extra spaces/blank lines in some parts of the main code** to make it easier to read and separate different sections visually. This is just to help avoid confusion while going through the code — it doesn't affect how the program runs.

## Functions Used

- **`select_course()`** — Gets the course selected by the user from the list box. If nothing is selected, it shows a warning; otherwise, it stores the selected course and confirms it via a popup.

- **`validate()`** — This is the core function tied to the Submit button. It:
  - Retrieves and cleans up the values from all input fields (name, age, phone number, address)
  - Checks each field to make sure nothing is left empty
  - Validates that the age selected falls within the allowed range (18–24)
  - If everything is valid, it writes the student's details into a text file (`students.txt`) in a tab-separated format, shows a success message, and closes the window
  - If something is missing or invalid, it shows an appropriate warning message instead

## Files You Can Customize

- **`students.txt`** — This is where all submitted student records are saved. You can open, view, or clear this file anytime. If it doesn't exist yet, it will be created automatically on the first successful submission.
- **`academy-logo.png`** — This is the logo image shown on the form. You can replace it with your own institution's logo (just keep the same file name, or update the file name in the code accordingly).

## A Note on Learning

This program isn't perfect — the layout uses manual pixel positioning (`place()`) rather than more flexible layout managers, and there's room for cleaner structure and validation logic. As I continue learning GUI development in Python, future versions/programs will be simpler, cleaner, and easier to maintain.
