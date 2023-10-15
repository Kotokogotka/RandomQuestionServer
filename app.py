from typing import List, Dict
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db: SQLAlchemy = SQLAlchemy(app)

class Question(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    question_id: int = db.Column(db.Integer, unique=True, nullable=False)
    question_text: str = db.Column(db.String(500), nullable=False)
    answer_text: str = db.Column(db.String(500), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'<Question {self.question_text}>'

@app.route('/api/questions', methods=['POST'])
def get_questions() -> str:
    data: Dict[str, int] = request.get_json()
    questions_num: int = data.get('questions_num', 1)
    questions: List[Dict[str, any]] = []

    while len(questions) < questions_num:
        response: requests.Response = requests.get(f'https://jservice.io/api/random?count={questions_num}')
        question_data: Dict[str, any] = response.json()[0]
        question_id: int = question_data['id']
        question_text: str = question_data['question']
        answer_text: str = question_data['answer']

        existing_question: Question = Question.query.filter_by(question_id=question_id).first()

        if existing_question is None:
            new_question: Question = Question(question_id=question_id, question_text=question_text, answer_text=answer_text)
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
