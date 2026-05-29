const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const BASE_URL = `${API_BASE_URL}/api/auth`;

export const signup = async (email, password) => {
  const res = await fetch(`${BASE_URL}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  return res.json();
};

export const login = async (email, password) => {
  const res = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  return res.json();
};
