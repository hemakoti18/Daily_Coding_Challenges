

data = [ 
    {"batch": "b7", "name": "Anil", "consumption": 72, "live": 65, "recording": 70, 
"assignment_sub": 80, "assignment_score": 75}, 
    {"batch": "b7", "name": "Meena", "consumption": 45, "live": 50, "recording": 55, 
"assignment_sub": 40, "assignment_score": 35}, 
    {"batch": "b7", "name": "Ravi", "consumption": 18, "live": 20, "recording": 25, 
"assignment_sub": 10, "assignment_score": 15}, 
    {"batch": "b7", "name": "Pooja", "consumption": 85, "live": 75, "recording": 80, 
"assignment_sub": 90, "assignment_score": 88}, 
    {"batch": "b7", "name": "Kiran", "consumption": 30, "live": 40, "recording": 45, 
"assignment_sub": 25, "assignment_score": 28}, 
 
    {"batch": "b8", "name": "Asha", "consumption": 90, "live": 85, "recording": 88, 
"assignment_sub": 92, "assignment_score": 90}, 
    {"batch": "b8", "name": "Manoj", "consumption": 55, "live": 60, "recording": 65, 
"assignment_sub": 50, "assignment_score": 45}, 
    {"batch": "b8", "name": "Deepa", "consumption": 22, "live": 30, "recording": 35, 
"assignment_sub": 20, "assignment_score": 18}, 
    {"batch": "b8", "name": "Rahul", "consumption": 78, "live": 70, "recording": 75, 
"assignment_sub": 80, "assignment_score": 76}, 
    {"batch": "b8", "name": "Sneha", "consumption": 10, "live": 15, "recording": 20, 
"assignment_sub": 5, "assignment_score": 8}, 
 
    {"batch": "b9", "name": "Vikram", "consumption": 88, "live": 82, "recording": 90, 
"assignment_sub": 85, "assignment_score": 80}, 
    {"batch": "b9", "name": "Divya", "consumption": 60, "live": 68, "recording": 72, 
"assignment_sub": 65, "assignment_score": 60}, 
    {"batch": "b9", "name": "Arjun", "consumption": 35, "live": 40, "recording": 50, 
"assignment_sub": 30, "assignment_score": 25}, 
    {"batch": "b9", "name": "Neha", "consumption": 95, "live": 90, "recording": 95, 
"assignment_sub": 98, "assignment_score": 96}, 
    {"batch": "b9", "name": "Karthik", "consumption": 15, "live": 20, "recording": 25, 
"assignment_sub": 10, "assignment_score": 12} 
] 


# Code :

"""
1. calculate_average(values) 
Return the average of a list of numbers. 

"""
# Overall Averages for the whole class
def calculate_averages(values):
    if not values:
        return 0
    else:
        return sum(values) / len(values)

print(f"\n------ 1.Overall Averages for the Whole Class ---------\n")

columns = ["consumption", "live", "recording", "assignment_sub", "assignment_score"]
for col in columns:
    all_values = [student[col] for student in data]
    avg = calculate_averages(all_values)
    print(f"Overall Averages {col.title()} : {avg:.2f}")

batches = ["b7", "b8", "b9"]
for batch in batches:
    print(f"\nBatch : {batch}")
    for col in columns:
        batch_values = [student[col] for student in data if student["batch"] == batch]
        avg = calculate_averages(batch_values)
        print(f"Average {col.title()} : {avg:.2f}")

"""
2. find_top_performers(data, column, threshold) 
Return students whose score in the given column is greater than or equal to the 
threshold.  

"""
# 1. మీ స్టూడెంట్ డేటా
data = [ 
    {"batch": "b7", "name": "Anil", "consumption": 72, "live": 65, "recording": 70, "assignment_sub": 80, "assignment_score": 75}, 
    {"batch": "b7", "name": "Meena", "consumption": 45, "live": 50, "recording": 55, "assignment_sub": 40, "assignment_score": 35}, 
    {"batch": "b7", "name": "Ravi", "consumption": 18, "live": 20, "recording": 25, "assignment_sub": 10, "assignment_score": 15}, 
    {"batch": "b7", "name": "Pooja", "consumption": 85, "live": 75, "recording": 80, "assignment_sub": 90, "assignment_score": 88}, 
    {"batch": "b7", "name": "Kiran", "consumption": 30, "live": 40, "recording": 45, "assignment_sub": 25, "assignment_score": 28}, 
    {"batch": "b8", "name": "Asha", "consumption": 90, "live": 85, "recording": 88, "assignment_sub": 92, "assignment_score": 90}, 
    {"batch": "b8", "name": "Manoj", "consumption": 55, "live": 60, "recording": 65, "assignment_sub": 50, "assignment_score": 45}, 
    {"batch": "b8", "name": "Deepa", "consumption": 22, "live": 30, "recording": 35, "assignment_sub": 20, "assignment_score": 18}, 
    {"batch": "b8", "name": "Rahul", "consumption": 78, "live": 70, "recording": 75, "assignment_sub": 80, "assignment_score": 76}, 
    {"batch": "b8", "name": "Sneha", "consumption": 10, "live": 15, "recording": 20, "assignment_sub": 5, "assignment_score": 8}, 
    {"batch": "b9", "name": "Vikram", "consumption": 88, "live": 82, "recording": 90, "assignment_sub": 85, "assignment_score": 80}, 
    {"batch": "b9", "name": "Divya", "consumption": 60, "live": 68, "recording": 72, "assignment_sub": 65, "assignment_score": 60}, 
    {"batch": "b9", "name": "Arjun", "consumption": 35, "live": 40, "recording": 50, "assignment_sub": 30, "assignment_score": 25}, 
    {"batch": "b9", "name": "Neha", "consumption": 95, "live": 90, "recording": 95, "assignment_sub": 98, "assignment_score": 96}, 
    {"batch": "b9", "name": "Karthik", "consumption": 15, "live": 20, "recording": 25, "assignment_sub": 10, "assignment_score": 12} 
]

# 2. మనం ముందుగా తయారు చేసుకున్న ఫంక్షన్
def find_top_performers(data, column, threshold):
    top_performers_list = []
    for student in data:
        if student[column] >= threshold: 
            top_performers_list.append(student)
    return top_performers_list

    # or list comprehension kuda use cheyocchu
    """
    లూప్ మొదట thresholds_config నుండి col = "consumption" మరియు th_value = 75 అని తీసుకుంటుంది.
    ఇప్పుడు find_top_performers(data, col, th_value) లైన్ రన్ అయినప్పుడు, అది ఫంక్షన్‌కి వెళ్తుంది.
    అక్కడ డైనమిక్‌గా:ఫంక్షన్ లోని column = "consumption" గా మారుతుంది.ఫంక్షన్ లోని threshold = 75 గా మారుతుంది.
    అప్పుడు సింగిల్ లైన్ కోడ్ బ్యాక్‌గ్రౌండ్‌లో ఇలా రన్ అవుతుంది:
    if student.get("consumption", 0) >= 75

    """
    # return [student for student in data if student.get(column, 0) >= threshold]


# 3. ప్రతి కాలమ్‌కు విడివిడిగా థ్రెషోల్డ్స్ కాన్ఫిగరేషన్ (మీరు మార్చుకోవచ్చు)
thresholds_config = {
    "consumption": 75,
    "live": 70,
    "recording": 80,
    "assignment_sub": 80,
    "assignment_score": 75
}

# 4. లూప్ ద్వారా రన్ చేసి రిజల్ట్ ప్రింట్ చేయడం
for col, th_value in thresholds_config.items():
     # 📌 ఇక్కడ 'col' లో ఉన్న వాల్యూ... ఫంక్షన్ లోని 'column' లోకి స్టోర్ అవుతుంది!
    # 📌 'th_value' లో ఉన్న వాల్యూ... ఫంక్షన్ లోని 'threshold' లోకి స్టోర్ అవుతుంది!
    result = find_top_performers(data, col, th_value)
    
    print(f"\n📌 {col.upper()} (Threshold: {th_value}) దాటిన టాప్ స్టూడెంట్స్:")
    for student in result:
        # కేవలం స్టూడెంట్ పేరు మరియు ఆ కాలమ్ లో వాళ్లకు వచ్చిన వాల్యూ మాత్రమే చూపిస్తుంది
        print(f"- {student['name']} (Batch: {student['batch']}, Value: {student[col]})")


"""
3. find_at_risk_students(data, column, threshold) 
Return students whose score in the given column is below the threshold.

"""
def find_at_risk_students(data, column, threshold):
    return [student for student in data if student[column] < threshold]
   #low_performers_list = [] 
   #for student in data:
   #   if student[column] < threshold:
   #     low_performers_list.append(student)
   #return low_performers_list


thresholds_config = {
    "consumption": 75,
    "live": 70,
    "recording": 80,
    "assignment_sub": 80,
    "assignment_score": 75
}

for col, th_value in thresholds_config.items():
    result = find_at_risk_students(data, col, th_value)

    print(f"\n📌 {col.upper()} (Threshold Value : {th_value})\n")
    
    for student in result :
        print(f"{student["name"]} (Batch : {student["batch"]}, Value : {student[col]})")

"""
4. batch_summary(data) 
Return summary insights such as:  
o total students  
o average attendance  
o average assignment submission  
o average total consumption  

"""
# Total students
total_students = len(data)
print(f"Total Students : {total_students}")

# average attendence
def average_attendence(data):
    batch_stats = {} #ప్రతి బ్యాచ్ యొక్క మొత్తం Attendence scores కూడటానికి ఖాళీ డిక్షనరీ

    for student in data:
        batch_id = student["batch"]

        if batch_id not in batch_stats:
            batch_stats[batch_id] = {"students" : 0, "attendence_sum" : 0}
        batch_stats[batch_id]["students"] += 1
        batch_stats[batch_id]["attendence_sum"] += (student["live"] + student["recording"]) / 2

    summary = {}
    for batch_id, stats in batch_stats.items():
        summary[batch_id] = {
            "total_students" : stats["students"],
            "average_attendence" : round(stats["attendence_sum"] / stats["students"],2)
        }

    return summary

final_output = average_attendence(data)
print(f"{final_output}\n")

for batch_id, info in final_output.items():
    print(f"Batch : {batch_id} | Students : {info["total_students"]} | Avg_attendence : {info["average_attendence"]}")

# for all batches 
# Return summary insights such as:  

# o total students  
# o average attendance  
# o average assignment submission  
# o average total consumption  

def batch_summary(data):
    batch_stats = {} #ప్రతి బ్యాచ్ యొక్క మొత్తం మార్కులను కూడటానికి ఖాళీ డిక్షనరీ

    #row = {"batch": "b7", "name": "Anil", "consumption": 72, "live": 65, "recording": 70, "assignment_sub": 80, "assignment_score": 75}
    for student in data:
        batch_id = student["batch"]
        if batch_id not in batch_stats:
            batch_stats[batch_id] = {
                "total_students" : 0,
                "total_attendance" : 0,
                "total_assignment_submission" : 0,
                "total_consumption" : 0
            }
        batch_stats[batch_id]["total_students"] += 1
        batch_stats[batch_id]["total_attendance"] += (student["live"] + student["recording"]) / 2
        batch_stats[batch_id]["total_assignment_submission"] += student["assignment_sub"]
        batch_stats[batch_id]["total_consumption"] += student["consumption"]

    summary_insights = {}
    for batch_id, stats in batch_stats.items():
        count = stats["total_students"]
        summary_insights[batch_id] = {
            "total_students" : count,
            "average_attendance" : round(stats["total_attendance"] / count,2),
            "average_assignment_submission" : round(stats["total_assignment_submission"] / count,2),
            "average_consumption" : round(stats["total_consumption"] / count,2)
        }
    return summary_insights

result = batch_summary(data)

for batch_id, info in result.items():
    print(f"\n===== Batch : {batch_id} =====\n")
    print(f"Total Students : {info["total_students"]}")
    print(f"Average Attendance : {info["average_attendance"]}")
    print(f"Average Assignment Submission : {info["average_assignment_submission"]}")
    print(f"Average Consumption : {info["average_consumption"]}\n")

"""
5. rank_batches(batch_data) 
Compare multiple batches and return the best-performing batch.

"""

def rank_batches(batch_data):
    #batch_totals: ప్రతి బ్యాచ్ యొక్క మొత్తం మార్కులను కూడటానికి ఖాళీ డిక్షనరీ.
    batch_totals = {}
    #batch_counts: ప్రతి బ్యాచ్‌లో ఎంతమంది స్టూడెంట్స్ ఉన్నారో లెక్కించడానికి ఖాళీ డిక్షనరీ.
    batch_counts = {}

    for row in batch_data:
        #row = {"batch": "b7", "name": "Anil", "consumption": 72, "live": 65, "recording": 70, "assignment_sub": 80, "assignment_score": 75}
        batch_name = row["batch"]

        # కేవలం సంఖ్యాపరమైన మార్కులను మాత్రమే కూడటం
        # total_score = (72 + 65 + 70 + 80 + 75) = 362
        total_score = (row["consumption"] + row["live"] + row["recording"] + row["assignment_sub"] + row["assignment_score"])

        # ఒక స్టూడెంట్ యావరేజ్ మార్కులు (మొత్తం 5 కేటగిరీలు)
        # student_average = 362 / 5 = 72.4
        student_average = total_score / 5

        if batch_name not in batch_totals:
            batch_totals[batch_name] = 0
            batch_counts[batch_name] = 0
        #batch_totals["b7"] = 0 + 72.4 = 72.4
        #batch_totals["b7"] = 72.4 + 45.0 = 117.4
        #batch_totals = {"b7": 252.2, "b8": 256.4, "b9": 297.2} (మొత్తం మార్కులు)
        batch_totals[batch_name] += student_average
        #batch_counts = {"b7": 5, "b8": 5, "b9": 5} (స్టూడెంట్స్ కౌంట్)
        batch_counts[batch_name] += 1
    
    best_batch = None
    highest_avg = 0

    #batch_totals = {"b7": 252.2, "b8": 256.4, "b9": 297.2} (మొత్తం మార్కులు)
    #batch_counts = {"b7": 5, "b8": 5, "b9": 5} (స్టూడెంట్స్ కౌంట్)
    for batch in batch_totals:
        # batch_avg = 252.2 / 5 = 50.44
        batch_avg = batch_totals[batch] / batch_counts[batch]
        print(f"Batch : {batch} Average : {batch_avg:.2f}")

        if batch_avg > highest_avg:
            highest_avg = batch_avg
            best_batch = batch
    return f"\nBest Performing Batch : {batch}, Highest Average : {highest_avg:.2f}\n"

result = rank_batches(data)

print(result)

"""
Sample challenge statement: 
You are given student performance data for three batches: b7, b8, and b9. 
Write Python user-defined functions to calculate batch-level insights and identify: 
• best batch overall  
• top-performing students  
• at-risk students  
• average attendance  
• average assignment submission  
• average content consumption 

"""

"""
1• best batch overall  

"""
# ikkada list use chesthunaam

batch_scores = {} # batch la scores ni track cheyyadaniki oka empty dictionary

for student in data:
     #row = {"batch": "b7", "name": "Anil", "consumption": 72, "live": 65, "recording": 70, "assignment_sub": 80, "assignment_score":75
    batch = student["batch"]
    # total_score = (72 + 65 + 70 + 80 + 75) = 362
    total_score = (student["consumption"] + student["live"] + student["recording"] + student["assignment_sub"] + student["assignment_score"])
    # student_average = 362 / 5 = 72.4
    student_average = total_score / 5

    if batch not in batch_scores:
        batch_scores[batch] = [] # { b7 : [72.4, 45.0, 17.6, 83.6,33.6] }
    #Calculation:
        # Batch b7 Total: (72.4 + 45.0 + 17.6 + 83.6 + 33.6) = 252.2 / 5 = 50.44
        # Batch b8 Total: (51.0 + 52.0 + 56.6 + 49.4 + 47.4) = 256.4 / 5 = 51.28
        # Batch b9 Total: (58.6 + 60.0 + 66.4 + 57.6 + 54.6) = 297.2 / 5 = 59.44
    batch_scores[batch].append(student_average)

best_batch = None
highest_average = 0

for batch, scores in batch_scores.items():
    score = sum(scores) / len(scores)
    if score > highest_average:
        highest_average = score
        best_batch = batch
    print(f"Batch : {batch} Average : {score:.2f}")
print(f"Best Batch : {best_batch}, Highest Average : {highest_average}")

"""
2• top-performing students 

"""   

" For Overall batches "
top_students =  [] # total 3 batches nunchi top 3 students kosam oka kotha list create chesam

for student in data:
    batch = student["batch"]
    name = student["name"]
    # average cheyyadaniki student each columns total chesthunnam
    total_score = [
        student["consumption"],
        student["live"],
        student["recording"],
        student["assignment_sub"],
        student["assignment_score"]
    ]
    student_average = sum(total_score) / len (total_score)

    top_students.append((batch, name, student_average))

top_students.sort(key=lambda x: x[2], reverse = True)
# sorted_students = sorted(top_students.items() key=lambda x:x[1], reverse=True)
print(f" Top 3 Students : {top_students[:3]}\n")

# output:
# Top 3 Students : [('b9', 'Vikram', 85.0), ('b8', 'Sneha', 11.6), ('b7', 'Ravi', 17.6)]


# for presentation
print("top 3 students from 3 batches")
for batch, name, average in top_students[:3]:
    print(f" batch : {batch}, ( Name : {name}, Highest_Average : {average})")
print("-" * 50)



# Method 2: Prathi Batch nundi Top Student ni chudadam (Batch-wise Top)    
top_students = {} # bacth-wise top students kosam

for student in data:
    batch = student["batch"]
    name = student["name"]

    total_score =[
        student["consumption"],
        student["live"],
        student["recording"],
        student["assignment_sub"],
        student["assignment_score"] 
    ]
    average = sum(total_score) / len(total_score)

    if batch not in top_students:
        top_students[batch] = []
    top_students[batch].append((name,average))

print("Batch-wise top 3 students")
# KOTHAGA CHESINA CHANGE: Batch top results store cheyadaniki oka list
batch_tops = []
for batch, students_list in top_students.items():#students_list లోకి దానికి ఎదురుగా ఉన్న లిస్ట్ [("Pooja", 80), ("Ravi", 60)] వస్తుంది.
    highest_average = 0
    top_student_name = None
    for name, average in students_list:
        if average > highest_average:
            highest_average = average
            top_student_name = name # # ఇన్నర్ లూప్ ఇక్కడితో ముగిసింది
    
    # ఈ ప్రింట్ లైన్ ఇన్నర్ లూప్ కి బయట... కానీ ఔటర్ లూప్ కి లోపల ఉంది!
    print(f"Batch : {batch}, (Name : {top_student_name}, Highest_average : {highest_average})")

    # Ikkada batch top details ni list loki add chesthunnam
    batch_tops.append((batch, top_student_name, highest_average))


# IPPUDU SORT CHESTHUNNAM: Index 2 (highest_average) ni batti sort cheyali
batch_tops.sort(key=lambda x: x[2], reverse=True)

print("-" * 80)
print("Batch-wise top 3 students descending order")
# Final sorted outputs print cheyadam
for batch, name, avg in batch_tops:
    print(f"Batch : {batch}, (Name : {name}, Highest_average : {avg:.1f})")
        

"""
3• at-risk students 

"""
# list use chesi chesam
at_risk_students = []

for student in data:
    average = (student["consumption"] + student["live"] + student["recording"] + 
               student["assignment_sub"] + student["assignment_score"]) / 5
    if average < 30:
        at_risk_students.append((student["batch"], student["name"], average))
print(f"\nAt_Risk_Students : {at_risk_students}")

# for presentation
for batch, name, average in at_risk_students:
    print(f"Batch : {batch} - ( Name : {name}, Average : {average} )")


# dictionary use chesi cheyyali
at_risk_students = {}

for student in data:
    average = (student["consumption"] + student["live"] + student["recording"] + 
               student["assignment_sub"] + student["assignment_score"]) / 5
    
    if average < 30:
        batch = student["batch"]
        name = student["name"]

         # Batch inka dictionary lo lekapothe, kotha empty list ni create chestham
        if batch not in at_risk_students:
            at_risk_students[batch] = []
        at_risk_students[batch].append((name, average))

# Dictionary structure print chesi chuddam
print("At_Risk_Students Dictionary:")
print(at_risk_students)
print("-" * 50)

# 2. Presentation loops (Batch-wise presentation)
print("# Batch wise At Risk Students Details:")
for batch, students_list in at_risk_students.items():
    print(f"\nBatch : {batch}")
    
    for name, average in students_list:
        print(f"Name : {name}, Average : {average}")
print("-" * 50)

"""
4• average attendance 

"""
# individual ga find chesthunnam
total_live = sum([student["live"] for student in data])
total_reording = sum([student["recording"] for student in data])

print(f"Average Live : {total_live / len(data)}")
print(f"Average recording : {(total_reording / len(data)):.2f}")

# method 1
# total_live / len(data) + total_recording / len(data) / 2

# 1. Individual totals mathrame ikkada cheyaley
total_live = sum([student["live"] for student in data])
total_reording = sum([student["recording"] for student in data])

# Averages calculations
avg_live = total_live / len(data)
avg_recording = total_reording / len(data)

# Rendu averages ni add chesi 2 thoni divide cheyali (leka total components thoni cheyali)
overall_average = (avg_live + avg_recording) / 2

print(f"Method 1:")
print(f"Average Live : {avg_live:.2f}")
print(f"Average recording : {avg_recording:.2f}")
print(f"Overall Average : {overall_average:.2f}\n")

# method 2
# Averages calculate chesthunnam
avg_live = sum([student["live"] for student in data]) / len(data)
avg_recording = sum([student["recording"] for student in data]) / len(data)

# CORRECTION: Rendu averages math calculations balance avalante 2 thoni divide cheyali
overall_average = (avg_live + avg_recording) / 2

print(f"Method 2:")
print(f"Average Live : {avg_live:.2f}")
print(f"Average recording : {avg_recording:.2f}")
print(f"Overall Average : {overall_average:.2f}\n")

#method 3
# 1. సింగిల్ లైన్ లో టోటల్స్ కనుక్కోవడం
total_points = sum([student["live"] + student["recording"] for student in data])

# 2. SINGLE LINE FORMULA: మొత్తం మార్కులు / (స్టూడెంట్స్ కౌంట్ * 2)
overall_average = total_points / (len(data) * 2) 
print(f"Method 3:")
print(f"Overall Average : {overall_average:.2f}\n")

# method 4
# లూప్ కోసం ముందుగా టోటల్స్ ని 0 అనుకుందాం
sum_live = 0
sum_recording = 0

# లూప్ లోపల ప్రతి ఒక్కరి మార్కులు యాడ్ చేయడం
for student in data:
    sum_live += student["live"]
    sum_recording += student["recording"]

# లూప్ బయటికి వచ్చాక యావరేజ్ లెక్కించడం
avg_live = sum_live / len(data)
avg_recording = sum_recording / len(data)

# లూప్ లోపల వచ్చిన రెండు యావరేజ్ లను కలిపి 2 తో డివైడ్ చేయడం
overall_average_loop = (avg_live + avg_recording) / 2

print(f"Method 4:")
print(f"Average Live : {avg_live:.2f}")
print(f"Average recording : {avg_recording:.2f}")
print(f"Overall Average (Loop Way) : {overall_average_loop:.2f}")


"""
5• average assignment submission

"""
total_subs = sum(student["assignment_sub"] for student in data)
print(f"\nmethod 1: List Comprehension")
print(f"Average Assignment Submission: {total_subs / len(data)}%\n")

# for loop
total_subs = 0
for student in data:
    asgmnt_sub = student["assignment_sub"]
    total_subs += asgmnt_sub
avg = total_subs / len(data)
print(f"Method 2: For Loop")
print(f"Average Assignment Submission : {avg}%\n")

"""
6. Average Content Consumption

"""
total_consumption = sum(student["consumption"] for student in data)
print(f"Average Content Consumption: {total_consumption / len(data)}%")

"""
• best batch overall  
• top-performing students  
• at-risk students  
• average attendance  
• average assignment submission  
• average content consumption 

"""
# 1. Average Attendance (Live + Recording average per batch or overall? Let's check overall first)
avg_live = sum(d['live'] for d in data) / len(data)
avg_rec = sum(d['recording'] for d in data) / len(data)
print(f"Overall Live: {avg_live}, Rec: {avg_rec:.2f}\n")

# Let's calculate batch wise averages to see "Best batch overall"
batches = ['b7', 'b8', 'b9']
for b in batches:
    b_data = [d for d in data if d['batch'] == b]
    c = sum(d['consumption'] for d in b_data) / 5
    l = sum(d['live'] for d in b_data) / 5
    r = sum(d['recording'] for d in b_data) / 5
    sub = sum(d['assignment_sub'] for d in b_data) / 5
    score = sum(d['assignment_score'] for d in b_data) / 5
    overall = (c + l + r + sub + score) / 5
    print(f"Batch {b} -> Consumption: {c}, Live: {l}, Recording: {r}, Sub: {sub}, Score: {score} | Overall: {overall:.2f}")

# Method 2:
def analyze_student_data(student_list):
    # Step 1: Batch wise data separate cheyadaniki empty dictionary structure
    batch_data = {}
    at_risk_students = []
    
    # Step 2: Loop through each student record
    for student in student_list:
        batch = student["batch"]
        consumption = student["consumption"]
        
        # Calculate individual attendance: (live + recording) / 2
        attendance = (student["live"] + student["recording"]) / 2
        assignment_sub = student["assignment_sub"]
        
        # At-risk target check: consumption < 20
        if consumption < 20:
            at_risk_students.append(student["name"])
            
        # Dictionary lo batch structure lekapothe initialize cheyali
        if batch not in batch_data:
            batch_data[batch] = {
                "total_consumption": 0,
                "total_attendance": 0,
                "total_assignment_sub": 0,
                "count": 0
            }
            
        # Data aggregation (totals calculation)
        batch_data[batch]["total_consumption"] += consumption
        batch_data[batch]["total_attendance"] += attendance
        batch_data[batch]["total_assignment_sub"] += assignment_sub
        batch_data[batch]["count"] += 1

    # Step 3: Batch averages and best batch identification
    best_batch = None
    max_avg_consumption = -1
    batch_summary_output = []

    for batch, metrics in sorted(batch_data.items()):
        count = metrics["count"]
        avg_cons = metrics["total_consumption"] / count
        avg_att = metrics["total_attendance"] / count
        
        # Best batch tracker based on highest average consumption
        if avg_cons > max_avg_consumption:
            max_avg_consumption = avg_cons
            best_batch = batch
            
        batch_summary_output.append(f"{batch} - Avg Consumption: {avg_cons:.1f}%, Avg Attendance: {avg_att:.1f}%")

    # Step 4: Final output print cheyadam
    print(f"Best Batch: {best_batch}\n")
    print("Batch Summary:")
    for summary in batch_summary_output:
        print(summary)
    print(f"\nAt-Risk Students:\nStudents with consumption below 20%: {', '.join(at_risk_students)}")

# Function Call
analyze_student_data(data)
