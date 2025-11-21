from flask import Flask, render_template_string

app = Flask(__name__)

# Sample products
products = [
    {"id": 1, "name": "Wireless Headphones", "price": "$49.99", "image": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Smart Watch", "price": "$79.99", "image": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Gaming Mouse", "price": "$29.99", "image": "https://via.placeholder.com/150"},
]

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shopping Home</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Roboto', sans-serif; background-color: #f3f3f3; margin:0; }
            .navbar { background-color:#131921; color:white; padding:15px 25px; display:flex; align-items:center; }
            .navbar h1 { margin:0; font-size:24px; }
            .container { padding:50px; text-align:center; }
            .products { display:flex; justify-content:center; gap:20px; flex-wrap:wrap; }
            .product-card { background:white; padding:20px; border-radius:10px; width:200px; box-shadow:0px 3px 8px rgba(0,0,0,0.2); text-align:center; }
            .product-card img { width:100%; border-radius:8px; }
            .product-card h3 { font-size:18px; margin:10px 0; }
            .product-card p { color:#0f1111; margin:5px 0; }
            .footer { margin-top:60px; font-size:14px; color:#555; text-align:center; }
        </style>
    </head>
    <body>
        <div class="navbar"><h1>Amazon-Style Store</h1></div>
        <div class="container">
            <h2>Welcome to My Shopping Website</h2>
            <div class="products">
            {% for product in products %}
                <div class="product-card">
                    <img src="{{ product.image }}" alt="{{ product.name }}">
                    <h3>{{ product.name }}</h3>
                    <p>{{ product.price }}</p>
                </div>
            {% endfor %}
            </div>
        </div>
        <div class="footer">© 2025 My-Shopping-App — Inspired by Amazon UI</div>
    </body>
    </html>
    '''
    return render_template_string(html, products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
