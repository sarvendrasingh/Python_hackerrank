crew_id_count = int(input("Number of crew: ").strip())
crew_id = []
print("Enter location of crews: ")
for _ in range(crew_id_count):
    crew_id_item = int(input().strip())
    crew_id.append(crew_id_item)

job_id_count = int(input("Number of repairs: ").strip())
job_id = []
print("Enter location of repairs: ")
for _ in range(job_id_count):
    job_id_item = int(input().strip())
    job_id.append(job_id_item)

crew_id.sort()
job_id.sort()
res = 0

for i in range(len(crew_id)):
    if crew_id[i] > job_id[i]:
        res += crew_id[i] - job_id[i]
    else:
        res += job_id[i] - crew_id[i]
print("Minimum distance to be covered: ")
print(res)
