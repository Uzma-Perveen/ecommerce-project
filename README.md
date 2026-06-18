🛒 Django E-Commerce Basic Store

A full-stack e-commerce web application built using **Python Django** framework that simulates a real-world online shopping system.

---

## 📖 Overview

This project is a **Basic E-Commerce Store** developed as part of a Django web development course. It covers real-world Django concepts including:

- User Authentication System
- Database Relationships
- Session Handling
- CRUD Operations
- Admin Management Panel

Customers can register, browse products, manage their shopping cart, place orders, and view order history. Admins can manage products, stock, and order statuses through Django's built-in admin panel.

---

## 🚀 Features

### 👤 Customer Side
| Feature | Description |
|---------|-------------|
| ✅ Register | Create a new account with username, email, password |
| ✅ Login / Logout | Secure authentication system |
| ✅ Browse Products | View all products in a grid layout |
| ✅ Search Products | Search products by name |
| ✅ Product Detail | View full product details |
| ✅ Add to Cart | Add products to shopping cart |
| ✅ Manage Cart | Increase, decrease, or remove items |
| ✅ Auto Calculation | Subtotal per item and total bill |
| ✅ Checkout | Place order with one click |
| ✅ Order History | View all previous orders |
| ✅ Order Details | View items inside each order |
| ✅ Out of Stock | Products show "Out of Stock" when unavailable |

### 🛠️ Admin Side
| Feature | Description |
|---------|-------------|
| ✅ Add Products | Add new products with image, price, stock |
| ✅ Edit Products | Update product details and stock |
| ✅ Delete Products | Remove products from store |
| ✅ View All Orders | See every customer order |
| ✅ Update Order Status | Change status: Pending → Confirmed → Delivered |
| ✅ View Order Items | See which products are inside each order |

---

## 🧰 Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.x | Backend Programming Language |
| Django | 5.2 | Web Framework |
| SQLite | Built-in | Database |
| HTML5 | - | Frontend Structure |
| CSS3 | - | Styling & Layout |
| Pillow | 12.x | Image Upload & Handling |
| Git | - | Version Control |
| GitHub | - | Code Repository |

---

## 📁 Project Structure
ecommerce_project/

│

├── ecommerce/                  # Main project configuration

│   ├── init.py

│   ├── settings.py             # Project settings

│   ├── urls.py                 # Main URL configuration

│   ├── asgi.py

│   └── wsgi.py

│

├── store/                      # Main application

│   ├── migrations/             # Database migrations

│   ├── templates/

│   │   └── store/              # HTML templates

│   │       ├── base.html       # Base template (navbar, layout)

│   │       ├── home.html       # Product listing page

│   │       ├── login.html      # Login page

│   │       ├── register.html   # Registration page

│   │       ├── product_detail.html  # Product detail page

│   │       ├── cart.html       # Shopping cart page

│   │       ├── checkout.html   # Checkout page

│   │       ├── order_success.html   # Order success page

│   │       ├── order_history.html   # Order history page

│   │       └── order_detail.html    # Order detail page

│   │

│   ├── init.py

│   ├── admin.py                # Admin panel configuration

│   ├── apps.py

│   ├── forms.py                # Registration form

│   ├── models.py               # Database models

│   ├── urls.py                 # App URL patterns

│   └── views.py                # Page logic & functions

│

├── media/                      # Uploaded product images

├── venv/                       # Virtual environment

├── manage.py                   # Django management script

├── README.md                   # Project documentation

└── .gitignore                  # Git ignore file

---

## 🗄️ Database Models

### Product
| Field | Type | Description |
|-------|------|-------------|
| name | CharField | Product name |
| price | DecimalField | Product price |
| description | TextField | Product description |
| image | ImageField | Product image |
| stock | PositiveIntegerField | Available stock |

### Cart & CartItem
| Field | Type | Description |
|-------|------|-------------|
| user | ForeignKey | Linked to User |
| product | ForeignKey | Linked to Product |
| quantity | PositiveIntegerField | Item quantity |

### Order & OrderItem
| Field | Type | Description |
|-------|------|-------------|
| user | ForeignKey | Linked to User |
| order_id | UUIDField | Unique order identifier |
| status | CharField | Pending / Confirmed / Delivered |
| total | DecimalField | Total order amount |
| created_at | DateTimeField | Order date and time |

### Relationships
User ──── Order ──── OrderItem ──── Product

User ──── Cart  ──── CartItem  ──── Product

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x installed
- pip installed
- Git installed

### 1. Clone the Repository
```bash
git clone https://github.com/Uzma-Perveen/ecommerce-project.git
cd ecommerce-project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 4. Install Required Packages
```bash
pip install django pillow
```

### 5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin Account
```bash
python manage.py createsuperuser
```
Enter your preferred username, email, and password.

### 7. Run the Development Server
```bash
python manage.py runserver
```

---

## 🌐 Usage

Once the server is running, open your browser:

| Page | URL |
|------|-----|
| 🏠 Home / Products | http://127.0.0.1:8000/ |
| 🔐 Login | http://127.0.0.1:8000/login/ |
| 📝 Register | http://127.0.0.1:8000/register/ |
| 🛒 Cart | http://127.0.0.1:8000/cart/ |
| 💳 Checkout | http://127.0.0.1:8000/checkout/ |
| 📦 Order History | http://127.0.0.1:8000/orders/ |
| ⚙️ Admin Panel | http://127.0.0.1:8000/admin/ |

---

## 🛠️ Admin Panel

1. Go to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Add products with name, price, description, image, and stock
4. View and manage all customer orders
5. Update order status from Pending → Confirmed → Delivered

---

## 👩‍💻 Developer

**Uzma Perveen**
- GitHub: [@Uzma-Perveen](https://github.com/Uzma-Perveen)

---

## 📄 License
This project is built for **educational purposes** as part of a Django web development course.

---

## 🙏 Acknowledgements
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/)
