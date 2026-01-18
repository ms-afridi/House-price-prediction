🏠 Apartment Rent Prediction App
A machine learning-powered web application that predicts apartment rental prices in major Indian cities using LightGBM algorithm.
Overview
This project uses a trained LightGBM (Light Gradient Boosting Machine) model to estimate apartment rental prices based on various features like location, size, furnishing status, and amenities. The interactive web interface is built with Streamlit, making it easy for users to get instant rent predictions.
Features

Interactive Web Interface: User-friendly sliders and dropdowns for inputting apartment details
Real-time Predictions: Instant rent estimates based on your input parameters
Multiple City Support: Covers major Indian cities including Kolkata, Mumbai, Bangalore, Delhi, Chennai, and Hyderabad
Comprehensive Parameters: Takes into account 10 different features for accurate predictions

Dataset
The model is trained on the House_Rent_Dataset.csv which includes rental data from various Indian cities with features such as:

Number of bedrooms (BHK)
City location
Furnishing status
Tenant preferences
Number of bathrooms
Point of contact
Floor details
Apartment size
Rent per square foot

Input Features
The application accepts the following inputs:

BHK: Number of bedrooms (1-6)
City: Kolkata, Mumbai, Bangalore, Delhi, Chennai, Hyderabad
Furnishing Status: Unfurnished, Semi-Furnished, Furnished
Tenant Preferred: Bachelors/Family, Bachelors, Family
Bathroom: Number of bathrooms (1-7)
Point of Contact: Contact Owner, Contact Agent
Rental Floor: Floor number (2 to 22)
Total Number of Floors: Total floors in building (0-30)
Fixed Size: Apartment size in square feet (10-3100)
Square Feet Rent: Rent per square foot (10-120)

Installation

Clone this repository:

bashgit clone https://github.com/ms-afridi/apartment-rent-prediction.git
cd apartment-rent-prediction

Install required dependencies:

pip install -r requirements.txt
```

```

## Project Structure
```
apartment-rent-prediction/
│
├── app.py                      # Streamlit web application
├── lgbm_model.pkl             # Trained LightGBM model
├── House_Rent_Dataset.csv     # Training dataset
├── House_Rent.ipynb           # Model training notebook
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
How It Works

The user inputs apartment details through the Streamlit interface
The input data is formatted into a pandas DataFrame
The pre-trained LightGBM model processes the features
The model outputs a rental price prediction in INR
The result is displayed to the user with proper formatting

Future Enhancements

Add more cities and regions
Include amenities like parking, gym, pool
Implement price trends and visualizations
Add comparison feature for multiple properties
Deploy to cloud platforms (Heroku, Streamlit Cloud, AWS)

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is open source and available under the MIT License.
Author
ms-afridi
Acknowledgments

Dataset source: House Rent Dataset
Built with Streamlit and LightGBM
Inspired by the need for transparent rental pricing in Indian metropolitan cities
