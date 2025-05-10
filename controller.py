import subprocess
import time

sec = 3

print("\n*** Welcome to AWS Services ***\n")

sub = input("\nAre you subscribed to sns? (yes/no) : ")

if sub.lower() == 'no':
    print("\nFirst you need to confirm your email, sending request...")
    subprocess.run(["python3", "sns.py"])
    answer = input("Did you confirmed the request? (yes/no) : ")
else:
    answer = 'yes'

if answer.lower() == 'yes':
    print("\nOk launching the program, Loading...\n")
    time.sleep(sec)

    subprocess.run(["python3", "createBuckets.py"])

    print("\nLoading...\n")
    time.sleep(sec)

    subprocess.run(["python3", "upload_files.py"])

    print("\nLoading...\n")
    time.sleep(sec)

    subprocess.run(["python3", "list_and_move.py"])

else:
    print("\n\n******** Process aborted ********\n\n")


print("\n****************** End of program ******************\n")
print("\n****************** GoodBye ******************\n")
