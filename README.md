This project is a simple and effective Age Calculator developed using Python. The main purpose of this program is to calculate a user’s current age in years based on their date of birth and the current system date. It is a beginner-friendly project that demonstrates how Python can work with dates and apply logical conditions to solve real-life problems.

The program starts by importing the date class from Python’s built-in datetime module. This module is essential because it provides access to today’s date directly from the system, ensuring accurate and up-to-date age calculation without manual input.

The user is prompted to enter their birth year, birth month, and birth day separately. These inputs are converted into integers so mathematical operations can be performed on them. Once the input is taken, the program retrieves today’s date using date.today() and stores it in a variable called today.

To calculate the age, the program initially subtracts the birth year from the current year. However, this alone is not always accurate. To handle this, a conditional statement is used to check whether the user’s birthday has already occurred in the current year. If today’s month is earlier than the birth month, or if the month is the same but the current day is before the birth day, the program subtracts one year from the calculated age. This logic ensures that the age calculation is precise.

Finally, the program displays the user’s age in a clear and readable format using a print statement.

🔹 Key Concepts Used

User input handling

Date and time manipulation

Conditional logic

Python’s datetime module

🔹 Learning Outcome

This project helps beginners understand how to work with real-time dates, apply logical conditions, and build a practical Python application. It is ideal for students who are starting with Python and want to improve their problem-solving skills through real-world examples.
