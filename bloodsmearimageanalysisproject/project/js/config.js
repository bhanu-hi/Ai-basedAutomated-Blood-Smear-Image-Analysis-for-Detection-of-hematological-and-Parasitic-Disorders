// Base URL for API requests
export const API_BASE = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000/api' 
    : '/api';

// Common headers for API requests
export const API_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
};

// Common fetch options
export const fetchOptions = (method, data = null) => ({
    method,
    headers: API_HEADERS,
    body: data ? JSON.stringify(data) : undefined,
    credentials: 'include' // Important for cookies if using sessions
});
