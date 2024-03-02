import subprocess

while True:
    value = input(
        """
                  Enter a choice : 
                  1 : Add Student
                  2 : Train Model
                  3 : Attendace
                  4 : Send Attendace Excel to Admin
                  q : Quit
                  
                  
                  """
    )
    if value == "1":
        subprocess.run(["python", "01_face_dataset.py"])
    if value == "2":
        subprocess.run(["python", "02_face_training.py"])
    if value == "3":
        subprocess.run(["python", "03_face_recognition.py"])
    if value == "4":
        subprocess.run(["python", "04_automail.py"])
    if value == "q":
        break
