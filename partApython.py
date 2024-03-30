from collections import defaultdict
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def dice_combinations(dieA, dieB):
    combinations = defaultdict(int)
    
    for a in range(1, dieA + 1):
        for b in range(1, dieB + 1):
            total = a + b
            combinations[total] += 1
    
    return combinations

def probability_of_sums(combinations):
    total_combinations = sum(combinations.values())
    probabilities = {key: value / total_combinations for key, value in combinations.items()}
    return probabilities

@app.route('/')
def index():
    # Provide default values for Die A and Die B
    default_dieA = 1
    default_dieB = 1

    # Get combinations and probabilities for default values
    combinations = dice_combinations(default_dieA, default_dieB)
    probabilities = probability_of_sums(combinations)

    # Render the template with default values and calculations
    return render_template('indexpartA.html', dieA=default_dieA, dieB=default_dieB, combinations=combinations, probabilities=probabilities)

@app.route('/roll-dice')
def roll_dice():
    dieA = int(request.args.get('dieA', 1))
    dieB = int(request.args.get('dieB', 1))

    combinations = dice_combinations(dieA, dieB)
    probabilities = probability_of_sums(combinations)

    return jsonify({
        'combinations': dict(combinations),
        'probabilities': probabilities
    })

if __name__ == '__main__':
    app.run(debug=True)
