# Ax the Gender Tax

For more information, visit the site:
http://ax-gender-tax.herokuapp.com

Requirements for Capstone Project Satisfied:

1. *Business Objective*: Users are consumers who want to make smarter choices about the products they buy. The app is aimed to help guide potential purchase decisions and give consumers more information about the potential gender tax they may be paying for. It specifically informs them what gendered descriptions/features that are costing more for so they can decide whether it is worth it. For example, the app tells them they are potentially paying about $0.8 of a pink tax based on the product description. Perhaps that’s enough for them to decide against it. But they also get to see words in the description what likely contributed most to that pink tax and then actively choose to pay the extra for “antioxidant”, “moisturisers”. Or if the other hand, if they see the word “beauty”, “perfect” as the main contributors to the markup instead, they may choose otherwise.

2. *Data Ingestion*: The project involved a lot of data processing beyond simply loading an existing data set.  This involved gathering data through API calls from multiple sources: from Amazon Product Advertising API, and then the Walmart Open API. There is non-trivial processing the data sets as much reformatting and other NLP techniques were necessary.  The project also found a unique perspective on that data via the gender divide.

3. *Visualizations*: The project contain at least two distinct types of visualizations.  A main scatter plots with cost and degree of “gender” as axis, bar charts highlighting the most informative words, and also histograms of costs. These were produced with Matplotlib/ Pandas but mostly Bokeh for some level of interactivity/ customization.

a. *Machine Learning*: The project included the creation and use of multiple machine learning models.  The project involved natural language processing to generate a categorized corpus of product descriptions. A naive bayes classifier was built and trained for classification of product description as intending for female or male consumers. And finally a regression of price based on the the language features, was created and cross validated. Several different linear and nonlinear models ranging from Lasso, Ridge, Random Forest, to Multi-layer perceptrons, were tested in combination with different vectorizing approaches.

b. *Interactive Website*: The project resulted in a website that allows users to interact with the data.  This is in the form of an interactive exploration of the data and a customized model predictions and analysis for users. This interactivity is server-side, via Flask. I also took care to make it mobile display friendly.

5. *Deliverable*: A deliverable that describe the work performed on the capstone as well as its primary results is in the form of a website and multiple Jupyter notebooks in analyses.  It describes the tools used, the process of data ingestion and analysis, and the major results.  It include the visualizations of point 3.  
