<h2>How to run </h2>
<h3>1. Install python</h3>
if python is not install in your system go to
https://www.python.org/downloads and install it
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
<h3>6. Run server</h3>
<small># migrate </small>
<p>python manage.py migrate</p>
<small>#run server</small>
<p>python manage.py runserver</p>
<h4> open http://127.0.0.1:8000/ </h4>
<p>now you can see the home page</p>
<img src="https://i.imgur.com/WWvTA5F.png" alt="">
<p> more items</p>
<img src="https://i.imgur.com/AUvejNM.png" alt="">

