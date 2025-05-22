from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recipe = ""
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        prompt = (
            f"Generate a detailed, step-by-step cooking recipe using the following ingredients: {ingredients}. "
            f"The recipe should include a name, ingredients list with quantities, preparation steps, cooking time, and servings."
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful and creative chef."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=700,
                temperature=0.7
            )
            recipe = response['choices'][0]['message']['content']
        except Exception as e:
            recipe = f"Error: {str(e)}"
    return render_template('index.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
