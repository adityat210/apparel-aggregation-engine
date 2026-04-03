"use client";

import { useEffect, useMemo, useState } from "react";

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

  const [retailer, setRetailer] = useState("");
  const [category, setCategory] = useState("");
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
  const [inStockOnly, setInStockOnly] = useState(false);
  const [sortBy, setSortBy] = useState("");

  const retailerOptions = useMemo(() => ["retailer_a", "retailer_b"], []);
  const categoryOptions = useMemo(() => ["tops", "outerwear", "bottoms"], []);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        setIsLoading(true);
        setError(null);

        const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
        const params = new URLSearchParams();

        if (retailer) params.set("retailer", retailer);
        if (category) params.set("category", category);
        if (minPrice) params.set("min_price", minPrice);
        if (maxPrice) params.set("max_price", maxPrice);
        if (inStockOnly) params.set("in_stock", "true");
        if (sortBy) params.set("sort_by", sortBy);

        const queryString = params.toString();
        const url = queryString ? `${baseUrl}/products?${queryString}` : `${baseUrl}/products`;

        const response = await fetch(url);

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
  }, [retailer, category, minPrice, maxPrice, inStockOnly, sortBy]);

  const resetFilters = () => {
    setRetailer("");
    setCategory("");
    setMinPrice("");
    setMaxPrice("");
    setInStockOnly(false);
    setSortBy("");
  };

  return (
    <main style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ marginBottom: "0.5rem" }}>Apparel Aggregation & Discovery Engine</h1>
      <p style={{ marginBottom: "1.5rem", color: "#555" }}>
        Browse apparel products aggregated from multiple retailers.
      </p>

      <section
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
          gap: "0.75rem",
          marginBottom: "1.5rem",
          padding: "1rem",
          border: "1px solid #333",
          borderRadius: "12px",
          backgroundColor: "#111",
        }}
      >
        <div>
          <label style={{ display: "block", marginBottom: "0.35rem" }}>Retailer</label>
          <select
            value={retailer}
            onChange={(e) => setRetailer(e.target.value)}
            style={{ width: "100%", padding: "0.6rem", borderRadius: "8px" }}
          >
            <option value="">All retailers</option>
            {retailerOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label style={{ display: "block", marginBottom: "0.35rem" }}>Category</label>
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            style={{ width: "100%", padding: "0.6rem", borderRadius: "8px" }}
          >
            <option value="">All categories</option>
            {categoryOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label style={{ display: "block", marginBottom: "0.35rem" }}>Min Price</label>
          <input
            type="number"
            value={minPrice}
            onChange={(e) => setMinPrice(e.target.value)}
            placeholder="0"
            style={{ width: "100%", padding: "0.6rem", borderRadius: "8px" }}
          />
        </div>

        <div>
          <label style={{ display: "block", marginBottom: "0.35rem" }}>Max Price</label>
          <input
            type="number"
            value={maxPrice}
            onChange={(e) => setMaxPrice(e.target.value)}
            placeholder="100"
            style={{ width: "100%", padding: "0.6rem", borderRadius: "8px" }}
          />
        </div>

        <div>
          <label style={{ display: "block", marginBottom: "0.35rem" }}>Sort By</label>
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            style={{ width: "100%", padding: "0.6rem", borderRadius: "8px" }}
          >
            <option value="">Default order</option>
            <option value="price_asc">Price: Low to High</option>
            <option value="price_desc">Price: High to Low</option>
            <option value="rating_desc">Rating: High to Low</option>
          </select>
        </div>


        <div style={{ display: "flex", alignItems: "end" }}>
          <label style={{ display: "flex", gap: "0.5rem", alignItems: "center" }}>
            <input
              type="checkbox"
              checked={inStockOnly}
              onChange={(e) => setInStockOnly(e.target.checked)}
            />
            In stock only
          </label>
        </div>

        <div style={{ display: "flex", alignItems: "end" }}>
          <button
            onClick={resetFilters}
            style={{
              width: "100%",
              padding: "0.7rem",
              borderRadius: "8px",
              border: "none",
              cursor: "pointer",
              fontWeight: 600,
            }}
          >
            Reset Filters
          </button>
        </div>
      </section>

      <p style={{ marginBottom: "1rem", color: "#aaa" }}>
        Showing {products.length} products
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
                backgroundColor: "#ffffff",
                color: "#111111",
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