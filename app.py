from flask import Flask, render_template, request, redirect
from collections import deque
from models import Patient  # This links the two files

app = Flask(__name__)

waiting_queue = deque()  # FIFO Queue Requirement
patients_seen = 0

@app.route('/')
def home():
    return render_template('home.html', 
                           queue=list(waiting_queue), 
                           total=len(waiting_queue),
                           seen=patients_seen)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        
        # Create the object using the Class
        patient = Patient(name, age, condition)
        waiting_queue.append(patient)
        return redirect('/')
    return render_template('add.html')

@app.route('/serve')
def serve():
    global patients_seen
    if waiting_queue:
        waiting_queue.popleft() # FIFO: First-in, first-out logic
        patients_seen += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)