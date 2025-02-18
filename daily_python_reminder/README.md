# Daily Python Learning Reminder

A simple Python script that sends daily desktop notifications to keep you on track with your Python learning journey. 🚀🐍

---

## Features:
- 📅 **Daily Reminders** at a specified time every day.
- 🔔 **Desktop Notifications** using the `plyer` library.
- ⏰ **Customizable Time** to fit your schedule.
- 🖥️ **Runs on Windows Command Prompt or Visual Studio Code.**

---

## Installation:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/tylermljones/daily-python-reminder.git
   cd daily-python-reminder
   ```

2. **Install the required library:**
   ```bash
   pip install plyer
   ```

---

## Usage:

1. Open the Python script `daily_reminder.py` in your code editor.
2. Modify the time in the script to your preferred schedule:
   ```python
   if current_time == "08:00:00":  # Change this to your desired time
   ```
3. Run the script:
   ```bash
   python daily_reminder.py
   ```

---

## Code Overview:
- `plyer.notification` is used to send desktop notifications.
- `time.sleep()` ensures the notification is sent once a day.
- Easily customizable to suit your learning schedule.

---

## Contributing:
Feel free to submit issues or pull requests to improve this script! 😊

---

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments:
- Inspired by the need to stay consistent while learning Python.
- Built with ❤️ using Python.

---

Happy Coding! 🐍✨