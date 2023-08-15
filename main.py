('''
import eel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Set up Eel
eel.init("web")

# Model and tokenizer initialization
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

@eel.expose
def generate_answer(text, question):
    # Prompt creation
    prompt = "Please answer the following question about this text. Text: " + text + " "

    # Combine prompt and question
    input_text = prompt + question

    # Create input tokens and limit to maximum length
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)

    # Generate model output
    outputs = model.generate(**inputs, max_length=50, num_beams=4, temperature=1.0)

    # Decode and return the output
    decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return decoded_outputs[0] if decoded_outputs else ""

# Run the app
if __name__ == "__main__":
    eel.start("index.html", size=(500, 300))
#
''')






import eel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Set up Eel
eel.init("web")

# Model and tokenizer initialization
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

@eel.expose
def generate_answer(text, question):
    # Prompt creation
    prompt = "Please answer the following question about this text. Text: " + text + " "

    # Combine prompt and question
    input_text = prompt + question

    # Create input tokens and limit to maximum length
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)

    # Generate model output
    outputs = model.generate(**inputs, max_length=50, num_beams=4, temperature=1.0)

    # Decode and return the output
    decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return decoded_outputs[0] if decoded_outputs else ""

# Run the app
if __name__ == "__main__":
    while True:
        eel.start("index.html", size=(500, 300))
