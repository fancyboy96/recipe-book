from flask import flask

app = Flask(__name__)
app.config("SQLALCHEMY_DATABASE_URI") = "sqlite:///recipe.db"

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2500))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    ingredients = db.relationship('Ingredient', back_populates='recipe', cascade="all, delete-orphan")
    steps = db.relationship('Step', back_populates='recipe', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Recipe {self.id}: {self.name}>"

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(200), nullablse=False)

    recipe = db.relationship('Recipe', back_populates='ingredients')

    def __repr__(self):
        return f"<Ingredient {self.id}: {self.name}>"

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    description = db.Column(db.String(2500), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    recipe = db.relationship('Recipe', back_populates='steps')

    def __repr__(self):
        return f"<Step {self.id}: {self.name}>"

@app.route("/", methods = "POST", "GET")
def index():
    if request.method == "POST":
        return "TODO"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)