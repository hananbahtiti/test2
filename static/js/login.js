document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
    };

    try {
      const response = await fetch('/api/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      const messageDiv = document.getElementById('message');

      if (response.ok) {
        messageDiv.innerHTML = `<span style="color: green;">✅ ${result.message}</span>`;
        localStorage.setItem('token', result.token);
        setTimeout(() => window.location.href = '/dashboard/', 2000); // تحويل بعد الدخول
      } else {
        messageDiv.innerHTML = `<span style="color: red;">❌ ${result.error || JSON.stringify(result)}</span>`;
      }
    } catch (err) {
      document.getElementById('message').innerHTML = `<span style="color: red;">❌ Network error</span>`;
    }
  });