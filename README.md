A simple Windows application that extracts birthdays from a CSV file and provides an easy way to copy names to the clipboard.

Features
✅ Modern UI with CustomTkinter
✅ Upload a CSV file with "Name" and "Birthday" columns
✅ Extracts birthdays from the past week (including Sunday)
✅ One-click copy to clipboard
✅ 2-second splash screen with author name
✅ Can be converted into a Windows EXE

Installation & Usage
1️⃣ Install dependencies:

nginx
Copy
Edit
pip install customtkinter pandas pyperclip
2️⃣ Run the script:

nginx
Copy
Edit
python TC_Birthday_2_Clipboard.py
3️⃣ Convert to EXE (optional):

css
Copy
Edit
pyinstaller --onefile --windowed --name "TC_Birthday_2_Clipboard" TC_Birthday_2_Clipboard.py
CSV Format Example
Name	Birthday
John Doe	1990-02-21
Jane Smith	1985-02-25
The program extracts birthdays that fall in the past week and displays only the names.

Contributing
Feel free to submit pull requests or report issues! 🚀
