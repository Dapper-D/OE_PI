import random

subjects = ["AWS S3", "EC2 Auto-scaling", "IAM Policy", "Lambda", "Terraform", "CloudWatch"]
actions = ["reviewing logs for", "optimizing the", "documenting the", "restructuring", "debugging"]
reasons = ["due to high latency.", "to improve security.", "for the Q3 audit.", "as per the new spec."]

with open("work_notes.txt", "w") as f:
    for _ in range(50):
        note = f"{random.choice(subjects)}: {random.choice(actions)} {random.choice(subjects)} {random.choice(reasons)}\n"
        f.write(note)
