import bcrypt

class User:
    def __init__(self, user_id: int, name: str, email: str, password: str, is_admin: bool = False):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = self.hash_password(password)
        self.is_admin = is_admin

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def record_breathing_audio(self, audio_file: str):
        # Method to record user's breathing audio
        pass

class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions_for_user(self, user_id: int):
        return [transaction for transaction in self.transactions if transaction.user.user_id == user_id]

class MLTask:
    def __init__(self, task_id: int, model: MLModel, audio_data):
        self.task_id = task_id
        self.model = model
        self.audio_data = audio_data

    def execute(self):
        # Logic to execute the ML task
        pass

class PredictionHistory:
    def __init__(self):
        self.predictions = []

    def add_prediction(self, prediction):
        self.predictions.append(prediction)

    def get_predictions_for_user(self, user_id: int):
        return [prediction for prediction in self.predictions if prediction.user.user_id == user_id]
