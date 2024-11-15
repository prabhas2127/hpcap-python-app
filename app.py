from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello, I'm Praful!"

@app.route('/calculate', methods=['GET'])
def calculate():
    
    operation = request.args.get('operation')
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)

   
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero!'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'operation': operation, 'num1': num1, 'num2': num2, 'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
