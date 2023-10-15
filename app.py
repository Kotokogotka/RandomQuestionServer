import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True, nullable=False)
    question_text = db.Column(db.String(500), nullable=False)
    answer_text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Question {self.question_text}>'

@app.route('/api/questions', methods=['POST'])
def get_questions():
    data = request.get_json()
    questions_num = data.get('questions_num', 1)
    questions = []

    while len(questions) < questions_num:
        response = requests.get(f'https://jservice.io/api/random?count={questions_num}')
        question_data = response.json()[0]
        question_id = question_data['id']
        question_text = question_data['question']
        answer_text = question_data['answer']

        existing_question = Question.query.filter_by(question_id=question_id).first()

        if existing_question is None:
            new_question = Question(question_id=question_id, question_text=question_text, answer_text=answer_text)
            db.session.add(new_question)
            db.session.commit()
            questions.append({
                'id': new_question.id,
                'question_text': new_question.question_text,
                'answer_text': new_question.answer_text,
                'created_at': new_question.created_at
            })

    return jsonify(questions)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
