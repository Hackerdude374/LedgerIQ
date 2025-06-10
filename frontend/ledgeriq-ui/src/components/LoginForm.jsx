import React, { useState } from 'react';

function LoginForm() {
  const [username, setUser] = useState('');
  const [password, setPass] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    const res = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ username, password })
    });

    if (res.ok) {
      alert('Login successful');
    } else {
      alert('Login failed');
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input placeholder="Username" onChange={(e) => setUser(e.target.value)} required />
      <input type="password" placeholder="Password" onChange={(e) => setPass(e.target.value)} required />
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginForm;
