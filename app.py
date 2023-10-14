import logging
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Question

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


# Регистрация маршрутов Flask
@app.route('/api/questions', methods=['POST'])
def get_questions():
    try:
        data = request.get_json()
        questions_num = data.get('questions_num', 1)
        questions = []

        while len(questions) < questions_num:
            try:
                response = requests.get(f'https://jservice.io/api/random?count={questions_num}')
                question_data = response.json()[0]
                question_id = question_data['id']
                question_text = question_data['question']
                answer_text = question_data['answer']

                existing_question = Question.query.filter_by(question_id=question_id).first()

                if existing_question is None:
                    new_question = Question(question_id=question_id, question_text=question_text,
                                            answer_text=answer_text)
                    db.session.add(new_question)
                    db.session.commit()
                    questions.append({
                        'id': new_question.id,
                        'question_text': new_question.question_text,
                        'answer_text': new_question.answer_text,
                        'created_at': new_question.created_at
                    })
            except requests.exceptions.RequestException as err:
                # Логироваание ошибки при запросе к внешнему API
                logging.error(f'Error making to external API {str(err)}')

        logging.info(f'Response sent with {len(questions)} questions')
        return jsonify(questions)

    except Exception as error:
        # Обработка остльных ошибок
        logging.error(f'Error {str(error)}')
        return jsonify({'error': 'Internet server error'}), 500


# Обрботка ошибки 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


# Обработка ошибки 500
@app.errorhandler(500)
def internet_server_error(error):
    return jsonify({'error': 'Interner Server Error'}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')