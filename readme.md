# Text Analysis and Prediction Website

This is a Flask-based website that performs various text analysis and prediction tasks on user-inputted text. The website utilizes the Komprehend API to achieve the functionality of sentiment analysis, named entity recognition analysis, emotion prediction, abuse detection, and key detection. These features provide valuable insights into the content and context of the given text.

## Features

1. **Sentiment Analysis**: This feature analyzes the sentiment of the text, determining whether it is positive, negative, or neutral. It provides an understanding of the overall tone and attitude expressed in the input.

2. **Named Entity Recognition Analysis**: This feature identifies and extracts specific named entities from the text, such as names of people, organizations, locations, and other important entities. It helps in categorizing and extracting meaningful information from the given text.

3. **Emotion Prediction**: This feature predicts the emotional content of the text, categorizing it into various emotions such as happiness, sadness, anger, surprise, fear, and more. It provides insights into the underlying emotions conveyed in the text.

4. **Abuse Detection**: This feature identifies abusive or offensive language present in the text. It helps in moderating content and maintaining a respectful and safe environment.

5. **Key Detection**: This feature extracts the key topics or keywords from the text, helping to understand the main ideas and concepts discussed in the input.

## Requirements

- Python 3.7 or above
- Flask framework
- Komprehend API credentials (API key)

## Installation

1. Clone the repository to your local machine:

```shell
git clone https://github.com/1abhi6/text-analyzer.git
```

2. Navigate to the project directory:

```shell
cd text-analyzer
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Configuration

1. Obtain Komprehend API credentials by signing up on the [Komprehend website](https://komprehend.io/).

2. Create the `config.py` file and add your Komprehend API key `YOUR_API_KEY`:

```python
API_KEY = 'YOUR_API_KEY'
```

## Usage

1. Run the Flask development server:

```shell
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000` to access the website.

3. Register/Login with email and password.

4. Now you will be able to access your dashboard.

5. Select what you want to do.

6. Enter the desired text in the provided input field and select the analysis or prediction feature you want to use.

7. Click the "Submit" or "Analyze" button to process the text.

8. The website will display the output of the selected analysis or prediction task.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This project utilizes the Komprehend API for text analysis and prediction. Visit their [website](https://komprehend.io/) for more information.
- The Flask framework was used for creating the web application. Visit the [Python documentation](https://komprehend.io/api-wrappers) for more details.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

## Contact

For any questions or inquiries, please contact [abhi@getifyme.com].

Feel free to use, modify, and distribute this code for educational or personal use.