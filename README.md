# **Streamlit Dashboard - Multi-Tab Application with Modular Code Design**

This repository contains a multi-tab application built with [Streamlit](https://streamlit.io/), designed for interactive data visualization and user-friendly interfaces. The application leverages `st.tabs` for a clean and intuitive navigation experience.

## **Features**

- **Tab-Based Navigation**: Users can switch between tabs for different content and functionality.
- **Two-Column Layout**:
  - **First Column (1:3 ratio)**: Contains reusable components such as:
    - **Date Range Picker**: Select a date range for filtering data.
    - **Dropdown Filter**: Choose from predefined options.
    - **Multi-Select Filter**: Select multiple items from a list.
  - **Second Column**: Displays tab-specific content and visualizations.
- **Modular Code Design**:
  - Shared components are encapsulated in reusable functions for consistency and maintainability.
  - Each tab's logic is stored in a separate module for easy scalability.

## **Technologies Used**
- **Streamlit**: For building the user interface.
- **Python**: For backend logic and data manipulation.

## **Directory Structure**
```plaintext
streamlit_app/
├── components/
│   └── common_components.py    # Reusable components like filters
├── pages/
│   ├── tab_one.py              # Logic for Tab One
│   ├── tab_two.py              # Logic for Tab Two
├── main.py                     # Entry point for the application
```
## **Clone this repository:**
git clone https://github.com/kython220282/dashboard.git
cd streamlit-app

## **Install dependencies:**
pip install -r requirements.txt
