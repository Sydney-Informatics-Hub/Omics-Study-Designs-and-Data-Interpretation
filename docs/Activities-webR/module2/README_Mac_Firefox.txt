MODULE 2 PRACTICAL — OPENING IN FIREFOX ON MAC
═══════════════════════════════════════════════

Chrome / Edge users: just double-click module2_design_activities.html. Done.
Skip this file entirely.

Firefox users: 2-minute setup below.


WHY THIS IS NEEDED
──────────────────
Firefox blocks WebAssembly shared memory when opening HTML files
directly from a folder or USB stick. Chrome and Edge don't have
this restriction. The fix is to run a tiny local web server
(one command, already included).


THE SIMPLEST METHOD — drag and drop
─────────────────────────────────────

Step 1:  Open Terminal
         Press Cmd+Space, type Terminal, press Enter

Step 2:  Type the letters:  cd
         Then press Space, do NOT press Enter yet
         (you should see:  cd  with a cursor waiting)

Step 3:  Open Finder and find the folder containing
         module2_practical.html and serve.py

Step 4:  Drag that FOLDER from Finder into the Terminal window
         The folder path will appear automatically after "cd "

Step 5:  Press Enter
         You are now inside the right folder

Step 6:  Type this and press Enter:
         python3 serve.py

Step 7:  Firefox will open automatically at:
         http://localhost:8000/module2_design_activities.html

         If it doesn't open automatically, copy that address
         into Firefox yourself.

Step 8:  When you are finished, press Ctrl+C in Terminal
         to stop the server, then close the Terminal window.


WHAT THE SERVER PRINTS WHEN IT WORKS
──────────────────────────────────────

  Module 2 Practical — server running
  ────────────────────────────────────
  Open this in Firefox (or any browser):

      http://localhost:8000/module2_design_activities.html

  Serving files from:  /Users/you/Desktop/module2
  Press Ctrl+C to stop.


TROUBLESHOOTING
───────────────

"Port 8000 already in use" / Firefox says connection refused
  The server now tries ports 8001, 8080, 8888, 9000 automatically.
  Watch the Terminal output — it will print the actual URL to use.
  Copy whatever URL appears and paste it into Firefox.

"python3: command not found"
  Try:   python serve.py   (without the 3)
  If that also fails, install Python free from https://www.python.org

"No such file or directory: serve.py"
  You are in the wrong folder. Repeat Steps 2–5 above,
  making sure to drag the folder that contains serve.py.

Page loads but shows a yellow Firefox warning banner
  You opened via file:// instead of http://localhost.
  Check that the address bar shows http://localhost:8000 (or 8001 etc.)

R never reaches "Ready" after the page loads
  Same cause — confirm the URL starts with http://localhost
