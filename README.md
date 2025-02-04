# Disease Prediction using Machine Learning

This project is a web application that predicts the likelihood of three diseases—Diabetes, Heart Disease, and Parkinson's Disease—based on user input. The application is built using Streamlit and leverages pre-trained machine learning models to provide predictions.

## Features

- **Diabetes Prediction**: Predicts the likelihood of diabetes based on factors such as glucose level, blood pressure, BMI, and more.
- **Heart Disease Prediction**: Predicts the likelihood of heart disease based on factors such as age, cholesterol level, resting blood pressure, and more.
- **Parkinson's Disease Prediction**: Predicts the likelihood of Parkinson's disease based on voice measurements and other health-related factors.

## Technologies Used

- **Python**: The core programming language used for the project.
- **Streamlit**: A framework for building web applications with Python.
- **Pickle**: Used for loading pre-trained machine learning models.
- **Machine Learning Models**: Pre-trained models for diabetes, heart disease, and Parkinson's disease prediction.

## Installation

### Clone the Repository:

```bash
git clone https://github.com/your-username/disease-prediction.git
cd disease-prediction
```

### Install Dependencies:

Ensure you have Python installed, then install the required packages using pip:

```bash
pip install streamlit pickle
```

### Run the Application:

Start the Streamlit application by running:

```bash
streamlit run app.py
```

### Access the Application:

Open your web browser and navigate to [http://localhost:8501](http://localhost:8501) to use the application.

## Usage

1. **Select a Disease Prediction Model**:
   Use the sidebar to select between Diabetes, Heart Disease, or Parkinson's Disease prediction.

2. **Input the Required Data**:
   Fill in the input fields with the relevant health data.

3. **Get the Prediction**:
   Click the "Test Result" button to get the prediction. The result will indicate whether the user is likely to have the selected disease.

## Project Structure

- `app.py`: The main application file containing the Streamlit code and model integration.
- `saved-models/`: Directory containing the pre-trained machine learning models.
  - `diabetes_model.sav`: Pre-trained model for diabetes prediction.
  - `heart_disease_model.sav`: Pre-trained model for heart disease prediction.
  - `parkinsons_model.sav`: Pre-trained model for Parkinson's disease prediction.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

The pre-trained models used in this project were trained on publicly available datasets.

Thanks to the Streamlit team for providing an easy-to-use framework for building web applications.

## Contact

For any questions or feedback, please contact [Your Name] at [your-email@example.com].