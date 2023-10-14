from app import db

# Определение моделей SQLAlchemy
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True, nullbel=False)
    question_text = db.Column(db.String(500), nullabel=False)
    answer_text = db.Column(db.String(500), nulllabel=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Question {self.question_text}>'