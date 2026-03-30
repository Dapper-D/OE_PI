import random

# Technical vocabulary to blend in with Cloud/IT workloads
tech_stack = ["AWS S3", "EC2 Cluster", "IAM Role", "Lambda Function", "Terraform Script", "CloudWatch Alarm", "VPC Peering"]
verbs = ["optimizing", "refactoring", "documenting", "debugging", "reviewing logs for", "scaling"]
outcomes = ["to reduce latency.", "for the security audit.", "to handle spike traffic.", "per the architecture review.", "to lower monthly spend."]

def generate_notes(count=50):
    with open("work_notes.txt", "w") as f:
        for _ in range(count):
            # Mix and match to create unique sentences
            s = random.choice(tech_stack)
            v = random.choice(verbs)
            o = random.choice(outcomes)
            
            note = f"{v.capitalize()} {s} {o}\n"
            f.write(note)
    print(f"✅ Successfully generated {count} unique work notes.")

if __name__ == "__main__":
    generate_notes()
