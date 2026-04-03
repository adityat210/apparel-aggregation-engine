"use client";

import { useEffect, useState } from "react";

type Product = {
  id: number;
  retailer: string;
  external_id: string;
  name: string;
  brand: string | null;
  category: string | null;
  color: string | null;
  price: number;
  currency: string;
  material: string | null;
  image_url: string | null;
  product_url: string;
  rating: number | null;
  review_count: number | null;
  in_stock: boolean;
};

export default function HomePage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
        const response = await fetch(`${baseUrl}/products`);

        if (!response.ok) {
          throw new Error("Failed to fetch products.");
        }

        const data: Product[] = await response.json();
        setProducts(data);
      } catch (err) {
        setError("Unable to load products from the backend.");
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchProducts();
  }, []);

  return (
    <main style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ marginBottom: "0.5rem" }}>Apparel Aggregation & Discovery Engine</h1>
      <p style={{ marginBottom: "2rem", color: "#555" }}>
        Browse apparel products aggregated from multiple retailers.
      </p>

      {isLoading && <p>Loading products...</p>}
      {error && <p style={{ color: "crimson" }}>{error}</p>}

      {!isLoading && !error && (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
            gap: "1rem",
          }}
        >
          {products.map((product) => (
            <div
              key={product.id}
              style={{
                border: "1px solid #ddd",
                borderRadius: "12px",
                padding: "1rem",
                backgroundColor: "#fff",
                color: "#111",
                boxShadow: "0 2px 6px rgba(0, 0, 0, 0.06)",
              }}
            >
              <p style={{ fontSize: "0.85rem", color: "#666", marginBottom: "0.5rem" }}>
                {product.retailer}
              </p>

              <h2 style={{ fontSize: "1.1rem", marginBottom: "0.5rem" }}>{product.name}</h2>

              <p style={{ marginBottom: "0.25rem" }}>
                <strong>Brand:</strong> {product.brand ?? "N/A"}
              </p>
              <p style={{ marginBottom: "0.25rem" }}>
                <strong>Category:</strong> {product.category ?? "N/A"}
              </p>
              <p style={{ marginBottom: "0.25rem" }}>
                <strong>Price:</strong> ${product.price.toFixed(2)}
              </p>
              <p style={{ marginBottom: "0.25rem" }}>
                <strong>Rating:</strong> {product.rating ?? "N/A"}
              </p>
              <p style={{ marginBottom: "0.75rem" }}>
                <strong>Status:</strong> {product.in_stock ? "In Stock" : "Out of Stock"}
              </p>

              <a
                href={product.product_url}
                target="_blank"
                rel="noreferrer"
                style={{ color: "#0a66c2", textDecoration: "none", fontWeight: 600 }}
              >
                View Product
              </a>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}