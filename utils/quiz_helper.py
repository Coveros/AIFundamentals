from IPython.display import HTML, display, clear_output
import html
import json

QUESTIONS = {
    "exercise3": {
        1: {
            "title": "Question 1: What is this fit, and what is the best next step?",
            "prompt": "Looking at the loss curve above, how accurate is the model trained above? Is it overfit, underfit, or just right? As an AI engineer on the team, what is the most logical next step to improve its performance?",
            "options": [
                ("A", "Overfit - add regularization to the model"),
                ("B", "Underfit - increase the model's complexity (e.g., use a deeper network backbone)"),
                ("C", "Just right - ship it!"),
                ("D", "Underfit - train the model on fewer images"),
                ("E", "Overfit - stop training earlier"),
            ],
            "correct": "B",
            "explanation": "High loss on both training and validation sets indicates underfitting. Increasing model complexity allows the network to learn the necessary features.",
        },
        2: {
            "title": "Question 2: What is this fit, and what is the best action now?",
            "prompt": "The more complex model is still underperforming, but the loss curve shows a clear downward trend. What is the best action to take now?",
            "options": [
                ("A", "Overfit - decrease the model's complexity"),
                ("B", "Underfit - train the model for more epochs"),
                ("C", "Just right - ship it!"),
                ("D", "Underfit - add more data to the training set immediately"),
                ("E", "Overfit - make bounding box requirements less strict"),
            ],
            "correct": "B",
            "explanation": "The steady downward loss curve shows the model is actively learning but hasn't converged yet. Training for more epochs gives it time to reach optimal loss.",
        },
        3: {
            "title": "Question 3: What is this fit, and how should you fix it?",
            "prompt": "The model now performs perfectly on the training data but fails on new data. How should you fix this problem?",
            "options": [
                ("A", "Underfit - increase the model's complexity"),
                ("B", "Overfit - add regularization and use early stopping"),
                ("C", "Just right - ship it!"),
                ("D", "Overfit - train even longer"),
                ("E", "Underfit - use only training performance"),
            ],
            "correct": "B",
            "explanation": "A low training loss combined with high validation loss is a classic sign of overfitting. Regularization (like dropout) and early stopping help the model generalize.",
        },
        4: {
            "title": "Question 4: Final model fit assessment",
            "prompt": "How accurate is the model trained above? Is it overfit, underfit, or just right?",
            "options": [
                ("A", "Underfit - add more layers"),
                ("B", "Overfit - add more regularization"),
                ("C", "Inconclusive - restart the whole process"),
                ("D", "Just right - ship it!"),
            ],
            "correct": "D",
            "explanation": "Both training and validation loss are low and closely aligned, showing the model has learned the patterns well without memorizing the training set.",
        },
    },
    "exercise4": {
        1: {
            "title": "Question 1: Automotive Self-driving Car Vision",
            "prompt": "Automotive: Self-driving car 'vision' task",
            "options": ["Object detection", "Classification", "Anomaly detection", "Regression", "Transfer learning", "Clustering"],
            "correct": "Object detection",
            "explanation": "Object detection identifies multiple objects (pedestrians, vehicles, traffic lights) in camera frames and draws bounding boxes around them.",
        },
        2: {
            "title": "Question 2: Healthcare Chest X-ray Analysis",
            "prompt": "Healthcare: Analyze chest X-rays for pneumonia",
            "options": ["Object detection", "Classification", "Anomaly detection", "Regression", "Transfer learning", "Clustering"],
            "correct": "Classification",
            "explanation": "Classification categorizes an input image into distinct classes, such as determining whether a chest X-ray shows pneumonia or not.",
        },
        3: {
            "title": "Question 3: Fraud Detection",
            "prompt": "Fraud Detection: Find fraudulent transactions",
            "options": ["Object detection", "Classification", "Anomaly detection", "Regression", "Transfer learning", "Clustering"],
            "correct": "Anomaly detection",
            "explanation": "Anomaly detection identifies rare or unexpected transaction patterns that deviate significantly from normal user activity.",
        },
        4: {
            "title": "Question 4: Farming Crop Yield Prediction",
            "prompt": "Farming: Predict crop yield",
            "options": ["Object detection", "Classification", "Anomaly detection", "Regression", "Transfer learning", "Clustering"],
            "correct": "Regression",
            "explanation": "Regression models predict continuous numeric values, such as estimating total crop yield quantity based on environmental factors.",
        },
        5: {
            "title": "Question 5: Vision Recognition Dog Breed Classification",
            "prompt": "Vision Recognition: Use a pre-trained image classifier for identifying dog breeds",
            "options": ["Object detection", "Classification", "Anomaly detection", "Regression", "Transfer learning", "Clustering"],
            "correct": "Transfer learning",
            "explanation": "Transfer learning reuses knowledge from a model pre-trained on a large dataset and adapts it to a new, specific task like dog breed classification.",
        },
        6: {
            "title": "Question 6: Retail Customer Segmentation",
            "prompt": "Retail: Group customers into similar segments",
            "options": ["Object detection", "Classification", "Anomaly detection", "Regression", "Transfer learning", "Clustering"],
            "correct": "Clustering",
            "explanation": "Clustering is an unsupervised learning technique that groups data points into clusters based on similarity without relying on pre-existing labels.",
        },
    },
    "exercise5": {
        1: {
            "title": "Question 1: First Step in ML Process",
            "prompt": "Step 1: You have raw data about customer purchases. What's the first thing to do?",
            "options": ["Model monitoring", "Model evaluation", "Feature engineering", "Data extraction", "Model training", "Model serving/deployment", "Model validation", "Data analysis"],
            "correct": "Data extraction",
            "explanation": "Data extraction is the foundational first step where raw data is gathered and integrated from diverse underlying data sources.",
        },
        2: {
            "title": "Question 2: Transforming Data for ML",
            "prompt": "Step 2: You've extracted the data. Now you need to convert it into features that ML models can understand. What is this step called?",
            "options": ["Model monitoring", "Model evaluation", "Feature engineering", "Data extraction", "Model training", "Model serving/deployment", "Model validation", "Data analysis"],
            "correct": "Feature engineering",
            "explanation": "Feature engineering transforms raw attributes into informative numerical inputs and representations suitable for machine learning algorithms.",
        },
        3: {
            "title": "Question 3: Processing Features for Training",
            "prompt": "Step 3: Before feeding features into your model, you need to clean, normalize, and prepare them. This is still part of which ML process step?",
            "options": ["Model monitoring", "Model evaluation", "Feature engineering", "Data extraction", "Model training", "Model serving/deployment", "Model validation", "Data analysis"],
            "correct": "Feature engineering",
            "explanation": "Data cleaning, scaling, and feature preprocessing are core activities within feature engineering that ensure data readiness for training.",
        },
        4: {
            "title": "Question 4: Building Your Model",
            "prompt": "Step 4: Now you feed your prepared data to different algorithms, testing which one performs best. This is called?",
            "options": ["Model monitoring", "Model evaluation", "Feature engineering", "Data extraction", "Model training", "Model serving/deployment", "Model validation", "Data analysis"],
            "correct": "Model training",
            "explanation": "Model training feeds preprocessed feature data into algorithms so they can learn parameters and underlying patterns.",
        },
        5: {
            "title": "Question 5: Testing Your Model",
            "prompt": "Step 5: You've trained a model. Now you test it on separate data to see how accurate it really is. This is called?",
            "options": ["Model monitoring", "Model evaluation", "Feature engineering", "Data extraction", "Model training", "Model serving/deployment", "Model validation", "Data analysis"],
            "correct": "Model evaluation",
            "explanation": "Model evaluation assesses accuracy and generalization by testing the trained model on an independent holdout test set.",
        },
        6: {
            "title": "Question 6: Ensuring Business Goals",
            "prompt": "Step 6: Your model performs well technically, but you need to confirm it meets your business requirements and goals. This is called?",
            "options": ["Model monitoring", "Model evaluation", "Feature engineering", "Data extraction", "Model training", "Model serving/deployment", "Model validation", "Data analysis"],
            "correct": "Model validation",
            "explanation": "Model validation verifies that the selected model satisfies key business criteria and operational constraints prior to rollout.",
        },
        7: {
            "title": "Question 7: Watching Your Model",
            "prompt": "Step 7: Your model is in production, but you need to continuously check its performance and ensure it's working correctly. This is called?",
            "options": ["Model monitoring", "Model evaluation", "Feature engineering", "Data extraction", "Model training", "Model serving/deployment", "Model validation", "Data analysis"],
            "correct": "Model monitoring",
            "explanation": "Model monitoring tracks production performance to detect data drift, model decay, and operational anomalies over time.",
        },
        8: {
            "title": "Question 8: Putting Your Model to Work",
            "prompt": "Step 8: Your model is approved and ready. Now you integrate it into your application and release it to users. This is called?",
            "options": ["Model monitoring", "Model evaluation", "Feature engineering", "Data extraction", "Model training", "Model serving/deployment", "Model validation", "Data analysis"],
            "correct": "Model serving/deployment",
            "explanation": "Model serving/deployment integrates trained models into live software pipelines so end users can make real-time or batch inferences.",
        },
    },
}


def show_question(exercise, q_num, clear=True):
    if clear:
        clear_output(wait=True)

    qdata = QUESTIONS.get(exercise, {}).get(q_num)
    if not qdata:
        display(HTML(f"<p style='color:red;'>Question {q_num} for {exercise} not found.</p>"))
        return

    q_id = f"{exercise}_q{q_num}"
    title = html.escape(qdata["title"])
    prompt = html.escape(qdata["prompt"])
    correct_val = html.escape(qdata["correct"])
    explanation_json = json.dumps(qdata.get("explanation", ""))

    options_html = ""
    for opt in qdata["options"]:
        if isinstance(opt, tuple):
            val, text = opt
            val_esc = html.escape(val)
            text_esc = html.escape(text)
            options_html += f"""
    <label style="display: block; margin: 10px 0; cursor: pointer; color: #000000;">
      <input type="radio" name="{q_id}" value="{val_esc}" style="margin-right: 10px;"> <strong>{val_esc})</strong> {text_esc}
    </label>"""
        else:
            val_esc = html.escape(opt)
            options_html += f"""
    <label style="display: block; margin: 10px 0; cursor: pointer; color: #000000;">
      <input type="radio" name="{q_id}" value="{val_esc}" style="margin-right: 10px;"> {val_esc}
    </label>"""

    html_code = f"""
<div style="font-family: Arial, sans-serif; max-width: 700px; padding: 20px; background: #ffffff; color: #000000; border-radius: 8px; border: 1px solid #cccccc; margin-top: 10px;">
  <h3 style="margin-top: 0; color: #000000;">{title}</h3>
  <p style="color: #000000; line-height: 1.6;">{prompt}</p>
  
  <div style="margin: 15px 0;">
    {options_html}
  </div>
  
  <button onclick="window.submit_{q_id}()" style="padding: 10px 20px; background: #0066cc; color: #ffffff; border: none; border-radius: 4px; cursor: pointer; font-size: 14px; font-weight: bold;">Submit Answer</button>
  <div id="{q_id}_output" style="margin-top: 15px; padding: 12px; border-left: 4px solid; display: none; border-radius: 3px; font-size: 14px;"></div>
</div>

<script>
window.submit_{q_id} = function() {{
  const selected = document.querySelector('input[name="{q_id}"]:checked');
  const output = document.getElementById('{q_id}_output');
  if (selected) {{
    const correctVal = '{correct_val}';
    const explanation = {explanation_json};
    const isCorrect = selected.value === correctVal;
    const border = isCorrect ? '#28a745' : '#dc3545';
    const bgColor = isCorrect ? '#d4edda' : '#f8d7da';
    const textColor = isCorrect ? '#155724' : '#721c24';
    const msg = isCorrect 
      ? '✓ <strong>Correct!</strong> ' + explanation 
      : '✗ <strong>Incorrect.</strong> Try again!';
    output.style.borderColor = border;
    output.style.backgroundColor = bgColor;
    output.style.color = textColor;
    output.innerHTML = msg;
    output.style.display = 'block';
  }} else {{
    alert('Please select an answer before submitting.');
  }}
}};
</script>
"""
    display(HTML(html_code))

