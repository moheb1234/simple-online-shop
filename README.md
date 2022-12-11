<h2>How to run </h2>
<h3>1. Install python</h3>
<p>if python is not install your system go to 
<a>https://www.python.org/downloads</a> and install it</p>
<h3>2. Clone repository </h3>
<p>git clone https://github.com/moheb1234/simple-online-shop.git</p>
<h3>3. Setup virtual environment</h3>
<p>open terminal cmd and cd to your project directory</p>
<small> # Install virtual environment</small>
<p>python -m venv venv</p>
<small># activate venv (for windows)</small>
<p>venv\Scripts\activate</p>
<h3>4. Install requirements</h3>
pip install -r requirements.txt
<h3>5. Load Sample Data</h3>
<p>now you can run server, but before you can load sample 
product in database for testing</p>
<small># load product with random price</small>
<p>python manage.py loadprodcts </p>
<small># delete all products</small>
<p>python manage.py deleteproducts </p>

