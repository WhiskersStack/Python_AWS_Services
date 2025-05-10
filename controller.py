import subprocess
import time

sec = 2

print("\n*** Welcome to AWS Services ***\n")
print("\nFirst you need to confirm your email, sending request...")

subprocess.run(["python3", "sns.py"])

answer = input("Did you confirmed the request? (yes/no) : ")

if answer.lower() == 'yes':
    print("\nGood Lets continue...\n\n\n")
    subprocess.run(["python3", "createBuckets.py"])

    time.sleep(sec)

    subprocess.run(["python3", "upload_files.py"])

    time.sleep(sec)

    subprocess.run(["python3", "list_and_move.py"])

    time.sleep(sec)
else:
    print("\n\n******** Process aborted ********\n\n")


print("\n****************** End of program ******************\n")
print("\n****************** GoodBye ******************\n")
