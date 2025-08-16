import pandas as pd
import random
import matplotlib.pyplot as plt



brands = ["HP", "ASUS", "Lenovo", "Dell", "Acer", "MSI", "Apple", "Samsung", "Realme", "Redmi"]
models = ["IdeaPad", "Inspiron", "Vivobook", "MacBook Air", "MacBook Pro", "Galaxy Book", "Aspire", "Pavilion", "ThinkPad", "ROG"]
processors = ["i3", "i5", "i7", "i9", "Ryzen 3", "Ryzen 5", "Ryzen 7"]

fake_data = []
for i in range(50):
    brand = random.choice(brands)
    model = random.choice(models)
    processor = random.choice(processors)
    price = f"₹{random.randint(25000, 95000)}"
    rating = round(random.uniform(3.5, 5.0), 1)
    reviews = f"{random.randint(500,5000)} Ratings & {random.randint(50,800)} Reviews"
    link = f"https://www.flipkart.com/{brand.lower()}-{model.lower().replace(' ','-')}-{i}"
    
    fake_data.append({
        "Name": f"{brand} {model} {processor}",
        "Price": price,
        "Rating": rating,
        "Reviews": reviews,
        "Link": link
    })

# Save dataset
csv_file = "flipkart_products_large_sample.csv"
df = pd.DataFrame(fake_data)
df.to_csv(csv_file, index=False, encoding="utf-8")
print(f"✅ Dataset saved to {csv_file} with {len(df)} records")

# -------------------------------
# Step 2: Load and Clean Dataset
# -------------------------------
df = pd.read_csv(csv_file)

# Clean price (remove ₹ and commas, convert to int)
df["Price"] = df["Price"].replace("₹", "", regex=True).replace(",", "", regex=True).astype(int)

# Extract brand name
df["Brand"] = df["Name"].apply(lambda x: x.split()[0])



# 1. Price distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10, edgecolor="black", color="skyblue")
plt.title("Price Distribution of Flipkart Products")
plt.xlabel("Price (₹)")
plt.ylabel("Number of Products")
plt.show()

# 2. Average rating per brand
brand_ratings = df.groupby("Brand")["Rating"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
brand_ratings.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Average Rating per Brand")
plt.xlabel("Brand")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.show()

# 3. Price vs Rating scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Price"], df["Rating"], alpha=0.7, color="green")
plt.title("Price vs Rating of Flipkart Products")
plt.xlabel("Price (₹)")
plt.ylabel("Rating")
plt.grid(True)
plt.show()
