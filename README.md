# Time Alert System

This Python-based Time Alert System provides hourly time notifications using text-to-speech technology. A pre-built `.exe` file is also available for users who do not have Python installed.

---

## Features
- Announces the current hour with a voice alert.
- Automatically adjusts for AM/PM format.
- Designed to run continuously in the background.
- No Python installation required (via provided `.exe` file).

---

## Requirements

### For Python Users:
- **Python Version**: Python 3.6 or higher
- **Modules**: 
  - `time` (built-in)
  - `pyttsx3` (install via `pip install pyttsx3`)

### For Non-Python Users:
- Download the provided `.exe` file and run it directly.

---

## How to Use

### Option 1: Run the Python Script
1. Clone or download this repository.
2. Install the required Python module:
   ```bash
   pip install pyttsx3
   ```
3. Run the script:
   ```bash
   python time_alert.py
   ```

### Option 2: Use the Pre-Built `.exe` File
1. [Download the pre-built `.exe` file here](#).  
   *(Add your link to the `.exe` file here.)*
2. Double-click the `.exe` file to start the program.
3. It will run in the background and announce the time every hour.

---

## Code Overview

### Functions:
- **`speak(text)`**: 
  - Initializes the `pyttsx3` engine to convert text to speech.
- **Main Logic**:
  - Continuously checks the time.
  - Announces the hour when minutes and seconds are `00:00`.

---

## Example Output

### Console Output
```
Time 9 AM
Time 10 AM
Time 11 PM
```

### Voice Alert
> "Time 9 AM"  
> "Time 10 AM"  
> "Time 11 PM"

---

## Download the `.exe` File
Click the link below to download the `.exe` file for direct use:  
[**Download Time Alert Executable**](#)  
*(Add your download link here.)*

---

## Future Enhancements
- Option to customize alert intervals (e.g., half-hourly).
- Allow users to set specific time zones or customize voice settings.
