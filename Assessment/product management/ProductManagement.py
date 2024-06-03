import tkinter as tk
from tkinter import messagebox,ttk
import pymysql

# Database connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="product_management",
)

cursor = db.cursor()

#Main Application Window
class ProductManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management System")
        self.root.geometry("600x400")
        self.root.config(bg='lightgray')
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Product Management System", bg='orange', fg='white', font='Lucida 20 bold', width=100).pack(pady=0)
        tk.Button(self.root, text="Admin Login", bg='orange', fg='white', font='Lucida 15' , command=self.admin_login, width=20).pack(pady=20)
        tk.Button(self.root, text="Admin Register", bg='orange', fg='white', font='Lucida 15' , command=self.admin_register, width=20).pack(pady=20)
        tk.Button(self.root, text="User Login", bg='orange', fg='white', font='Lucida 15' , command=self.user_login, width=20).pack(pady=20)
        tk.Button(self.root, text="User Register", bg='orange', fg='white', font='Lucida 15' , command=self.user_register, width=20).pack(pady=20)

    def admin_login(self):
        self.clear_window()
        tk.Label(self.root, text="Admin Login", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)
        
        tk.Label(self.root, text="Name :", bg='lightgray', font='Lucida 12').place(x=180, y=70)
        self.admin_name = tk.Entry(self.root)
        self.admin_name.pack(pady=40)

        tk.Label(self.root, text="Contact :", bg='lightgray', font='Lucida 12').place(x=170, y=130)
        self.admin_contact = tk.Entry(self.root)
        self.admin_contact.pack()

        tk.Button(self.root, text="Login", command=self.validate_admin_login, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.main_menu, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=5)

    def admin_register(self):
        self.clear_window()
        tk.Label(self.root, text="Admin Register", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        tk.Label(self.root, text="Name :", bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=40)
        self.reg_admin_name = tk.Entry(self.root)
        self.reg_admin_name.place(x=90, y=43)

        tk.Label(self.root, text="Contact :", bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=70)
        self.reg_contact = tk.Entry(self.root)
        self.reg_contact.place(x=90, y=72)

        tk.Label(self.root, text="Email :", bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=100)
        self.reg_email = tk.Entry(self.root)
        self.reg_email.place(x=90, y=104)

        self.gender_var = tk.IntVar()
        tk.Label(self.root, text="Gender : ",bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=130)
        self.reg_male = tk.Radiobutton(self.root, text='Male', variable=self.gender_var, value=0, bg='lightgray', fg='Black', font='Lucida 10')
        self.reg_male.place(x=90, y=130)
        self.reg_female = tk.Radiobutton(self.root, text='Female', variable=self.gender_var, value=1, bg='lightgray', fg='Black', font='Lucida 10')
        self.reg_female.place(x=150, y=130)

        tk.Label(self.root, text="City : ",bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=160)
        self.city = tk.Entry(self.root)
        self.city.place(x=90, y=163)

        tk.Label(self.root, text="State : ",bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=190)
        self.state = tk.Entry(self.root)
        self.state.place(x=90, y=193)
        
        tk.Button(self.root, text="Register", command=self.create_admin_account, bg='orange', fg='white', font='Lucida 10', width=15).place(x=50, y=250)
        tk.Button(self.root, text="Back", command=self.main_menu, bg='orange', fg='white', font='Lucida 10', width=15).place(x=50, y=300)

    def user_login(self):
        self.clear_window()
        tk.Label(self.root, text="User Login", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        tk.Label(self.root, text="Name :", bg='lightgray', font='Lucida 12').place(x=180, y=70)
        self.user_name = tk.Entry(self.root)
        self.user_name.pack(pady=40)

        tk.Label(self.root, text="Contact :", bg='lightgray', font='Lucida 12').place(x=170, y=130)
        self.user_contact = tk.Entry(self.root)
        self.user_contact.pack()

        tk.Button(self.root, text="Login", command=self.validate_user_login, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.main_menu, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=5)

    def user_register(self):
        self.clear_window()
        tk.Label(self.root, text="User Register", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        tk.Label(self.root, text="Name :", bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=40)
        self.reg_user_name = tk.Entry(self.root)
        self.reg_user_name.place(x=90, y=43)

        tk.Label(self.root, text="Contact :", bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=70)
        self.user_contact = tk.Entry(self.root)
        self.user_contact.place(x=90, y=72)

        tk.Label(self.root, text="Email :", bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=100)
        self.user_email = tk.Entry(self.root)
        self.user_email.place(x=90, y=104)

        self.user_gender_var = tk.IntVar()
        tk.Label(self.root, text="Gender : ",bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=130)
        self.user_male = tk.Radiobutton(self.root, value=0,text='Male',bg='lightgray',fg='Black',font='Lucida 10', variable=self.user_gender_var)
        self.user_male.place(x=90, y=130)
        self.user_female = tk.Radiobutton(self.root, value=1,text='Female',bg='lightgray',fg='Black',font='Lucida 10', variable=self.user_gender_var)
        self.user_female.place(x=150, y=130)

        tk.Label(self.root, text="City : ",bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=160)
        self.user_city = tk.Entry(self.root)
        self.user_city.place(x=90, y=163)

        tk.Label(self.root, text="State : ",bg='lightgray',fg='black',font='Lucida 12').place(x=20, y=190)
        self.user_state = tk.Entry(self.root)
        self.user_state.place(x=90, y=193)
        
        tk.Button(self.root, text="Register", command=self.create_user_account, bg='orange', fg='white', font='Lucida 10', width=15).place(x=50, y=250)
        tk.Button(self.root, text="Back", command=self.main_menu, bg='orange', fg='white', font='Lucida 10', width=15).place(x=50, y=300)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def validate_admin_login(self):
        name = self.admin_name.get()
        contact = self.admin_contact.get()  

        cursor.execute("SELECT * FROM admin WHERE name=%s AND contact=%s", (name, contact))
        result = cursor.fetchone()

        if result:
            self.admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def validate_user_login(self):
        name = self.user_name.get()
        contact = self.user_contact.get()

        cursor.execute("SELECT * FROM users WHERE name=%s AND contact=%s", (name, contact))
        result = cursor.fetchone()

        if result:
            self.user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def create_admin_account(self):
        name = self.reg_admin_name.get()
        contact = self.reg_contact.get()
        email = self.reg_email.get()
        gender = self.gender_var.get()
        city = self.city.get()
        state = self.state.get()

        cursor.execute("INSERT INTO admin (name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)", (name, contact, email, gender, city, state))
        db.commit()
        messagebox.showinfo("Success", "Admin account created successfully")
        self.main_menu()

    def create_user_account(self):
        name = self.reg_user_name.get()
        contact = self.user_contact.get()
        email = self.user_email.get()
        gender = self.user_gender_var.get()
        city = self.user_city.get()
        state = self.user_state.get()

        cursor.execute("INSERT INTO users (name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)", (name, contact, email, gender, city, state))
        db.commit()
        messagebox.showinfo("Success", "Account created successfully")
        self.main_menu()

    def admin_dashboard(self):
        self.clear_window()
        tk.Label(self.root, text="Admin Dashboard", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)
       
        tk.Button(self.root, text="Add Product", command=self.add_product, bg='orange', fg='white',font='Lucida 15', width=25).pack(pady=15)
        tk.Button(self.root, text="Update Product", command=self.update_product, bg='orange', fg='white',font='Lucida 15', width=25).pack(pady=15)
        tk.Button(self.root, text="Delete Product", command=self.delete_product, bg='orange', fg='white',font='Lucida 15', width=25).pack(pady=15)
        tk.Button(self.root, text="View Products", command=self.view_products, bg='orange', fg='white',font='Lucida 15', width=25).pack(pady=15)
        tk.Button(self.root, text="Logout", command=self.main_menu, bg='orange', fg='white',font='Lucida 15', width=25).pack(pady=15)

    def add_product(self):
        self.clear_window()
        tk.Label(self.root, text="Add Product", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        tk.Label(self.root, text="Product Name :", bg='lightgray', font='Lucida 12').place(x=150, y=50)
        self.prod_name = tk.Entry(self.root)
        self.prod_name.place(x=270, y=54)

        tk.Label(self.root, text="Price :", bg='lightgray', font='Lucida 12').place(x=212, y=80)
        self.prod_price = tk.Entry(self.root)
        self.prod_price.place(x=270, y=84)

        tk.Label(self.root, text="Quantity :", bg='lightgray', font='Lucida 12').place(x=192, y=110)
        self.prod_quantity = tk.Entry(self.root)
        self.prod_quantity.place(x=270, y=114)

        tk.Button(self.root, text="Add Product", command=self.save_product, bg='orange', fg='white', font='Lucida 10', width=15).place(x=130, y=150)
        tk.Button(self.root, text="Back", command=self.admin_dashboard, bg='orange', fg='white', font='Lucida 10', width=15).place(x=280, y=150)

    def save_product(self):
        name = self.prod_name.get()    
        price = self.prod_price.get()
        qty = self.prod_quantity.get()

        cursor.execute("INSERT INTO product (name, price, qty) VALUES (%s, %s, %s)", (name, price, qty))
        db.commit()
        messagebox.showinfo("Success", "Product added successfully")
        self.admin_dashboard()

    def update_product(self):
        self.clear_window()
        tk.Label(self.root, text="Update Product", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)
        
        tk.Label(self.root, text="Enter Product ID :", bg='lightgray', font='Lucida 12').place(x=170, y=60)
        self.prod_id = tk.Entry(self.root)
        self.prod_id.place(x=300, y=63)
        tk.Button(self.root, text="Fetch Details", command=self.fetch_product_details, bg='orange', fg='white', font='Lucida 10', width=15).place(x=230, y=100)

    def fetch_product_details(self):
        prod_id = self.prod_id.get()
        cursor.execute("SELECT * FROM product WHERE id=%s", (prod_id))
        product = cursor.fetchone()

        if product:
            self.clear_window()
            tk.Label(self.root, text="Update Product", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

            tk.Label(self.root, text="Product Name :", bg='lightgray', font='Lucida 12').place(x=150, y=50)
            self.prod_name = tk.Entry(self.root)
            self.prod_name.insert(0, product[1])
            self.prod_name.place(x=270, y=54)

            tk.Label(self.root, text="Price :", bg='lightgray', font='Lucida 12').place(x=212, y=80)
            self.prod_price = tk.Entry(self.root)
            self.prod_price.insert(0, product[2])
            self.prod_price.place(x=270, y=84)

            tk.Label(self.root, text="Quantity :", bg='lightgray', font='Lucida 12').place(x=192, y=110)
            self.prod_quantity = tk.Entry(self.root)
            self.prod_quantity.insert(0, product[3])
            self.prod_quantity.place(x=270, y=114)

            tk.Button(self.root, text="Update", command=lambda: self.save_updated_product(prod_id), bg='orange', fg='white', font='Lucida 10', width=15).place(x=130, y=150)
            tk.Button(self.root, text="Back", command=self.admin_dashboard, bg='orange', fg='white', font='Lucida 10', width=15).place(x=280, y=150)
        else:
            messagebox.showerror("Error", "Product not found")

    def save_updated_product(self, prod_id):
        name = self.prod_name.get()        
        price = self.prod_price.get()
        qty = self.prod_quantity.get()

        cursor.execute("UPDATE product SET name=%s, price=%s, qty=%s WHERE id=%s",
                   (name, price, qty, prod_id))
        db.commit()
        messagebox.showinfo("Success", "Product updated successfully")
        self.admin_dashboard()

    def delete_product(self):
        self.clear_window()
        tk.Label(self.root, text="Delete Product", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        tk.Label(self.root, text="Enter Product ID :", bg='lightgray', font='Lucida 12').place(x=170, y=60)
        self.prod_id = tk.Entry(self.root)
        self.prod_id.place(x=300, y=63)

        tk.Button(self.root, text="Delete", command=self.confirm_delete_product, bg='orange', fg='white', font='Lucida 10', width=15).place(x=150, y=135)
        tk.Button(self.root, text="Back", command=self.admin_dashboard, bg='orange', fg='white', font='Lucida 10', width=15).place(x=300, y=135)

    def confirm_delete_product(self):
        prod_id = self.prod_id.get()
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this product?")

        if confirm:
            cursor.execute("DELETE FROM product WHERE id=%s", (prod_id,))
            db.commit()
            messagebox.showinfo("Success", "Product deleted successfully")
            self.admin_dashboard()

    def view_products(self):
        self.clear_window()
        tk.Label(self.root, text="Product List", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()

        if products:
            columns = ["ID", "Product Name", "Price", "Quantity"]
            self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
            for col in columns:
                self.tree.heading(col, text=col)
            for product in products:
                self.tree.insert("", "end", values=product)
            self.tree.pack()
        else:
            tk.Label(self.root, text="No products available").pack()

        tk.Button(self.root, text="Back", command=self.admin_dashboard, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=10)

    def user_dashboard(self):
        self.clear_window()
        tk.Label(self.root, text="User Dashboard", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        tk.Button(self.root, text="View Products", command=self.view_products_user, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=10)
        tk.Button(self.root, text="Purchase Product", command=self.purchase_product, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.main_menu, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=10)

    def view_products_user(self):
        self.clear_window()
        tk.Label(self.root, text="Product List", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()

        if products:
            columns = ["ID", "Product Name", "Price", "Quantity"]
            self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
            for col in columns:
                self.tree.heading(col, text=col)
            for product in products:
                self.tree.insert("", "end", values=product)
            self.tree.pack()
        else:
            tk.Label(self.root, text="No products available").pack()

        tk.Button(self.root, text="Back", command=self.user_dashboard, bg='orange', fg='white', font='Lucida 10', width=15).pack(pady=10)

    def purchase_product(self):
        self.clear_window()
        tk.Label(self.root, text="Purchase Product", bg='orange', fg='white', font='Lucida 18 bold', width=100).pack(pady=0)

        tk.Label(self.root, text="Enter Product ID :", bg='lightgray', font='Lucida 12').place(x=150, y=80)
        self.prod_id = tk.Entry(self.root)
        self.prod_id.place(x=290, y=83)

        tk.Label(self.root, text="Enter Quantity :", bg='lightgray', font='Lucida 12').place(x=167, y=110)
        self.quantity = tk.Entry(self.root)
        self.quantity.place(x=290, y=113)

        tk.Button(self.root, text="Purchase", command=self.process_purchase, bg='orange', fg='white', font='Lucida 10', width=15).place(x=150, y=160)
        tk.Button(self.root, text="Back", command=self.user_dashboard, bg='orange', fg='white', font='Lucida 10', width=15).place(x=290, y=160)
    
    def process_purchase(self):
        prod_id = self.prod_id.get()
        quantity = int(self.quantity.get())

        cursor.execute("SELECT * FROM product WHERE id=%s", (prod_id,))
        product = cursor.fetchone()

        if product:
            if product[3] >= quantity:  # Check if there is enough stock
                cursor.execute("UPDATE product SET qty=qty-%s WHERE id=%s", (quantity, prod_id))
                db.commit()
                messagebox.showinfo("Success", "Purchase successful")
                self.user_dashboard()
            else:
                messagebox.showerror("Error", "Insufficient stock")
        else:
            messagebox.showerror("Error", "Product not found")

if __name__ == "__main__":
    root = tk.Tk()
    pms = ProductManagementSystem(root)
    root.mainloop()