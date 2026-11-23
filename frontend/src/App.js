import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:5000/api';

function App() {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [todos, setTodos] = useState([]);
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const [todoForm, setTodoForm] = useState({ title: '', description: '' });
  const [isLogin, setIsLogin] = useState(true);

  useEffect(() => {
    if (token) {
      loadUser();
      loadTodos();
    }
  }, [token]);

  const loadUser = async () => {
    try {
      const res = await axios.get(`${API_URL}/auth/user`, {
        headers: { 'x-auth-token': token }
      });
      setUser(res.data);
    } catch (err) {
      console.error(err);
      logout();
    }
  };

  const loadTodos = async () => {
    try {
      const res = await axios.get(`${API_URL}/todos`, {
        headers: { 'x-auth-token': token }
      });
      setTodos(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleAuthSubmit = async (e) => {
    e.preventDefault();
    const endpoint = isLogin ? 'login' : 'register';
    
    try {
      const res = await axios.post(`${API_URL}/auth/${endpoint}`, formData);
      localStorage.setItem('token', res.data.token);
      setToken(res.data.token);
      setUser(res.data.user);
      setFormData({ name: '', email: '', password: '' });
    } catch (err) {
      alert(err.response?.data?.msg || 'Authentication failed');
    }
  };

  const handleTodoSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(`${API_URL}/todos`, todoForm, {
        headers: { 'x-auth-token': token }
      });
      setTodos([res.data, ...todos]);
      setTodoForm({ title: '', description: '' });
    } catch (err) {
      alert('Failed to create todo');
    }
  };

  const toggleComplete = async (id, completed) => {
    try {
      const res = await axios.put(
        `${API_URL}/todos/${id}`,
        { completed: !completed },
        { headers: { 'x-auth-token': token } }
      );
      setTodos(todos.map(todo => todo._id === id ? res.data : todo));
    } catch (err) {
      alert('Failed to update todo');
    }
  };

  const deleteTodo = async (id) => {
    try {
      await axios.delete(`${API_URL}/todos/${id}`, {
        headers: { 'x-auth-token': token }
      });
      setTodos(todos.filter(todo => todo._id !== id));
    } catch (err) {
      alert('Failed to delete todo');
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
    setTodos([]);
  };

  if (!token) {
    return (
      <div className="App">
        <div className="auth-container">
          <h1>MERN Todo App</h1>
          <div className="auth-toggle">
            <button 
              className={isLogin ? 'active' : ''} 
              onClick={() => setIsLogin(true)}
            >
              Login
            </button>
            <button 
              className={!isLogin ? 'active' : ''} 
              onClick={() => setIsLogin(false)}
            >
              Register
            </button>
          </div>
          
          <form onSubmit={handleAuthSubmit}>
            {!isLogin && (
              <input
                type="text"
                placeholder="Name"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                required
              />
            )}
            <input
              type="email"
              placeholder="Email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              required
            />
            <input
              type="password"
              placeholder="Password"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              required
            />
            <button type="submit">{isLogin ? 'Login' : 'Register'}</button>
          </form>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <header>
        <h1>My Todos</h1>
        <div className="user-info">
          <span>Welcome, {user?.name}!</span>
          <button onClick={logout}>Logout</button>
        </div>
      </header>

      <div className="todo-container">
        <form onSubmit={handleTodoSubmit} className="todo-form">
          <input
            type="text"
            placeholder="Todo title"
            value={todoForm.title}
            onChange={(e) => setTodoForm({ ...todoForm, title: e.target.value })}
            required
          />
          <input
            type="text"
            placeholder="Description (optional)"
            value={todoForm.description}
            onChange={(e) => setTodoForm({ ...todoForm, description: e.target.value })}
          />
          <button type="submit">Add Todo</button>
        </form>

        <div className="todos-list">
          {todos.length === 0 ? (
            <p className="no-todos">No todos yet. Add one above!</p>
          ) : (
            todos.map(todo => (
              <div key={todo._id} className={`todo-item ${todo.completed ? 'completed' : ''}`}>
                <div className="todo-content">
                  <h3 onClick={() => toggleComplete(todo._id, todo.completed)}>
                    {todo.completed && <span className="checkmark">✓ </span>}
                    {todo.title}
                  </h3>
                  {todo.description && <p>{todo.description}</p>}
                </div>
                <button onClick={() => deleteTodo(todo._id)} className="delete-btn">
                  Delete
                </button>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;